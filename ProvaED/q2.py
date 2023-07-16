def palindromo():
  palavra = input()
  inverter = palavra[::-1]
  if palavra == inverter:
    print("A palavra é um Palíndromo !")
  else:
    print ("A palavra não é um Palíndromo !")

nome = palindromo()


#receber a string deseja
nome = input()
#reverter a posição da string 
nome2 = nome[::-1]
# comparar com a string de entrada
if nome == nome2:
  print("check !")
else:
  print("fail !")
#printar resultado.
print(nome2)