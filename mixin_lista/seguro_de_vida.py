from tributavel_mixin import TributavelMixin

class SeguroDeVida(TributavelMixin):
    def __init__(self, numero, valor, conta):
        self._numero = numero
        self._valor = valor
        self._conta = conta #Pode ter o titular tbm

    def valor_imposto(self):
        imposto = 0.05 * self._valor + 34
        self._conta.sacar(imposto)
        return imposto