#percorrer uma string com range usando a função len()
nome = input('Digite um nome: ')
for i in range(len(nome)):
#imprimir cada caractere em linha separado, necessário colocar o print dentro do for. 
  print(nome[i])
#imprimir string de forma reversa. -1 indica sequencia de trás para frente.
for i in range(len(nome))[::-1]:
  print(nome[i])

