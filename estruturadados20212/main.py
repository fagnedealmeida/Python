#quantidade de números e os numeros definidos pelas entradas
#entrada que define a quantidade de numeros a serem inseridos.
quantidade = int(input('Quantidade de números a serem informados: '))
#lista para adicionar os números
lista=[]
#o laço para serem inseridos os números com o range da variável quantidade.
for contador in range(0,quantidade):
  numeros = int(input('Digite um número: '))
  lista.append(numeros)
#condições para definir os maiores, menor e médias dos valores, sendo feita com o laço testando os indices da lista.
maior = menor = lista[0]
soma=0
for i in range(0,quantidade):
  soma = soma + numeros
  if lista[i]>maior:
    maior=lista[i]
  if lista[i]<menor:
    menor=lista[i]
media = soma/quantidade
print("O maior número digitado é: {}".format(maior))
print("O menor número digitado é: {}".format(menor))
print("A média dos números digitados é: {}".format(media))