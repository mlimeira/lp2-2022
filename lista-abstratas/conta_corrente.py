from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, saldo, senha):
        super().__init__(numero, cliente, saldo, senha)

    def atualiza(self, taxa):
        #Atualizando com o método da superclasse
        #super().atualiza(taxa * 2)
        valor = self._saldo * taxa * 2
        self.depositar(valor)
        self.sacar(0.1)
        return valor
