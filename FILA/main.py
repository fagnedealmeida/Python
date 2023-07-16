from fila import Fila
from pessoa import Pessoa

#criação da fila vazia
fila = Fila()
fila.imprimir()
p1 = Pessoa("iracy morais", "017929")
p2 = Pessoa("fagne de almeida", "018033")
print(fila.estaVazia())

fila.enfileirar("Jose")
fila.enfileirar("Fagne")
fila.enfileirar("Iracy")
fila.enfileirar("Maria")

fila.imprimir()
print(fila.estaVazia())


fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.imprimir()
print(fila.estaVazia())
fila.enfileirar(p1)
fila.enfileirar(p2)
fila.imprimir()
