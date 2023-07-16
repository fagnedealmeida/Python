class Calculadora:
  def __init__(self, fabricante, preço, modelo):
    self.fabricante = fabricante
    self.preço = preço
    self.modelo = modelo

  def setFabricante(self, novoFabricante):
    self.fabricante = novoFabricante

  def setPreço(self,novoPreço):
    self.preço = novoPreço

  def setModelo(self,novoModelo):
    self.modelo = novoModelo

  def somar(self, a, b):
    soma = a + b
    print(soma)

  def diminuir(self, a, b):
    subtrair = a - b
    print(subtrair)

  def multiplicar(self, a, b):
    multiplicacao = a * b
    print(multiplicacao)
    
  def dividir(self, a, b):
    if a != 0 and b != 0:
      divisao = a/b
      print(divisao)
    else:
      print("Divisão por zero não pode ser feita.")

  def exibirDados(self):
    print("Calculdora fabricada pela:", self.fabricante, "\nCom o preço de: R$", self.preço,"\nDo modelo:", self.modelo)
    