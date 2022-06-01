from conta import Conta


class Banco:
    #A lista de contas pertence a cada objeto do tipo banco
    def __init__(self):
        self._produtos = []
        self._caixa_geral = 0
    #Método para incluir as produto dentro do banco
    def incluir_produto(self, produto):
        self._produtos.append(produto)
    def remover_produto(self, produto):
        self._produtos.pop(produto)
    def listar_contas(self):
        caixa_temp = 0
        for c in self._produtos:
            if isinstance(c, Conta):
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
        for c in self._produtos:
            if isinstance(c, Conta):
               print(c)
               total_atualizacoes += c.atualiza(taxa)
               total_saldo += c.saldo
               print(c)
            print(f'Total das atualizações: {total_atualizacoes}')
            print(f'Total dos saldos: {total_saldo}')

    def calcular_imposto_banco(self, mt):
        return mt.calcular_impostos(self._produtos)
