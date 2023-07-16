#tabuada de multiplicação
#usando a entrada dentro do for para fazer o cálculo 
# o range para o intervalo da tabuada
# com o print dentro do for para repetir a operação
#usando .format para deixar o print melhor.
numero = int(input("Digite um número:"))
for contador in range(1,11):
  print("{} x {} = {}".format(numero,contador,numero*contador))


# poderia ter sido feita com while
contador = 1
while contador <= 10:
  # estrutura do cálculo da tabuada