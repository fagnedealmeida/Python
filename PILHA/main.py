from pilha import Pilha

pilha = Pilha()

print(pilha.estaVazia())
pilha.imprimirPilha()

pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)
pilha.desempilhar()


pilha.imprimirPilha()

print(pilha.estaVazia())