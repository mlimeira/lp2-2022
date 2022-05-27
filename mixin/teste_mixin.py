from diretor import Diretor
from gerente import Gerente

g1 = Gerente('Manoel', 1111111111, 1000, 123)
d1 = Diretor('Limeira', 0000000000, 2000, 1)

print(g1.autentica(123))
print(d1.get_nome())
#d1.autentica(123)