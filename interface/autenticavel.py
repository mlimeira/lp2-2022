import abc


class AutenticavelInterface(abc.ABC):
    """
    Esta classe define os objetos autenticaveis que devem
    implementar o método autentica.
    """
    @abc.abstractmethod
    def autentica(self, valor):
        """
        Esse método retorna True caso o valor seja igual a senha
        e False caso contrário.
        """
        pass
