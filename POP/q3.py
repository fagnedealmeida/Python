A, B, C= input().split(" ")
D, E, F= input().split(" ")

A = int(A)
B = int(B)
C = float(C)
D = int(D)
E = int(E)
F = float(F)

V1 = B*C
V2 = E*F

TOTAL = V1+V2

print(f"VALOR A PAGAR: R$ {TOTAL:.2f}")
