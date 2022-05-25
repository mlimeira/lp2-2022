from conta import Conta


class ContaInvestimento(Conta):
    def __init__(self, numero, cliente, saldo, senha):
        super().__init__(numero, cliente, saldo, senha)

    def atualiza(self, taxa):
        valor = self._saldo * taxa
        self.depositar(valor)
        self.sacar(9.99)
        return valor
