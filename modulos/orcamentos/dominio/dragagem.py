"""Equivalência funcional mínima da aba 6. Dragagem."""

from dataclasses import dataclass
import math


def _numero(valor, campo):
    if valor is not None and (
        isinstance(valor, bool) or not isinstance(valor, (int, float))
        or not math.isfinite(valor) or valor < 0
    ):
        raise ValueError(f"{campo} deve ser numérico não negativo ou vazio.")
    return float(valor) if valor is not None else None


@dataclass(frozen=True, slots=True)
class EntradaDragagem:
    celula: str
    bloco: str
    descricao: str
    valor: float | None
    unidade: str = ""

    def __post_init__(self):
        for campo in ("celula", "bloco", "descricao", "unidade"):
            valor = getattr(self, campo)
            if not isinstance(valor, str) or (campo != "unidade" and not valor.strip()):
                raise ValueError(f"{campo} inválido.")
            object.__setattr__(self, campo, valor.strip())
        object.__setattr__(self, "valor", _numero(self.valor, self.celula))


def _entradas_iniciais():
    dados = (
        ("F7", "Identificação", 'Valor "no estado"', 150000, "R$"),
        ("C9", "I - Operação", "Quantidade de horas/mês", 198, "h"),
        ("D9", "I - Operação", "Eficiência", .9, "fator"),
        ("E9", "I - Operação", "Consumo por hora", 7, "l/h"),
        ("F9", "I - Operação", "Valor do combustível", 9, "R$/l"),
        ("F12", "I - Operação", "Fretes e carretos", 2000, "R$/mês"),
        ("F13", "I - Operação", "Materiais de segurança e uniformes", 500, "R$/mês"),
        ("P12", "Referências informativas", "Operador", 28.35, "R$/h"),
        ("P13", "Referências informativas", "ajudante", 11.13, "R$/h"),
        ("P14", "Referências informativas", "Operador sistema de desidrataçao", 15.15, "R$/h"),
        ("B20", "II - Pessoal / salários", "Quantidade — Engenheiro", None, "pessoa"),
        ("D20", "II - Pessoal / salários", "Unitário — Engenheiro", 25, "R$/h"),
        ("J20", "II - Pessoal / memorial de horas", "Horas extras (70%)", .5, "h/dia"),
        ("K20", "II - Pessoal / memorial de horas", "Dias — horas extras (70%)", 22, "dias"),
        ("B21", "II - Pessoal / salários", "Quantidade — Encarregado", None, "pessoa"),
        ("D21", "II - Pessoal / salários", "Unitário — Encarregado", 20, "R$/h"),
        ("J21", "II - Pessoal / memorial de horas", "Horas extras (100%)", 0, "h/dia"),
        ("K21", "II - Pessoal / memorial de horas", "Dias — horas extras (100%)", 1, "dia"),
        ("B22", "II - Pessoal / salários", "Quantidade — Operador de draga", 1, "pessoa"),
        ("D22", "II - Pessoal / salários", "Unitário — Operador de draga", 28.35, "R$/h"),
        ("B23", "II - Pessoal / salários", "Quantidade — Ajudante", 1, "pessoa"),
        ("D23", "II - Pessoal / salários", "Unitário — Ajudante", 11.13, "R$/h"),
        ("J23", "II - Pessoal / memorial de horas", "Horas normais", 7.33333, "h/dia"),
        ("K23", "II - Pessoal / memorial de horas", "Dias — horas normais", 30, "dias"),
        ("B24", "II - Pessoal / salários", "Quantidade — Técnico de Segurança", None, "pessoa"),
        ("D24", "II - Pessoal / salários", "Unitário — Técnico de Segurança", 15, "R$/h"),
        ("B25", "II - Pessoal / salários", "Quantidade — Motorista", None, "pessoa"),
        ("D25", "II - Pessoal / salários", "Unitário — Motorista", 7.5, "R$/h"),
        ("B26", "II - Pessoal / salários", "Quantidade — Operador booster", None, "pessoa"),
        ("D26", "II - Pessoal / salários", "Unitário — Operador booster", 12.5, "R$/h"),
        ("B27", "II - Pessoal / salários", "Quantidade — Administrativo", None, "pessoa"),
        ("D27", "II - Pessoal / salários", "Unitário — Administrativo", 9.1, "R$/h"),
        ("E28", "II - Pessoal / salários", "Linha sem identificação no total de salários", None, "R$"),
        ("A37", "II - Pessoal / encargos", "Taxa sobre salários", 110, "%"),
        ("C42", "II - Pessoal / cantina informativa", "Almoço por pessoa", 10, "R$"),
        ("C43", "II - Pessoal / cantina informativa", "Café por pessoa", 2.5, "R$"),
        ("C44", "II - Pessoal / cantina informativa", "Lanche por pessoa", 2.5, "R$"),
        ("C45", "II - Pessoal / cantina informativa", "Jantar por pessoa", 10, "R$"),
        ("B52", "II - Pessoal / refeições", "Funcionários alojados", 1, "pessoa"),
        ("C52", "II - Pessoal / refeições", "Café — alojados", 5, "R$"),
        ("D52", "II - Pessoal / refeições", "Almoço — alojados", 15, "R$"),
        ("E52", "II - Pessoal / refeições", "Jantar — alojados", 15, "R$"),
        ("F52", "II - Pessoal / refeições", "Dias — alojados", 30, "dias"),
        ("B53", "II - Pessoal / refeições", "Funcionários da cidade", 1, "pessoa"),
        ("C53", "II - Pessoal / refeições", "Café — cidade", 5, "R$"),
        ("D53", "II - Pessoal / refeições", "Almoço — cidade", 15, "R$"),
        ("E53", "II - Pessoal / refeições", "Jantar — cidade", None, "R$"),
        ("F53", "II - Pessoal / refeições", "Dias — cidade", 22, "dias"),
        ("C59", "II - Pessoal / alojamento", "Aluguel", None, "R$"),
        ("C60", "II - Pessoal / alojamento", "Água e luz", None, "R$"),
        ("C61", "II - Pessoal / alojamento", "Multa por rescisão", None, "R$"),
        ("C62", "II - Pessoal / alojamento", "Limpeza", 100, "R$"),
        ("E67", "II - Pessoal / viagens", "Valor — Engenheiro", None, "R$"),
        ("E68", "II - Pessoal / viagens", "Valor — Encarregado", None, "R$"),
        ("B69", "II - Pessoal / viagens", "Quantidade — Funcionários", 1, "pessoa"),
        ("D69", "II - Pessoal / viagens", "Unitário — Funcionários", None, "R$"),
        ("B82", "II - Pessoal / prêmios", "Quantidade — Engenheiro", None, "pessoa"),
        ("D82", "II - Pessoal / prêmios", "Unitário — Engenheiro", None, "R$"),
        ("E82", "II - Pessoal / prêmios", "Valor — Engenheiro", None, "R$"),
        ("B83", "II - Pessoal / prêmios", "Quantidade — Encarregado", None, "pessoa"),
        ("D83", "II - Pessoal / prêmios", "Unitário — Encarregado", None, "R$"),
        ("E83", "II - Pessoal / prêmios", "Valor — Encarregado", None, "R$"),
        ("B84", "II - Pessoal / prêmios", "Quantidade — Draguistas", None, "pessoa"),
        ("D84", "II - Pessoal / prêmios", "Unitário — Draguistas", None, "R$"),
        ("E84", "II - Pessoal / prêmios", "Valor — Draguistas", None, "R$"),
        ("B85", "II - Pessoal / prêmios", "Quantidade — Ajudantes", None, "pessoa"),
        ("D85", "II - Pessoal / prêmios", "Unitário — Ajudantes", None, "R$"),
        ("E85", "II - Pessoal / prêmios", "Valor — Ajudantes", None, "R$"),
        ("E141", "III - Manutenção", "Limpeza e pintura", 250, "R$/mês"),
        ("E142", "III - Manutenção", "Mão de obra de terceiros", 250, "R$/mês"),
        ("E151", "IV - Equipamentos de apoio", "Batimetria final", None, "R$"),
        ("E152", "IV - Equipamentos de apoio", "Pick-Up", None, "R$"),
        ("E153", "IV - Equipamentos de apoio", "Medidor de vazão + densidade", None, "R$"),
        ("E154", "IV - Equipamentos de apoio", "Automóvel (carros + combustível)", 4000, "R$"),
        ("E155", "IV - Equipamentos de apoio", "Máquina de solda", None, "R$"),
        ("E156", "IV - Equipamentos de apoio", "Maçarico", None, "R$"),
        ("E157", "IV - Equipamentos de apoio", "Ferramentas", None, "R$"),
        ("E159", "IV - Equipamentos de apoio", "Linha vazia do total de apoio", None, "R$"),
        ("I151", "IV - Linha de recalque", "Tubulação — quantidade", 250, "m"),
        ("J151", "IV - Linha de recalque", "Tubulação — preço por metro", 150, "R$/m"),
        ("I152", "IV - Linha de recalque", "Tubulação — depreciação", 12, "meses"),
        ("I153", "IV - Linha de recalque", "Tubulação — juros", 1, "%"),
        ("I156", "IV - Linha de recalque", "Flutuante — quantidade", 37.5, "pç"),
        ("J156", "IV - Linha de recalque", "Flutuante — preço por peça", 200, "R$/pç"),
        ("I157", "IV - Linha de recalque", "Flutuante — depreciação", 12, "meses"),
        ("I158", "IV - Linha de recalque", "Flutuante — juros", 1, "%"),
        ("J161", "IV - Linha de recalque", "Acoplamento — preço por peça", 150, "R$/pç"),
        ("I162", "IV - Linha de recalque", "Acoplamento — depreciação", 12, "meses"),
        ("I163", "IV - Linha de recalque", "Acoplamento — juros", 1, "%"),
        ("E173", "V - Administrativas", "Comissões", 0, "R$"),
        ("E174", "V - Administrativas", "Viagens de inspeção", 200, "R$"),
        ("E175", "V - Administrativas", "Viagens administrativas", 0, "R$"),
        ("E176", "V - Administrativas", "Comunicações", 300, "R$"),
        ("E177", "V - Administrativas", "Seguro e licenciamento", None, "R$"),
        ("E187", "VI - B.D.I.", "Outros (percentual/valor não preenchido e não somado)", None, "R$"),
        ("D225", "Resumo", "Produção prevista", 1930.5, "m³/mês"),
        ("D227", "Resumo", "Custo unitário", None, "R$/m³"),
        ("D229", "Resumo", "BDI", None, "R$/m³"),
        ("H235", "Hora à disposição", "Quantidade de dias", 22, "dias"),
        ("I235", "Hora à disposição", "Horas por dia", 9, "h/dia"),
        ("J248", "Preço de operação por hora", "BDI", 1.6, "fator"),
        ("J250", "Preço de operação por hora", "Horas trabalhadas/mês", 198, "h"),
        ("L250", "Preço de operação por hora", "Fator da hora à disposição", .6, "fator"),
        ("J251", "Preço de operação por hora", "Eficiência de operação", .6, "fator"),
    )
    return tuple(EntradaDragagem(*item) for item in dados)


@dataclass(frozen=True, slots=True)
class Dragagem:
    entradas: tuple[EntradaDragagem, ...] = _entradas_iniciais()

    def __post_init__(self):
        if not isinstance(self.entradas, tuple) or not all(isinstance(x, EntradaDragagem) for x in self.entradas):
            raise ValueError("Entradas de Dragagem inválidas.")
        celulas = [x.celula for x in self.entradas]
        if len(celulas) != len(set(celulas)):
            raise ValueError("Células de entrada de Dragagem devem ser únicas.")


@dataclass(frozen=True, slots=True)
class ResultadosDragagem:
    celulas: dict[str, float | None]

    def valor(self, celula):
        return self.celulas.get(celula)


OBSERVACOES_DRAGAGEM = (
    'A1 contém manualmente "5. ", embora o nome da aba seja 6. Dragagem.',
    'Título: CUSTO DE DRAGAGEM, Canteiro e Operação do Sistema de Desidratação de lodo.',
    'DATA:  28/05/2021 · CLIENTE:  SABESP CUBATAO · EQUIPAMENTO: Draga 6".',
    'Turno: 8h = 260h/H.mês; referência adicional: 12h = 420h/H.mês.',
    'O Excel escreve Total "Desesas Diretas" e repete a letra b) no bloco de B.D.I.',
    'Prêmios de Produção e cantina unitária são informativos e não entram em G87.',
)


FORMULAS_DRAGAGEM = (
    ("F10", "=C9*D9*E9*F9"), ("F11", "=F10*0.1"),
    ("E15", "=F10+F11+F12+F13"), ("A20", "=L24"),
    ("E20", "=D20*B20*A20"), ("L20", "=J20*K20"),
    ("A21", "=L24"), ("E21", "=D21*B21*A21"), ("L21", "=J21*K21"),
    ("A22", "=L24"), ("E22", "=D22*B22*A22"),
    ("A23", "=L24"), ("E23", "=D23*B23*A23"), ("L23", "=J23*K23"),
    ("A24", "=L24"), ("E24", "=D24*B24*A24"),
    ("L24", "=(L20*1.7)+(L21*2)+L23"),
    ("A25", "=L24"), ("E25", "=D25*B25*A25"),
    ("A26", "=L24"), ("E26", "=D26*B26*A26"),
    ("A27", "=L24"), ("E27", "=D27*B27*A27"),
    ("E31", "=E20+E21+E22+E23+E24+E25+E26+E27+E28"),
    ("C37", "=E31"), ("E37", "=(C37*A37)/100"),
    ("E46", "=G52+G53"), ("G52", "=B52*(C52+D52+E52)*F52"),
    ("G53", "=B53*(C53+D53+E53)*F53"), ("E62", "=C59+C60+C61+C62"),
    ("E69", "=D69*B69"), ("E71", "=SUM(E67:E69)"),
    ("G87", "=E71+E62+E46+E37+E31"),
    ("E139", "=(0.6/100)*F7"), ("E140", "=(1/100)*F7"),
    ("E144", "=E139+E140+E141+E142"), ("H146", "=E144"),
    ("E150", "=K167"), ("K151", "=I151*J151"),
    ("J152", "=K151/I152"), ("J153", "=K151*(1/100)"),
    ("J154", "=SUM(J152:J153)"), ("K156", "=I156*J156"),
    ("J157", "=K156/I157"), ("E158", "=Canteiro!F32"),
    ("J158", "=K156*(1/100)"), ("J159", "=SUM(J157:J158)"),
    ("D161", "=E150+E151+E152+E155+E156+E157+E158+E159+E153+E154"),
    ("I161", "=(I151/12)+2"), ("K161", "=I161*J161"),
    ("J162", "=K161/I162"), ("J163", "=K161*(1/100)"),
    ("J164", "=SUM(J162:J163)"), ("H167", "=J154"),
    ("I167", "=J159"), ("J167", "=J164"), ("K167", "=SUM(H167:J167)"),
    ("E178", "=E173+E174+E175+E176+E177"),
    ("G181", "=E178+D161+H146+G87+E15"),
    ("E185", "=G181*(5/100)"), ("E186", "=G181*(5/100)"),
    ("E189", "=E185+E186"), ("E192", "=F7/60"),
    ("E193", "=F7*0.01"), ("E194", "=G181*0.005"),
    ("E196", "=E192+E193+E194"), ("D215", "=G181"),
    ("D218", "=E189"), ("D220", "=E196"),
    ("D222", "=D215+D218+D220"), ("D231", "=D227+D229"),
    ("D234", "=J253*0.6*0.62"), ("J235", "=H235*I235"),
    ("D244", "=D222"), ("D245", "='5. Operação Sistema'!F24"),
    ("D246", "=SUM(D244:D245)"), ("D247", "=ROUNDUP(Produção!D24,0)"),
    ("J247", "=D246"), ("D248", "=D246*D247"),
    ("J249", "=J247*J248"), ("L249", "=J249/J250"),
    ("L251", "=L249*L250"), ("J252", "=J250*J251"),
    ("J253", "=J249/J252"),
)


def calcular_dragagem(
    dragagem: Dragagem,
    canteiro_f32: float | None,
    operacao_sistema_f24: float | None,
    producao_d24: float | None,
) -> ResultadosDragagem:
    """Reproduz as 84 fórmulas reais, na ordem de dependência da planilha."""
    v = {x.celula: x.valor for x in dragagem.entradas}
    z = lambda celula: 0.0 if v.get(celula) is None else v[celula]
    div = lambda a, b: None if b in (None, 0) else (0.0 if a is None else a) / b

    v["F10"] = z("C9") * z("D9") * z("E9") * z("F9")
    v["F11"] = z("F10") * .1
    v["E15"] = sum(z(x) for x in ("F10", "F11", "F12", "F13"))
    v["L20"] = z("J20") * z("K20"); v["L21"] = z("J21") * z("K21")
    v["L23"] = z("J23") * z("K23")
    v["L24"] = z("L20") * 1.7 + z("L21") * 2 + z("L23")
    for linha in range(20, 28):
        v[f"A{linha}"] = v["L24"]
        v[f"E{linha}"] = z(f"D{linha}") * z(f"B{linha}") * z(f"A{linha}")
    v["E31"] = sum(z(f"E{x}") for x in range(20, 29))
    v["C37"] = v["E31"]; v["E37"] = z("C37") * z("A37") / 100
    v["G52"] = z("B52") * (z("C52") + z("D52") + z("E52")) * z("F52")
    v["G53"] = z("B53") * (z("C53") + z("D53") + z("E53")) * z("F53")
    v["E46"] = z("G52") + z("G53")
    v["E62"] = sum(z(x) for x in ("C59", "C60", "C61", "C62"))
    v["E69"] = z("D69") * z("B69")
    v["E71"] = z("E67") + z("E68") + z("E69")
    v["G87"] = sum(z(x) for x in ("E71", "E62", "E46", "E37", "E31"))
    v["E139"] = .006 * z("F7"); v["E140"] = .01 * z("F7")
    v["E144"] = sum(z(x) for x in ("E139", "E140", "E141", "E142")); v["H146"] = v["E144"]
    v["K151"] = z("I151") * z("J151"); v["J152"] = div(v["K151"], v.get("I152"))
    v["J153"] = z("K151") * .01; v["J154"] = z("J152") + z("J153")
    v["K156"] = z("I156") * z("J156"); v["J157"] = div(v["K156"], v.get("I157"))
    v["E158"] = canteiro_f32; v["J158"] = z("K156") * .01
    v["J159"] = z("J157") + z("J158")
    v["I161"] = z("I151") / 12 + 2; v["K161"] = z("I161") * z("J161")
    v["J162"] = div(v["K161"], v.get("I162")); v["J163"] = z("K161") * .01
    v["J164"] = z("J162") + z("J163")
    v["H167"], v["I167"], v["J167"] = v["J154"], v["J159"], v["J164"]
    v["K167"] = z("H167") + z("I167") + z("J167"); v["E150"] = v["K167"]
    v["D161"] = sum(z(x) for x in ("E150", "E151", "E152", "E155", "E156", "E157", "E158", "E159", "E153", "E154"))
    v["E178"] = sum(z(f"E{x}") for x in range(173, 178))
    v["G181"] = sum(z(x) for x in ("E178", "D161", "H146", "G87", "E15"))
    v["E185"] = z("G181") * .05; v["E186"] = z("G181") * .05
    v["E189"] = z("E185") + z("E186")
    v["E192"] = z("F7") / 60; v["E193"] = z("F7") * .01; v["E194"] = z("G181") * .005
    v["E196"] = z("E192") + z("E193") + z("E194")
    v["D215"], v["D218"], v["D220"] = v["G181"], v["E189"], v["E196"]
    v["D222"] = z("D215") + z("D218") + z("D220")
    v["D231"] = z("D227") + z("D229")
    v["J235"] = z("H235") * z("I235")
    v["D244"] = v["D222"]; v["D245"] = operacao_sistema_f24
    v["D246"] = z("D244") + z("D245")
    v["D247"] = math.ceil(producao_d24) if producao_d24 is not None else None
    v["J247"] = v["D246"]; v["D248"] = z("D246") * z("D247")
    v["J249"] = z("J247") * z("J248"); v["L249"] = div(v["J249"], v.get("J250"))
    v["L251"] = None if v["L249"] is None else v["L249"] * z("L250")
    v["J252"] = z("J250") * z("J251"); v["J253"] = div(v["J249"], v["J252"])
    v["D234"] = None if v["J253"] is None else v["J253"] * .6 * .62
    return ResultadosDragagem(v)
