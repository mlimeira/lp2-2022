from conta_corrente import ContaCorrente
from seguro_de_vida import SeguroDeVida
from manipulador_tributavel import ManipuladorTributavel

cc = ContaCorrente(1, 'Manoel', 1000, '123')
sg = SeguroDeVida(1, 1000, cc)

lista = [cc, sg]

mt = ManipuladorTributavel()
print(mt.calcular_impostos(lista))