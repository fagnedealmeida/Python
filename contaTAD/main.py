from conta import Conta

c1 = Conta(15397, "fagne", 100.00)
c2 = Conta(2469, "iracy", 200.00)
c1.sacar(100.00)
c1.sacar(10)
print("#", c1.numero, " | Titular: ", c1.titular, "| R$ ", c1.saldo)

print("Titular: ",c1.titular)
print("Titular: ",c2.titular)
c1.depositar(10)
c1.exibirDado()
