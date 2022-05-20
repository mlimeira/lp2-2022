from presidente import Presidente
from secretario import Secretario
from diretor import Diretor
#Não posso criar objetos a partir da classe Abstrata
#func = Funcionario('Manoel', 1111111111, 1000)
func = Diretor('Manoel', 1111111111, 1000, 123)
pres = Presidente('Limeira', 99999999999, 5000)
secr = Secretario('Júnior', 99999999999, 5000)

print(secr.bonificacao())