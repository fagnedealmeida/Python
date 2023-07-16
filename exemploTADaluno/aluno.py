
class Aluno:
  def __init__(self, nome, matricula, nota1, nota2,endereço):
    self.nome = nome 
    self.matricula = matricula
    self.nota1 = nota1
    self.nota2 = nota2
#inserindo variaveis de outra classe em uma classe.
    self.endereço = endereço

  def calcularMedia(self):
    media = (self.nota1+self.nota2) / 2
    return media

  def exibirDados(self):
    print("Matricula: ", self.matricula, "\nNome: ", self.nome, "\nNota 1: ", self.nota1, "\nNota 2: ", self.nota2)
    self.endereço.exibirEndereço()