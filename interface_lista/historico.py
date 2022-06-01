class Historico:
  def __init__(self):
    self.transacoes = []

  def imprime(self):
    for tr in self.transacoes:
      print(tr)