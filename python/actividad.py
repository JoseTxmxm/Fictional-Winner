#Prueba de código de actividad 5

nombre = input("Ingrese su nombre: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su telefono: ")

while not nombre.isalpha() or not direccion or not telefono.isdigit():
    print("¡Error! ingrese la información válida")

    nombre = input("Ingrese su nombre: ")
    direccion = input("Ingrese su dirección: ")
    telefono = input("Ingrese su telefono: ")
