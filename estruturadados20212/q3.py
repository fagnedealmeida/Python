#soma de ímpares de um intervalo
#usa-se uma variável contadora para a soma
#for com intervalo determinado
#a condição IF para separar os ímpares dentro do for.
soma = 0
for c in range(1,501):
  if c % 2 != 0:
    soma = soma + c
print(soma)
