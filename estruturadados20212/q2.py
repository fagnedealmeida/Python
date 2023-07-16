#inserir valores dentro de uma lista vazia conforme as entradas
#lista vazia
lista = []
quantidade= int(input("digite a quantidade números: "))
#entrada como intevalo do range
for contador in range (0,quantidade):
  #os numeros da entrada a partir da repetição do for adicionados na lista vazia.
  numero= int(input("Entre com um número: "))
  lista.append(numero)
#exibir a lista em laço ou seja, cada elemento por vez
for i in range(0,quantidade):
  print(lista[i])
#exibir uma lista da forma inversa.
for i in range(quantidade-1,-1,-1):
  print(lista[i])