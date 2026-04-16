def fator_distancia(distancia):

    if distancia <= 1000:
        return 1
    elif distancia <= 3000:
        return 0.75
    else:
        return 0.55


def calcular_producao(vazao, distancia):
    return vazao * fator_distancia(distancia)


def calcular_tempo(volume, producao):
    return volume / producao


def calcular_dias(tempo_h, horas_dia):
    return tempo_h / horas_dia


def calcular_diesel(consumo, tempo_h, preco_diesel):
    return consumo * tempo_h * preco_diesel


def calcular_receita(volume, preco):
    return volume * preco


def calcular_lucro(receita, custo):
    return receita - custo
