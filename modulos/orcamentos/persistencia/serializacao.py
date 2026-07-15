"""Serialização JSON do domínio; o domínio não conhece este formato."""

import json

from modulos.orcamentos.dominio.estados import EstadoCenario, EstadoVersao
from modulos.orcamentos.dominio.identidades import CenarioId, OrcamentoId, VersaoId
from modulos.orcamentos.dominio.modelos import Cenario, Orcamento, VersaoOrcamento
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia

SCHEMA_VERSION = 1


def serializar_versao(orcamento: Orcamento, versao: VersaoOrcamento) -> str:
    if versao.orcamento_id != orcamento.id:
        raise ValueError("A versão não pertence ao orçamento informado.")
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
            "versao_anterior_id": (
                str(versao.versao_anterior_id) if versao.versao_anterior_id else None
            ),
            "cenario_adotado_id": (
                str(versao.cenario_adotado_id) if versao.cenario_adotado_id else None
            ),
            "cenarios": [
                {
                    "id": str(cenario.id),
                    "versao_id": str(cenario.versao_id),
                    "nome": cenario.nome,
                    "estado": cenario.estado.value,
                }
                for cenario in versao.cenarios
            ],
        },
    }
    return json.dumps(documento, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def desserializar_versao(conteudo: str) -> ResultadoPersistencia[tuple[Orcamento, VersaoOrcamento]]:
    try:
        documento = json.loads(conteudo)
    except (TypeError, json.JSONDecodeError):
        return _corrompido("JSON inválido.")
    try:
        if not isinstance(documento, dict) or documento.get("schema_version") != SCHEMA_VERSION:
            return _corrompido("Schema inválido ou não suportado.")
        if set(documento) != {"schema_version", "orcamento", "versao"}:
            return _corrompido("Estrutura raiz inválida.")
        dados_orcamento = documento["orcamento"]
        dados_versao = documento["versao"]
        if set(dados_orcamento) != {"id", "objeto", "finalidade", "responsavel"}:
            return _corrompido("Propriedades do orçamento inválidas.")
        campos_versao = {
            "id", "orcamento_id", "numero", "autor", "estado",
            "versao_anterior_id", "cenario_adotado_id", "cenarios",
        }
        if set(dados_versao) != campos_versao:
            return _corrompido("Propriedades da versão inválidas.")

        orcamento = Orcamento(
            OrcamentoId(dados_orcamento["id"]),
            dados_orcamento["objeto"],
            dados_orcamento["finalidade"],
            dados_orcamento["responsavel"],
        )
        orcamento_id_versao = OrcamentoId(dados_versao["orcamento_id"])
        if orcamento_id_versao != orcamento.id:
            return _corrompido("A versão pertence a outro orçamento.")
        versao = VersaoOrcamento(
            VersaoId(dados_versao["id"]),
            orcamento_id_versao,
            dados_versao["numero"],
            dados_versao["autor"],
            EstadoVersao(dados_versao["estado"]),
            VersaoId(dados_versao["versao_anterior_id"])
            if dados_versao["versao_anterior_id"] else None,
        )
        cenarios = {}
        for item in dados_versao["cenarios"]:
            if set(item) != {"id", "versao_id", "nome", "estado"}:
                return _corrompido("Propriedades de cenário inválidas.")
            cenario = Cenario(
                CenarioId(item["id"]), VersaoId(item["versao_id"]),
                item["nome"], EstadoCenario(item["estado"]),
            )
            if cenario.versao_id != versao.id or cenario.id in cenarios:
                return _corrompido("Cenário inválido ou pertencente a outra versão.")
            cenarios[cenario.id] = cenario
        adotado = (
            CenarioId(dados_versao["cenario_adotado_id"])
            if dados_versao["cenario_adotado_id"] else None
        )
        if adotado is not None:
            if adotado not in cenarios or cenarios[adotado].estado is not EstadoCenario.ATIVO:
                return _corrompido("Cenário adotado inválido.")
        if versao.estado in (EstadoVersao.CONGELADA, EstadoVersao.APROVADA):
            if not any(c.estado is EstadoCenario.ATIVO for c in cenarios.values()):
                return _corrompido("Versão congelada precisa de cenário ativo.")
        if versao.estado is EstadoVersao.APROVADA and adotado is None:
            return _corrompido("Versão aprovada precisa de cenário adotado.")
        object.__setattr__(versao, "_cenarios", cenarios)
        object.__setattr__(versao, "cenario_adotado_id", adotado)
        object.__setattr__(orcamento, "_versoes", {versao.id: versao})
        return ResultadoPersistencia(StatusPersistencia.SUCESSO, (orcamento, versao))
    except (KeyError, TypeError, ValueError, AttributeError):
        return _corrompido("Documento contém valor ou propriedade inválida.")


def _corrompido(mensagem: str):
    return ResultadoPersistencia(StatusPersistencia.DADO_CORROMPIDO, erro=mensagem)
