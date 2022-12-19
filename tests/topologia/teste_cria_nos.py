import pytest

from theqube_qunet import theqube_qunet
from theqube_qunet.topologia.topologia import Topologia


@pytest.fixture
def teste_cria_nos():
    rede = Topologia('Rede Teste', {})
    rede.criar_nós(
        {'A': {'num_qubits': 2, 'tipo': 'Supercondutor', 'processador': False, 'detector': False, 'ruído': None},
         'B': {'num_qubits': 3, 'tipo': 'Vacância de Diamante', 'processador': True, 'detector': False, 'ruído': None},
         'C': {'num_qubits': 5, 'tipo': 'Sistema 3', 'processador': False, 'detector': True, 'ruído': None}}
    )
    resultado = rede.listar_nós()
    esperado = '\n A 2 Supercondutor False False None\n B 3 Vacância de Diamante True False None\n C 5 Sistema 3 ' \
               'False True None '
    assert resultado == esperado
