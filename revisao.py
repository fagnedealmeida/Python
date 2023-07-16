vendedor = str(input())
salario = float(input())
mes = float(input())

comissao = mes * 0.15
salario_final = comissao + salario
print("TOTAL =  R$ %.2f" % salario_final)

