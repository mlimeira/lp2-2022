from conta_corrente import ContaCorrente
from banco import Banco
from tributavel_interface import TributavelInterface
from seguro_de_vida import SeguroDeVida
from manipulador_tributavel import ManipuladorTributavel

cc = ContaCorrente(1, 'Manoel', 1000, '123')
sg = SeguroDeVida(1, 1000, cc)

lista = [cc, sg]

bb = Banco()
bb.incluir_produto(cc)
bb.incluir_produto(sg)

mt = ManipuladorTributavel()
#print(mt.calcular_impostos(lista))
TributavelInterface.register(ContaCorrente)
TributavelInterface.register(SeguroDeVida)

print(bb.calcular_imposto_banco(mt))