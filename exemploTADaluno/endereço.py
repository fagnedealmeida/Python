class Endereço:
  def __init__ (self, rua, numero, bairro, cidade):
    self.rua = rua
    self.numero = numero
    self.bairro = bairro
    self.cidade = cidade

  def exibirEndereço(self):
    print("Endereço: Rua", self.rua,",", self.numero,",", self.bairro,",",self.cidae)
    