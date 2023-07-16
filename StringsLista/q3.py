#inserir nome e imprimir em forma de escada. 
nome = input()
#percorrer todo o tamanho do nome
for i in range(0,len(nome)+1):
#a cada laço do for imprimi uma nova letra pelos índices da string.
  print(nome[:i])
