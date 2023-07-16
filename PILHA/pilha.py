class Pilha:
  #construtor
  def __init__(self):
  #deve criar com o tipo lista[]
    self.elementos = []

#verificar se a pilha tem dados  ou não.  
  def estaVazia(self):
    if (len(self.elementos)  == 0):
      return True
    else:
      return False
      
#adicionar elementos na pilha no topo da pilha, o ultimo (topo) elemento para ser inserido na direita, usando o append.
  def empilhar(self, dado):
    self.elementos.append(dado)

#exibição da pilha de acordo com a quantidade de elementos
#e indicação do último (topo) da pilha
  def imprimirPilha(self):
    if (self.estaVazia()):
      print("Pilha = []")
#com a lista contendo dados a exibição devera ficar 
    else: 
#o uso do end='' para o print não pular linha para futuros prints.
      print("Pilha = [", end='')
#for para verificar se cada elemento da lista é o último
      for e in self.elementos:
        if (self.elementos.index(e) == len(self.elementos)-1):
#sendo o último não utilizar virgula após o elemento
          print(e, " ", sep='', end='')
        else:
#não sendo o último utilizar virgula após o elemento
          print(e, ", ", sep='', end='')
#ao fim do for da lista colocar a sinalização do topo
      print("<-- topo]")

#para retirar elementos da pilha se tiver dados
  def desempilhar(self):
    if ( not self.estaVazia()):
      self.elementos.pop()
      
#para descobrir o topo da lista, retornar o len-1 da pilha
  def consultaTopo(self):
    if (not self.estaVazia()):
      return self.elementos[len(self.elementos)-1]
    else:
      return None
    
#usando a função len encontra o tamanha da pilha
  def tamanho(self):
    return len(self.elementos)
        