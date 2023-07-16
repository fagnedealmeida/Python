class Pessoa:
  def __init__(self,nome, rg):
    self.nome=nome
    self.rg=rg

  def __repr__(self):
    saida="Nome " + str(self.nome) + " - " + "RG: " + str(self.rg)
    return saida