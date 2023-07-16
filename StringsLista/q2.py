#inserir uma data DD/MM/AAAA
#transformar o mês para escrita por extenso. usando split(/)
dia, mes, ano = input("Digite uma data: ").split("/")

#tratamento para as condições de cada mes.
if mes == "01":
  mes = "Janeiro"
if mes == "02":
  mes = "Fevereiro"
if mes == "03":
  mes = "Março"
if mes == "04":
  mes = "Abril"
if mes == "05":
  mes = "Maio"
if mes == "06":
  mes = "Junho"
if mes == "07":
  mes = "Julho"
if mes == "08":
  mes = "Agosto"
if mes == "09":
  mes = "Setembro"
if mes == "10":
  mes = "Outubro"
if mes == "11":
  mes = "Novembro"
if mes == "12":
  mes = "Dezembro"

print("Você nasceu em {} de {} de {}".format(dia, mes, ano))
