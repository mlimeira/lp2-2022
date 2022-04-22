from conta import Conta
from cliente import Cliente

#c1 = Conta(1,'Manoel', 1000)
#c2 = Conta(2,'Carlos', 10)
cli1 = Cliente('Manoel','L.',000000000000)
cli2 = Cliente('Carlos','A',111111111111)
c1 = Conta(1, cli1, 1000,'123')
c2 = Conta(2, cli2, 10,'123456')
c1.depositar(500)
c2.depositar(1200)
print(dir(c1))
#Acesso indevido ao atributo privado
#c1._saldo = 999999999
c1.sacar(2000)
c2.sacar(480)
c1.extrato.imprime()
print('===========')
c2.extrato.imprime()
print('Saldo:{}'.format(c1.saldo))
#c1.set_numero = 2000
print(Conta.get_total_contas())
#print('T:{} S:{}'.format(c2.titular.cpf, c2.saldo))
#c1.chave_pix = '123345878'
print(dir(c1))