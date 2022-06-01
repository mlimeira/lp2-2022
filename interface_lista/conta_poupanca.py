from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, saldo, senha):
        super().__init__(numero, cliente, saldo, senha)

    def atualiza(self, taxa):
        valor = self._saldo * taxa * 3
        self.depositar(valor)
        return valor
