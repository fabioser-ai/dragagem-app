"""Serialização JSON do domínio; o domínio não conhece este formato."""

import json
from dataclasses import asdict
from datetime import date

from modulos.orcamentos.dominio.barrilete import Barrilete, ItemBarrilete
from modulos.orcamentos.dominio.cotacoes import (
    Cotacoes,
    ItemCotacao,
    PropostaFornecedor,
)
from modulos.orcamentos.dominio.dados_obra import DadosObra
from modulos.orcamentos.dominio.estados import EstadoCenario, EstadoVersao
from modulos.orcamentos.dominio.identidades import CenarioId, OrcamentoId, VersaoId
from modulos.orcamentos.dominio.modelos import Cenario, Orcamento, VersaoOrcamento
from modulos.orcamentos.dominio.premissas import OrigemPremissa, Premissa, ValorPremissa
from modulos.orcamentos.dominio.producao import Producao
from modulos.orcamentos.persistencia.contratos import ResultadoPersistencia, StatusPersistencia

SCHEMA_VERSION = 8


def _dados_obra_para_dict(dados):
    if dados is None:
        return None
    documento = asdict(dados)
    documento["data"] = dados.data.isoformat()
    return documento


def _dados_obra_de_dict(dados):
    if dados is None:
        return None
    esperados = set(DadosObra.__dataclass_fields__)
    if not isinstance(dados, dict) or set(dados) != esperados:
        raise ValueError
    valores = dict(dados)
    valores["data"] = date.fromisoformat(valores["data"])
    return DadosObra(**valores)


def _cotacoes_para_dict(cotacoes):
    return asdict(cotacoes) if cotacoes is not None else None


def _proposta_de_dict(dados):
    campos = {
        "nome", "contato", "telefone", "detalhe",
        "primeiro_valor", "segundo_valor",
    }
    if not isinstance(dados, dict) or set(dados) != campos:
        raise ValueError
    return PropostaFornecedor(**dados)


def _cotacoes_schema_5(dados):
    campos = {"guindaste", "container", "banheiro_quimico", "destinacao"}
    if not isinstance(dados, dict) or set(dados) != campos:
        raise ValueError

    def propostas(linhas, primeiro, segundo):
        resultado = []
        for linha in linhas:
            campos_linha = {"nome", "contato", "telefone", "detalhe", primeiro}
            if segundo:
                campos_linha.add(segundo)
            if not isinstance(linha, dict) or set(linha) != campos_linha:
                raise ValueError
            resultado.append(
                PropostaFornecedor(
                    linha["nome"],
                    linha["contato"],
                    linha["telefone"],
                    linha["detalhe"],
                    linha[primeiro],
                    linha[segundo] if segundo else None,
                )
            )
        return tuple(resultado)

    return Cotacoes(
        (
            ItemCotacao(
                "inicial-guindaste", "Guindaste", "Preço por hora", "Preço por diária",
                propostas(dados["guindaste"], "preco_hora", "preco_diaria"),
            ),
            ItemCotacao(
                "inicial-container", "Container", "Preço por mês", "Frete por hora",
                propostas(dados["container"], "preco_mes", "frete_hora"),
            ),
            ItemCotacao(
                "inicial-banheiro-quimico", "Banheiro Químico", "Preço por mês", None,
                propostas(dados["banheiro_quimico"], "preco_mes", None),
            ),
            ItemCotacao(
                "inicial-destinacao", "Destinação", "Preço por mês", None,
                propostas(dados["destinacao"], "preco_mes", None),
            ),
        )
    )


def _cotacoes_de_dict(dados, schema):
    if dados is None:
        return Cotacoes.iniciais()
    if schema == 5:
        return _cotacoes_schema_5(dados)
    if not isinstance(dados, dict) or set(dados) != {"itens"}:
        raise ValueError
    itens = []
    campos_item = {
        "id", "nome", "rotulo_primeiro_valor", "rotulo_segundo_valor", "propostas"
    }
    for dados_item in dados["itens"]:
        if not isinstance(dados_item, dict) or set(dados_item) != campos_item:
            raise ValueError
        itens.append(
            ItemCotacao(
                dados_item["id"],
                dados_item["nome"],
                dados_item["rotulo_primeiro_valor"],
                dados_item["rotulo_segundo_valor"],
                tuple(_proposta_de_dict(item) for item in dados_item["propostas"]),
            )
        )
    return Cotacoes(tuple(itens))


def _producao_de_dict(dados):
    if dados is None:
        return Producao()
    campos = {"vazao", "eficiencia", "concentracao"}
    if not isinstance(dados, dict) or set(dados) != campos:
        raise ValueError
    return Producao(**dados)


def _barrilete_de_dict(dados):
    if dados is None:
        return Barrilete()
    campos = {
        "quantidade_operadores", "custo_hora_operador", "encargos_operador",
        "quantidade_ajudantes", "custo_hora_ajudante", "encargos_ajudante",
        "custo_refeicao", "custo_transporte", "itens", "bdi",
    }
    if not isinstance(dados, dict) or set(dados) != campos or not isinstance(dados["itens"], list):
        raise ValueError
    campos_item = {
        "id", "descricao", "unidade", "quantidade", "preco_base",
        "multiplicador_preco", "preco_unitario_manual", "preco_total_informado",
    }
    itens = []
    for dados_item in dados["itens"]:
        if not isinstance(dados_item, dict) or set(dados_item) != campos_item:
            raise ValueError
        itens.append(ItemBarrilete(**dados_item))
    valores = dict(dados)
    valores["itens"] = tuple(itens)
    return Barrilete(**valores)


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
    dados_versao = {
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
        "dados_obra": _dados_obra_para_dict(versao.dados_obra),
    }
    if versao.cotacoes is not None:
        dados_versao["cotacoes"] = _cotacoes_para_dict(versao.cotacoes)
    dados_versao["producao"] = asdict(versao.producao)
    dados_versao["barrilete"] = asdict(versao.barrilete)
    documento = {
        "schema_version": SCHEMA_VERSION,
        "orcamento": {
            "id": str(orcamento.id),
            "objeto": orcamento.objeto,
            "finalidade": orcamento.finalidade,
            "responsavel": orcamento.responsavel,
        },
        "versao": dados_versao,
    }
    return json.dumps(documento, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def desserializar_versao(conteudo: str):
    try:
        documento = json.loads(conteudo)
    except (TypeError, json.JSONDecodeError):
        return _corrompido("JSON inválido.")
    try:
        schema = documento.get("schema_version") if isinstance(documento, dict) else None
        if schema not in (1, 3, 4, 5, 6, 7, SCHEMA_VERSION) or set(documento) != {"schema_version", "orcamento", "versao"}:
            return _corrompido("Schema inválido ou não suportado.")
        dados_o, dados_v = documento["orcamento"], documento["versao"]
        if set(dados_o) != {"id", "objeto", "finalidade", "responsavel"}:
            return _corrompido("Propriedades do orçamento inválidas.")
        campos_v1 = {
            "id", "orcamento_id", "numero", "autor", "estado",
            "versao_anterior_id", "cenario_adotado_id", "cenarios",
        }
        campos_por_schema = {
            1: (campos_v1, campos_v1 | {"dados_obra"}),
            3: (campos_v1 | {"premissas"}, campos_v1 | {"premissas"}),
            4: (
                campos_v1 | {"premissas", "dados_obra"},
                campos_v1 | {"premissas", "dados_obra"},
            ),
            5: (
                campos_v1 | {"premissas", "dados_obra"},
                campos_v1 | {"premissas", "dados_obra", "cotacoes"},
            ),
            6: (
                campos_v1 | {"premissas", "dados_obra", "cotacoes"},
                campos_v1 | {"premissas", "dados_obra", "cotacoes"},
            ),
            7: (
                campos_v1 | {"premissas", "dados_obra", "cotacoes", "producao"},
                campos_v1 | {"premissas", "dados_obra", "cotacoes", "producao"},
            ),
            SCHEMA_VERSION: (
                campos_v1 | {
                    "premissas", "dados_obra", "cotacoes", "producao", "barrilete"
                },
                campos_v1 | {
                    "premissas", "dados_obra", "cotacoes", "producao", "barrilete"
                },
            ),
        }
        obrigatorios, permitidos = campos_por_schema[schema]
        if not obrigatorios.issubset(dados_v) or not set(dados_v).issubset(permitidos):
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
        object.__setattr__(
            versao, "_dados_obra", _dados_obra_de_dict(dados_v.get("dados_obra"))
        )
        object.__setattr__(
            versao, "_cotacoes", _cotacoes_de_dict(dados_v.get("cotacoes"), schema)
        )
        object.__setattr__(versao, "_producao", _producao_de_dict(dados_v.get("producao")))
        object.__setattr__(
            versao, "_barrilete", _barrilete_de_dict(dados_v.get("barrilete"))
        )
        object.__setattr__(versao, "cenario_adotado_id", adotado)
        object.__setattr__(orcamento, "_versoes", {versao.id: versao})
        return ResultadoPersistencia(StatusPersistencia.SUCESSO, (orcamento, versao))
    except (KeyError, TypeError, ValueError, AttributeError):
        return _corrompido("Documento contém valor ou propriedade inválida.")


def _corrompido(mensagem: str):
    return ResultadoPersistencia(StatusPersistencia.DADO_CORROMPIDO, erro=mensagem)
