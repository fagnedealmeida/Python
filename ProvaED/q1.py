# entrada em int para o ano
ano = int(input("Digite um ano: "))
string = str(ano)

#condição se é divisível por 4 e terminar em 00.
#uso da string para tratamento com dígitos finais.
if ano % 4 == 0  and string[2:]=="00":
  if ano % 400 == 0:
    print(ano, "é bissexto")
  else:
    print(ano, "não é bissexto")
else:
  if ano % 4==0 and string[2:]!= "00":
    print(ano, "é bissexto")
  else:
    print(ano, "não é bissexto")