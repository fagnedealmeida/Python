salario = float(input())

# código que faz o calculo do aumento salario baseado na 
# porcentagem descrita em relacao ao valor do salario
if salario > 0 and salario <= 400.00:
    percentual = 15
    
elif salario > 400.01 and salario <= 800.00:
    percentual = 12
    
elif salario > 800.01 and salario <= 1200.00:
    percentual = 10
    
elif salario > 1200.01 and salario <= 2000.00:
    percentual = 7
    
else:
    percentual = 4
    
  
ajuste = salario*(percentual/100)
nsalario = ajuste + salario

print(f"Novo salario: {nsalario:.2f}")
print(f"Reajuste ganho: {ajuste:.2f}")
print(f"Em percentual: {percentual} %")
