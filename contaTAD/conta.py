class Conta:
#construtor em python __init__
#pode-se usar o construtor preenchido colocando o valor junto com o argumento, necessário usar para todos
  def __init__(self, numero=0, titular="DEFAULT", saldo=0.00):
    #self é o memso que this em java
    self.numero = numero
    self.titular = titular
    self.saldo = saldo

  def exibirDado(self):
    print("#", self.numero, " | Titular: ", self.titular, "| R$ ", self.saldo)

  def sacar(self, quantia):
    if (quantia > 0 and quantia <= self.saldo):
      self.saldo = self.saldo - quantia

  def depositar(self, quantia):
    if (quantia > 0):
      self.saldo = self.saldo + quantia
    