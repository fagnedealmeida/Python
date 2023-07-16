#devemos inicializar duas variavéis vazias para guarda os valores digitados e fazendo as comparações.
cidade_final=""
distancia_final=0
while True:
#colocando a string para letra maíuscula, afim de atender a condição de parada do while true.
  cidade=input("Digite o nome da cidade da sua viagem: ").upper()
  if cidade=="FIM":
    break
#solicitando a distância da viagem e o valor da passagem.
  distancia=int(input("Digite a distância da viagem: "))
  passagem=float(input("Digite o valor da passagem: "))
#processamento da condição de valor limite e maior distância de viagem.
#caso atenda a condição, será atualizada a cidade e distância.
  if distancia>distancia_final and (passagem*2)<=300:
    cidade_final=cidade
    distancia_final=distancia

if cidade_final=="":
  print("SEM DESTINO")
else:
  print("%s" % cidade_final)
