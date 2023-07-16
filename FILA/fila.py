class Fila:
  def __init__(self):
    self.fila = []

  def estaVazia(self):
    if (self.tamanho() == 0):
      return True
    else:
      return False
      
  #colocar sempre no final da fila.
  def enfileirar(self, dado):
    self.fila.append(dado)

  def imprimir(self):
    if (self.estaVazia()):
      print("Fila=[ ]")
    else:
      print("Fila=[ frente >>> ", end='')
      for e in self.fila:
        if (self.fila.index(e) == len(self.fila)-1):
          print(e, " ", sep='', end='' )
        else: 
          print(e, ", ", sep='', end='' )
      print("]")
      
#retirar o dado que esta na frente da fila(primeiro).
  def desenfileirar(self):
    if (not self.estaVazia()):
      self.fila.pop(0) #remove o primeiro O

  def tamanho(self):
    return len(self.fila)
    
#encontrar o primeiro da fila usando a posição[0]
  def primeiro(self):
    if not self.estaVazia():
      return self.fila[0]
    else:
      None
      
#encontrar o ultimo da fila atraves do len - 1  
  def ultimo(self):
    if not self.estaVazia():
      return self.fila[self.tamanho()-1]
    else:
      None
    
    