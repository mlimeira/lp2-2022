import abc


class Autenticavel(abc.ABC):
    @abc.abstractmethod
    def autentica(self, valor):
        pass