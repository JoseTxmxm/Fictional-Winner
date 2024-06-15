# calculadora en python, ejemplo 1
print("Ejemplo 1, x + y")
x = (int(input("Escriba un número para x:")))
y = (int(input("Escriba un número para y:")))

print("El resultado es:", x + y)
print("")

# Ejemplo 2, una sola línea de código
print("Ejemplo 2, int + int")
print(int(input("Escriba un número: ")) + (int(input("Escriba un número: "))))
print("")

# Ejemplo 3, redondeo de valores de coma flotante a valores mas cercanos, round
print("Ejemplo 3, round a + b")
a = float(input("Escriba un número para a: "))
b = float(input("Escriba un número para b: "))
# round
z = round(a + b)
print("El resultado es:", z)
print("")

# Ejemplo 4, formato numérico separador con comas para miles
print("Ejemplo 4, formato númerico para números mayores a 1000")
print(f"{z:,}")  # formato numérico para redondeo de miles con comas
print("")

# Ejemplo 5, division, redondeo de decimales
print("Ejemplo 5, redondeo con la función round, división c / d")
c = float(input("Escriba un número para c: "))
d = float(input("Escriba un número para d: "))
# round
q = round(c / d, 2)
print(q)
print("")
# Redondeo con cadena de formato 'f'
print("Redondeo de división d / c con cadena de formato \"f\"")
j = d / c
print(f"{j:.2f}")
print("")
