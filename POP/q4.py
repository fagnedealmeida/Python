valor = float(input()) * 100

moedas = [100,50,25,10,5,1]
cedulas = [10000,5000,2000,100,200]

print("NOTAS: ")

for  ced in cedulas:
  qtd_cedulas = valor // ced
  print(f"{qtd_cedulas:.0f} nota(s) de R$ {(ced/100):.2f}")
  valor -= ced*qtd_cedulas

print("NOTAS:")

for md in moedas:
  qtd_moedas = valor // md
  