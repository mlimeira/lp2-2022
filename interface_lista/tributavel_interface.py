import abc


class TributavelInterface(abc.ABC):
    '''Interface'''
    @abc.abstractmethod
    def valor_imposto(self):
        '''Método da Interface'''
        pass