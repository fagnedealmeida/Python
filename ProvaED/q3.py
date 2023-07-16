def rendimento (idade, valor):
  tempo = (65-idade) * 12
  mes = valor * 0.10
  capital_final = valor + mes * tempo
  return capital_final


Nome = str(input("Digite seu nome: "))
Idade = int(input("Digite sua idade: "))
Deposito = float(input("Digite a quantia para depósito: "))
Poupanca = rendimento(Idade,Deposito)

print(f"{Nome}, com seu depósito de R$ {Deposito} ao aposentar-se terá um rendimento total de R$ {Poupanca}")
