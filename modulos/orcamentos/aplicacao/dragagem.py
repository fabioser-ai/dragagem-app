"""Caso de uso da aba 6. Dragagem."""

from modulos.orcamentos.dominio.dragagem import Dragagem
from modulos.orcamentos.dominio.modelos import VersaoOrcamento


def salvar_dragagem(versao: VersaoOrcamento, dragagem: Dragagem):
    return versao.registrar_dragagem(dragagem)
