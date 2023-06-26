def mostrar_menu():
    print(" | MENU | ")
    print("1. Agregar Contacto")
    print("2. Actualizar Contacto")
    print("3. Eliminar Contacto")
    print("4. Salir del menú")


def añadir_contacto():
    nombre_contacto = input("Ingrese nombre de contacto: ")
    numero_contacto = input("Ingrese número de teléfono: ")
    with open("archivo.txt", "a") as archivo:
        archivo.write(
            "Nombre: " + nombre_contacto + " Numero: " + numero_contacto + "\n"
        )
    print("Contacto agregado con éxito\n")


def actualizar_contacto():
    nombre_contacto = input("Ingrese el nombre a actualizar: ")
    numero_nuevo = input("Ingrese el nuevo número: ")
    actualizadas = []
    with open("archivo.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(" ")
            if datos[0] == "Nombre:" and datos[1] == nombre_contacto:
                linea = "Nombre: " + nombre_contacto + " Numero: " + numero_nuevo + "\n"
            actualizadas.append(linea)
    with open("archivo.txt", "w") as archivo:
        archivo.writelines(actualizadas)
    if any(actualizadas):
        print("Contacto actualizado")
    else:
        print("No se encontró en la agenda\n")


def eliminar_contacto():
    nombre_contacto = input("Ingrese el nombre a eliminar: ")
    eliminadas = []
    with open("archivo.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(" ")
            if datos[0] == "Nombre:" and datos[1] != nombre_contacto:
                eliminadas.append(linea)
    with open("archivo.txt", "w") as archivo:
        archivo.writelines(eliminadas)
    if any(eliminadas):
        print("Contacto eliminado")
    else:
        print("No se encontró en la agenda\n")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una de estas opciones: ")
        if opcion == "1":
            añadir_contacto()
        elif opcion == "2":
            actualizar_contacto()
        elif opcion == "3":
            eliminar_contacto()
            break
        else:
            print("Opción inválida. Selecciona una opción válida.")
        print()


main()
