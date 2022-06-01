from tributavel_interface import TributavelInterface


class ManipuladorTributavel:
    def calcular_impostos(self, lista_tributaveis):
        total = 0
        for tr in lista_tributaveis:
            if isinstance(tr, TributavelInterface):
                total += tr.valor_imposto()
        return total