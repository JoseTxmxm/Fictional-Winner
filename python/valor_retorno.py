# Valores de retorno
# Ask user for name
name = input("What's your name? :").strip().title()# Operaciones en una sola línea para código más limpio, conciso

print("Estamos en la líena 4, hello,") # Print("hello,", name)
print(name)

# Operadores + y coma, argumentos de función múltiple
print("Estamos en la línea 8, hello,", name)
print("EStamos en la línea 9, hello," + name)

# Escaping Characteres
# Say hello to user
print('Estamos en la línea 14, hello, "friend"') # Ejemplo 1 de uso de comillas dobles dentro de comillas simples en el código
print("Estamos en la línea 15, hello, \"friend\"") # Ejemplo 2 de uso de comillas dobles dentro de comillas dobles en el código

# F-String
print("Estamos en la línea 18, hello, {name}")
print(f"Estamos en la línea 19, hello, {name}")

"""
Métodos de cadenas
name = name.strip() = Remove whitespace from str
name = name.capitalize() = Agrega una mayúscula a la primera letra del primer string, nombre, etc.
name = name.title() = Agega maúsculas a las primera palabras a más de dos strings
name = name.strip.().title.() = Mejora la estética del código
name = input("What's your name? :").strip().title() Operaciones en una sola líena para código más conciso y limpio
"""
# Parámetro nombrado end
print("Estamos en la línea 30 probando el parámetro especial end", end="???\n") # Este parámtetro nombrado lleva un salto de línea por default \n
print("Estamos en la línea 31 probando el parámetro especial end", end="espacio\n") # Este parámtetro nombrado lleva un salto de línea por default \n

# Parámetro nombrado sep
print("Estamos en la línea 34 probando el parámetro especial sep:", name, sep="
print("Estamos en al línea 35 probando el parámetro especial sep: ", name, sep="???")

# Split user's name into first name and last name
first, last = name.split(" ")
print(f"Estamos en la línea 39 probando el método de cadena split, {first}")
print(f"Estamos en la línea 40 probando el método de cadena split, {last}")
