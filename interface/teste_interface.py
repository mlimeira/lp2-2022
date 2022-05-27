from diretor import Diretor
from gerente import Gerente
from autenticavel import AutenticavelInterface
from sistema_interno import SistemaInterno

g1 = Gerente('Manoel', 1111111111, 1000, 123)
d1 = Diretor('Limeira', 0000000000, 2000, 1, 123)

#print(g1.autentica(123))
#print(d1.get_nome())
#d1.autentica(123)

sistema = SistemaInterno()
sistema.login(g1, 123)

#Diretor não era autenticavel
#Vamos registrar como um autenticavel pelo método register
AutenticavelInterface.register(Diretor)
sistema.login(d1, 123)
d1.teste()