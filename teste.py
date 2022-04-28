from funcionario import Funcionario
from gerente import Gerente
from diretor import Diretor

g1 = Gerente('Fulano', 11111111111, 1000, '123')
f1 = Funcionario('Manoel', 99999999999, 1000)
d1 = Diretor('Ciclano', 00000000000, 1000, 777)

print(g1.bonificacao())
print(f1.bonificacao())
print(d1.bonificacao())