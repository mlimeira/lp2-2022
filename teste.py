from cliente import Cliente
from funcionario import Funcionario
from gerente import Gerente
from diretor import Diretor
from controle_bonificacao import ControleBonificacao

g1 = Gerente('Fulano', 11111111111, 1000, '123')
f1 = Funcionario('Manoel', 99999999999, 1000)
d1 = Diretor('Ciclano', 00000000000, 1000, 777)

print(g1.bonificacao())
print(f1.bonificacao())
print(d1.bonificacao())


cli = Cliente('Teste Cliente', 'Silva', 111111111)

cb = ControleBonificacao()

cb.registra(g1)
cb.registra(f1)
cb.registra(d1)
cb.registra(cli)

print(cb.get_total_bon())
