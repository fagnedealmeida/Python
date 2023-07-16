leve = 3
media = 4
grave = 5
gravissima = 7
pontos = 0


for c in range (1,6):
  multa = input(f"Digite a gravidade da multa {c}:")
  multa.lower()

  if multa == "leve":
    pontos = pontos + 3
  elif multa == "media":
    pontos = pontos + 4
  elif multa == "grave":
    pontos = pontos + 5
  elif multa == "gravissima":
    pontos = pontos + 7

if pontos >= 21:
  print(f"Condutor atingiu o limite de pts carteira: {pontos} pontos, Carteira suspensa.")
else:
  print(f"Condutor com {pontos} pontos")