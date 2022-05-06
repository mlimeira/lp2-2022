class Emprestimo:
    _total_emprestimos = 0

    def __init__(self, valor, parcelas, juros, conta):
        self._valor = valor
        self._parcelas = parcelas
        self._juros = juros
        self._conta = conta
        self._montante = self._valor + (self._valor*juros)
        self._valor_parcela = self._montante/self._parcelas
        conta.depositar(self._valor)
        Emprestimo._total_emprestimos += 1

    @classmethod
    def total_emprestimos(cls):
        return cls._total_emprestimos

    def pagar_parcela(self):
        self._conta.sacar(self._valor_parcela)
        self._parcelas -= 1
        self._montante -= self._valor_parcela
        self.status()

    def status(self):
        print('---Situação do Emprestimo---')
        print(f'Faltam {self._parcelas} parcelas')
        print(f'Falta pagar {self._montante}')
        print(f'Seu saldo é de: {self._conta.saldo}')
        print('------------------------------')

