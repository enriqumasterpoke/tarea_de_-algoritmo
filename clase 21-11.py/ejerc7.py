"""
Utilizando rangos,suma el valor de todos los numeros pares desde el 2(inclusive) hasta el 100 (inclusive).
"""
suma=0
for i in range(0,101,2):
    suma+=i
print(f"la suma es:{suma}")