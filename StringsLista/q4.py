#uso do while true, pois o final do programa será com comando do usuário.
while True:
#menu do programa com informações a serem passadas ao usuário sobre o programa.
  print("========MENU========")
  print("1- Entrar com dados \nde uma cadeia de DNA. \n2- Sair do Programa.")
  print("====================")
  opcao=int(input("Digite o nº da opção\ndesejada:"))
#condição de parada do programa
  if (opcao==2):
    print("Programa encerrado !")
    break
 
  if (opcao==1):
#criando string vazia para ser preenchida conforma o programa.

    lista=""
    cadeia= input("Digite a sequência do\nDNA:")
#tratamento para as entradas em minísculo transformando em maísculo atendendo as condições.
    dna = cadeia.upper()
 
#for sobre o input para testar as condições
    for i in dna:
#condições de verificação de uma string e preenchimento de outra string vazia através da concatenação +=.
      if (i == "A"):
        lista+="U"
      elif (i =="T"):
        lista+="A"
      elif (i =="C"):
        lista+="G"
      elif (i =="G"):
        lista+="C"

#print após o fim do for mostrando os resultados.      
    print("Cadeia de RNA: ",lista) 

  
