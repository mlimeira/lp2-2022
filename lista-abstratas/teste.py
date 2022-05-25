from conta import Conta
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente
from banco import Banco
from encapsulamento.conta_fantasma import ContaFantasma

#c1 = Conta(1, 'Fulano', 1000, '123')
c2 = ContaCorrente(2, 'Ciclano', 1000, '1234')
c3 = ContaPoupanca(3, 'Rogério', 1000, '123456')
c4 = ContaFantasma()

bb = Banco()
#bb.incluir_conta(c1)
bb.incluir_conta(c2)
bb.incluir_conta(c3)
#bb.incluir_conta(c4)

bb.atualizar_contas(0.1)