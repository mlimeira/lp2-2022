from encapsulamento.banco import Banco
from encapsulamento.conta import Conta
from encapsulamento.emprestimo import Emprestimo

bb = Banco()
c1 = Conta(1, 'Fulano', 1000, 123, bb)
c2 = Conta(2, 'Ciclano', 2000, 123)
c3 = Conta(3, 'Beltrano', 3000, 123)

c1.depositar(500)
c2.sacar(500)
c3.sacar(2500)
c1.depositar(200)
c2.depositar(100)
c3.depositar(100)



bb.incluir_conta(c1)
bb.incluir_conta(c2)
bb.incluir_conta(c3)
bb.listar_contas()
bb.imprime_caixa()

e1 = Emprestimo(1000, 10, 0.1, c3)

for i in range(10):
    e1.pagar_parcela()
