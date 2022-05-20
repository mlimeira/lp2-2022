import abc


class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @abc.abstractmethod
    def bonificacao(self):
        pass