from funcionario import Funcionario

class ControleBonificacao:
    def __init__(self):
        self._total_bon = 0

    def registra(self, f):
        #Primeira forma
        #if(hasattr(funcionario, 'bonificacao')):
        #Segunda forma
        #if(isinstance(f, Funcionario)):
        #    self._total_bon += f.bonificacao()
        #else:
        #    print('A referencia não possui o recurso de bonificação')
        #Terceira forma
        try:
            self._total_bon += f.bonificacao()
        except AttributeError as atte:
            print('A referencia não possui o recurso de bonificação')

    def get_total_bon(self):
        return self._total_bon