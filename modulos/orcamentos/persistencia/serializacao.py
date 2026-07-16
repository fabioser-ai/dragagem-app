"""Serialização JSON do domínio; o domínio não conhece este formato."""

import json

from modulos.orcamentos.dominio.estados import EstadoCenario, EstadoVersao
from modulos.orcamentos.dominio.identidades import CenarioId, OrcamentoId, VersaoId
from modulos.orcamentos.dominio.modelos import Cenario, Orcamento, VersaoOrcamento
from modulos.orcamentos.dominio.premissas import OrigemPremissa, Premissa, ValorPremissa
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia

SCHEMA_VERSION = 3


def _valor_para_dict(valor):
    if valor is None:
        return None
    return {
        "valor": valor.valor,
        "unidade": valor.unidade,
        "origem": valor.origem.value,
        "autor": valor.autor,
        "vigencia": valor.vigencia,
        "justificativa": valor.justificativa,
    }


def _valor_de_dict(dados):
    if dados is None:
        return None
    campos = {"valor", "unidade", "origem", "autor", "vigencia", "justificativa"}
    if not isinstance(dados, dict) or set(dados) != campos:
        raise ValueError
    return ValorPremissa(
        dados["valor"], dados["unidade"], OrigemPremissa(dados["origem"]),
        dados["autor"], dados["vigencia"], dados["justificativa"],
    )


def serializar_versao(orcamento: Orcamento, versao: VersaoOrcamento) -> str:
    if versao.orcamento_id != orcamento.id:
        raise ValueError("A versão não pertence ao orçamento informado.")
    grupos = []
    for (cenario_id, conceito), historico in versao._premissas.items():
        grupos.append({
            "cenario_id": str(cenario_id),
            "conceito": conceito,
            "historico": [
                {
                    "sequencia": registro.sequencia,
                    "sugerido": _valor_para_dict(registro.sugerido),
                    "adotado": _valor_para_dict(registro.adotado),
                }
                for registro in historico
            ],
        })
    documento = {
        "schema_version": SCHEMA_VERSION,
        "orcamento": {
            "id": str(orcamento.id),
            "objeto": orcamento.objeto,
            "finalidade": orcamento.finalidade,
            "responsavel": orcamento.responsavel,
        },
        "versao": {
            "id": str(versao.id),
            "orcamento_id": str(versao.orcamento_id),
            "numero": versao.numero,
            "autor": versao.autor,
            "estado": versao.estado.value,
            "versao_anterior_id": str(versao.versao_anterior_id) if versao.versao_anterior_id else None,
            "cenario_adotado_id": str(versao.cenario_adotado_id) if versao.cenario_adotado_id else None,
            "cenarios": [
                {"id": str(c.id), "versao_id": str(c.versao_id), "nome": c.nome, "estado": c.estado.value}
                for c in versao.cenarios
            ],
            "premissas": grupos,
        },
    }
    return json.dumps(documento, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def desserializar_versao(conteudo: str):
    try:
        documento = json.loads(conteudo)
    except (TypeError, json.JSONDecodeError):
        return _corrompido("JSON inválido.")
    try:
        schema = documento.get("schema_version") if isinstance(documento, dict) else None
        if schema not in (1, SCHEMA_VERSION) or set(documento) != {"schema_version", "orcamento", "versao"}:
            return _corrompido("Schema inválido ou não suportado.")
        dados_o, dados_v = documento["orcamento"], documento["versao"]
        if set(dados_o) != {"id", "objeto", "finalidade", "responsavel"}:
            return _corrompido("Propriedades do orçamento inválidas.")
        campos_v1 = {
            "id", "orcamento_id", "numero", "autor", "estado",
            "versao_anterior_id", "cenario_adotado_id", "cenarios",
        }
        esperados = campos_v1 | ({"premissas"} if schema == SCHEMA_VERSION else set())
        if set(dados_v) != esperados:
            return _corrompido("Propriedades da versão inválidas.")

        orcamento = Orcamento(
            OrcamentoId(dados_o["id"]), dados_o["objeto"],
            dados_o["finalidade"], dados_o["responsavel"],
        )
        orcamento_id = OrcamentoId(dados_v["orcamento_id"])
        if orcamento_id != orcamento.id:
            return _corrompido("A versão pertence a outro orçamento.")
        versao = VersaoOrcamento(
            VersaoId(dados_v["id"]), orcamento_id, dados_v["numero"], dados_v["autor"],
            EstadoVersao(dados_v["estado"]),
            VersaoId(dados_v["versao_anterior_id"]) if dados_v["versao_anterior_id"] else None,
        )

        cenarios = {}
        for item in dados_v["cenarios"]:
            if set(item) != {"id", "versao_id", "nome", "estado"}:
                raise ValueError
            cenario = Cenario(
                CenarioId(item["id"]), VersaoId(item["versao_id"]),
                item["nome"], EstadoCenario(item["estado"]),
            )
            if cenario.versao_id != versao.id or cenario.id in cenarios:
                raise ValueError
            cenarios[cenario.id] = cenario

        premissas = {}
        for grupo in dados_v.get("premissas", []):
            if set(grupo) != {"cenario_id", "conceito", "historico"}:
                raise ValueError
            cenario_id = CenarioId(grupo["cenario_id"])
            if cenario_id not in cenarios or not isinstance(grupo["historico"], list):
                raise ValueError
            historico = []
            for item in grupo["historico"]:
                if set(item) != {"sequencia", "sugerido", "adotado"}:
                    raise ValueError
                registro = Premissa(
                    grupo["conceito"], item["sequencia"],
                    _valor_de_dict(item["sugerido"]), _valor_de_dict(item["adotado"]),
                )
                if registro.sequencia != len(historico) + 1:
                    raise ValueError
                historico.append(registro)
            chave = (cenario_id, grupo["conceito"])
            if not historico or chave in premissas:
                raise ValueError
            premissas[chave] = tuple(historico)

        adotado = CenarioId(dados_v["cenario_adotado_id"]) if dados_v["cenario_adotado_id"] else None
        if adotado is not None and (
            adotado not in cenarios or cenarios[adotado].estado is not EstadoCenario.ATIVO
        ):
            raise ValueError
        if versao.estado in (EstadoVersao.CONGELADA, EstadoVersao.APROVADA) and not any(
            c.estado is EstadoCenario.ATIVO for c in cenarios.values()
        ):
            raise ValueError
        if versao.estado is EstadoVersao.APROVADA and adotado is None:
            raise ValueError
        object.__setattr__(versao, "_cenarios", cenarios)
        object.__setattr__(versao, "_premissas", premissas)
        object.__setattr__(versao, "cenario_adotado_id", adotado)
        object.__setattr__(orcamento, "_versoes", {versao.id: versao})
        return ResultadoPersistencia(StatusPersistencia.SUCESSO, (orcamento, versao))
    except (KeyError, TypeError, ValueError, AttributeError):
        return _corrompido("Documento contém valor ou propriedade inválida.")


def _corrompido(mensagem: str):
    return ResultadoPersistencia(StatusPersistencia.DADO_CORROMPIDO, erro=mensagem)
