#manipular string - trocando a letra a por #
frase= str(input('Digite uma frase:'))
nova = frase.replace("A", "#")
print(nova)

#uma nova forma de resolver.
frase=input("Digite uma frase: ")
lista=[]
#percorrer a frase digitada pelo indices e adicionar em uma lista.
for i in range(len(frase)):
  lista.append(frase[i])
#condição de substituição das letras
  if frase[i]=='a' or frase[i]=='A':
    lista[i]='#'
#print para imprimir a lista na mesma linha com end.
print(lista[i], end="")