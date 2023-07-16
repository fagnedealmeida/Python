from aluno import Aluno
from endereço import Endereço

#função para definir o aluno com maior nota, atraves da lista de alunos criada.
def maiorNota(lista):
#variaveis contadoras de maior nota e posição na lista.
  maior=lista[0].nota1
  pos=0
#for para testar na lista as maiores notas, especificando o atributo NOTA1
  for i in range(len(lista)):
    if lista[i].nota1 > maior:
      maior=lista[i].nota1
      pos=i
  return lista[pos]

#função para definir o aluno com maior média, pela lista de alunos.
def maiorMedia(lista):
  maior = lista[0].calcularMedia()
  pos = 0
  for i in range(len(lista)):
    if lista[i].calcularMedia() > maior:
      maior = lista[i].calcularMedia()
      pos = i
  return lista[pos]

  
#variavel vazia para ser preenchida durante o for.
listaAlunos = []

#for para inserir dados de mais alunos:
for i in range(3):
  
#criando variaveis de entrada para os atributos da classe Aluno
  Nome = input("Nome do aluno: ")
  Matricula = input("Matrícula do aluno: ")
  Nota1 = float(input("Primeira nota: "))
  Nota2 = float(input("Segunda nota: "))
  endereço = input("Rua: ")
  num = input("Numero: ")
  bairro = input("Bairro: ")
  cidade = input("Cidade: ")
#utilizando outra classe "endereço" dentro de outra classe 
  end = Endereço(endereço, num, bairro, cidade)
#criando o objeto Aluno c1 e atribuindo as variaveis existentes ao aluno.
  c1 = Aluno(Nome, Matricula, Nota1, Nota2,end)
  
#adicionando os dados de cada objeto (c1) na lista.
  listaAlunos.append(c1)

#for para imprimir os dados de cada aluno pela lista de alunos criada.
for i in range(3):
  listaAlunos[i].exibirDados()
#calcula a media e exibir junto com os dados
  print("Média: ", listaAlunos[i].calcularMedia())
  if listaAlunos[i].calcularMedia()>= 7:
    print("Aprovado")
  
#mostrar o aluno com maior nota 1, usando a função.
AlunoMaior = maiorNota(listaAlunos)
AlunoMaior.exibirDados()

#mostrar o aluno com maior média, usando função.
AlunoMedia = maiorMedia(listaAlunos)
AlunoMedia.exibirDados()