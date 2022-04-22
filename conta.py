from historico import Historico

class Conta:
  #Atributo privado de Classe
  _total_contas = 0

  @classmethod
  def get_total_contas(cls):
    return Conta._total_contas

  #Caracteristicas
  __slots__ = ['_numero', '_titular', '_saldo', '_senha','extrato']
  def __init__(self, numero, cliente, saldo, senha):
    self._senha = senha
    self._numero = numero
    self._titular = cliente
    self._saldo = saldo
    self.extrato = Historico()
    Conta._total_contas += 1

  def set_saldo(self, valor):
    self._saldo = valor

  def sacar(self, valor):
    if self._saldo >= valor:
      self._saldo = self._saldo - valor
      self.extrato.transacoes.append('Saque de {}'.format(valor))
    else:
      print("Saldo insuficiente!!!")

  def depositar(self, valor):
    self._saldo += valor
    self.extrato.transacoes.append('Depósito de {}'.format(valor))

  @property
  def saldo(self):
    return self._saldo

  def get_numero(self):
    return self._numero

#  @get_numero.setter
  def set_numero(self, numero):
    self._numero = numero

  def get_senha(self):
    return self._senha

  def altera_senha(self, nova_senha):
    self._senha = nova_senha