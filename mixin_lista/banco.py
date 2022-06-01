class Banco:
    #A lista de contas pertence a cada objeto do tipo banco
    def __init__(self):
        self._contas = []
        self._caixa_geral = 0
    #Método para incluir as contas dentro do banco
    def incluir_conta(self, conta):
        self._contas.append(conta)
    def remover_conta(self, conta):
        self._contas.pop(conta)
    def listar_contas(self):
        caixa_temp = 0
        for c in self._contas:
            print(f'Extrato da conta {c.numero}')
            c.extrato.imprime()
            print('---------------------')
            print(f'Saldo final {c.saldo}')
            print('---------------------')
            caixa_temp += c.saldo
        self._caixa_geral = caixa_temp

    def imprime_caixa(self):
        print(f'Total de dinheiro no banco: {self._caixa_geral}')

    def atualizar_contas(self, taxa):
        total_atualizacoes = 0
        total_saldo = 0
        for c in self._contas:
           print(c)
           total_atualizacoes += c.atualiza(taxa)
           total_saldo += c.saldo
           print(c)
        print(f'Total das atualizações: {total_atualizacoes}')
        print(f'Total dos saldos: {total_saldo}')

