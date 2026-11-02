from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython


lista1 = MiLista(10)
lista2 = ListaPython()


# LEER UN NÚMERO ENTERO
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número entero válido.")


# LEER LOS DATOS DE UN PASAJERO
def leer_pasajero():
    numero = leer_entero("Número del pasajero: ")
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    edad = leer_entero("Edad: ")
    fecha_vuelo = input("Fecha del vuelo (AAAA-MM-DD): ")
    destino = input("Destino: ")
    asiento = input("Asiento: ")

    return Pasajero(
        numero, nombre, cedula, edad,
        fecha_vuelo, destino, asiento
    )


# CARGAR LOS PASAJEROS DE PRUEBA

def cargar_datos_prueba(lista):
    lista.añadir(Pasajero(1005, "Diana", "0923456789", 22,
                          "2026-11-15", "Quito", "12A"))

    lista.añadir(Pasajero(1002, "Ana", "0923456780", 28,
                          "2026-11-15", "Lima", "03C"))

    lista.añadir(Pasajero(1009, "Luis", "0923456781", 35,
                          "2026-11-20", "Bogotá", "18F"))

    lista.añadir(Pasajero(1004, "Beto", "0923456782", 16,
                          "2026-11-20", "Quito", "07B"))

    lista.añadir(Pasajero(1001, "Elena", "0923456783", 41,
                          "2026-11-22", "Lima", "01A"))

    print("Datos de prueba cargados.")


# MOSTRAR LAS OPCIONES
def mostrar_opciones(titulo, extras=False):
    print("\n" + "=" * 40)
    print(titulo)
    print("=" * 40)
    print("1. Añadir pasajero")
    print("2. Listar pasajeros")
    print("3. Insertar pasajero")
    print("4. Buscar pasajero")
    print("5. Búsqueda binaria")
    print("6. Modificar pasajero")
    print("7. Eliminar por posición")
    print("8. Eliminar por número")
    print("9. Ordenar ascendente")
    print("10. Ordenar descendente")
    print("11. Reversar lista")
    print("12. Copiar lista")
    print("13. Mostrar longitud")

    if extras:
        print("14. Filtrar por destino")
        print("15. Mostrar mayores de edad")

    print("C. Cargar datos de prueba")
    print("0. Volver al menú principal")


# MENÚ DE OPERACIONES
def menu_lista(lista, titulo, extras=False):
    while True:
        mostrar_opciones(titulo, extras)
        opcion = input("Seleccione una opción: ").strip().upper()

        if opcion == "1":
            pasajero = leer_pasajero()
            lista.añadir(pasajero)

        elif opcion == "2":
            lista.listar()

        elif opcion == "3":
            posicion = leer_entero("Posición donde insertar: ")
            pasajero = leer_pasajero()
            lista.insertar(posicion, pasajero)

        elif opcion == "4":
            numero = leer_entero("Número del pasajero que busca: ")
            pos = lista.buscar(numero)

            if pos != -1:
                print("Pasajero encontrado en la posición:", pos)
            else:
                print("El pasajero no existe.")

        elif opcion == "5":
            print("(Recuerda ordenar primero: opción 9)")
            numero = leer_entero("Número del pasajero que busca: ")
            pos = lista.buscar_binaria(numero)

            if pos != -1:
                print("Pasajero encontrado en la posición:", pos)
            else:
                print("El pasajero no existe.")

        elif opcion == "6":
            numero = leer_entero("Número del pasajero: ")
            destino = input("Nuevo destino: ")
            asiento = input("Nuevo asiento: ")
            lista.modificar(numero, destino, asiento)

        elif opcion == "7":
            posicion = leer_entero("Posición que desea eliminar: ")
            eliminado = lista.eliminar_por_posicion(posicion)

            if eliminado is not None:
                print("Pasajero eliminado:", eliminado)

        elif opcion == "8":
            numero = leer_entero("Número del pasajero que desea eliminar: ")
            resultado = lista.eliminar_por_valor(numero)

            if resultado:
                print("Pasajero eliminado correctamente.")
            else:
                print("No se encontró el pasajero.")

        elif opcion == "9":
            lista.ordenar_asc()
            print("Lista ordenada de forma ascendente.")
            lista.listar()

        elif opcion == "10":
            lista.ordenar_desc()
            print("Lista ordenada de forma descendente.")
            lista.listar()

        elif opcion == "11":
            lista.reversar()
            print("Lista reversada.")
            lista.listar()

        elif opcion == "12":
            copia = lista.copiar()
            print("Lista original:")
            lista.listar()
            print("Lista copiada:")
            copia.listar()

        elif opcion == "13":
            print("Cantidad de pasajeros:", lista.longitud())

        elif opcion == "14" and extras:
            destino = input("Ingrese el destino: ")
            pasajeros = lista.filtrar_por_destino(destino)

            if len(pasajeros) == 0:
                print("No hay pasajeros con ese destino.")
            else:
                for pasajero in pasajeros:
                    print(pasajero)

        elif opcion == "15" and extras:
            pasajeros = lista.mayores_de_edad()

            if len(pasajeros) == 0:
                print("No hay pasajeros mayores de edad.")
            else:
                for pasajero in pasajeros:
                    print(pasajero)

        elif opcion == "C":
            cargar_datos_prueba(lista)

        elif opcion == "0":
            break

        else:
            print("Opción no válida.")


# MENÚ PILA  (MiLista como PILA: LIFO, el último en entrar es el primero en salir)
#   La BASE es la posición 0 y el TOPE es la última posición ocupada.
#   Apilar y desapilar SIEMPRE se hacen por el final: así no hay corrimientos.
def menu_pila(lista):
    while True:
        print("\n" + "=" * 40)
        print("MENÚ - MI LISTA COMO PILA (LIFO)")
        print("=" * 40)
        print("1. Apilar pasajero (push)")
        print("2. Desapilar pasajero (pop)")
        print("3. Ver el tope (peek)")
        print("4. Mostrar la pila")
        print("5. ¿La pila está vacía?")
        print("6. Tamaño de la pila")
        print("C. Cargar datos de prueba")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip().upper()

        if opcion == "1":
            antes = lista.longitud()
            lista.añadir(leer_pasajero())
            if lista.longitud() > antes:
                print("Pasajero apilado.")

        elif opcion == "2":
            if lista.longitud() == 0:
                print("La pila está vacía: no hay nada que desapilar.")
            else:
                ultimo = lista.longitud() - 1               # el tope
                eliminado = lista.eliminar_por_posicion(ultimo)
                print("Pasajero desapilado:", eliminado)

        elif opcion == "3":
            if lista.longitud() == 0:
                print("La pila está vacía.")
            else:
                print("Tope de la pila:", lista.datos[lista.longitud() - 1])

        elif opcion == "4":
            if lista.longitud() == 0:
                print("La pila está vacía.")
            else:
                print("(posición 0 = base · última posición = tope)")
                lista.listar()

        elif opcion == "5":
            if lista.longitud() == 0:
                print("Sí, la pila está vacía.")
            else:
                print("No, la pila tiene elementos.")

        elif opcion == "6":
            print("Cantidad de pasajeros en la pila:", lista.longitud())

        elif opcion == "C":
            cargar_datos_prueba(lista)

        elif opcion == "0":
            break

        else:
            print("Opción no válida.")


# MENÚ COLA  (ListaPython como COLA: FIFO, el primero en entrar es el primero en salir)
#   El FRENTE es la posición 0 y el FINAL es la última posición.
#   Se encola por el final y se desencola por el frente.
def menu_cola(lista):
    while True:
        print("\n" + "=" * 40)
        print("MENÚ - LISTA PYTHON COMO COLA (FIFO)")
        print("=" * 40)
        print("1. Encolar pasajero (enqueue)")
        print("2. Desencolar pasajero (dequeue)")
        print("3. Ver el frente (front)")
        print("4. Mostrar la cola")
        print("5. ¿La cola está vacía?")
        print("6. Tamaño de la cola")
        print("C. Cargar datos de prueba")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip().upper()

        if opcion == "1":
            antes = lista.longitud()
            lista.añadir(leer_pasajero())
            if lista.longitud() > antes:
                print("Pasajero encolado.")

        elif opcion == "2":
            if lista.longitud() == 0:
                print("La cola está vacía: no hay nadie que atender.")
            else:
                atendido = lista.eliminar_por_posicion(0)   # el frente
                print("Pasajero atendido (sale de la cola):", atendido)

        elif opcion == "3":
            if lista.longitud() == 0:
                print("La cola está vacía.")
            else:
                print("Frente de la cola:", lista.pasajeros[0])

        elif opcion == "4":
            if lista.longitud() == 0:
                print("La cola está vacía.")
            else:
                print("(posición 0 = frente · última posición = final)")
                lista.listar()

        elif opcion == "5":
            if lista.longitud() == 0:
                print("Sí, la cola está vacía.")
            else:
                print("No, la cola tiene elementos.")

        elif opcion == "6":
            print("Cantidad de pasajeros en la cola:", lista.longitud())

        elif opcion == "C":
            cargar_datos_prueba(lista)

        elif opcion == "0":
            break

        else:
            print("Opción no válida.")


# MENÚ PRINCIPAL
def main():
    while True:
        print("\n========== SISTEMA DE PASAJEROS ==========")
        print("1. MiLista como PILA (LIFO)")
        print("2. ListaPython como COLA (FIFO)")
        print("3. MiLista: menú completo de operaciones")
        print("4. ListaPython: menú completo de operaciones")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_pila(lista1)

        elif opcion == "2":
            menu_cola(lista2)

        elif opcion == "3":
            menu_lista(lista1, "MENÚ - MI LISTA")

        elif opcion == "4":
            menu_lista(lista2, "MENÚ - LISTA PYTHON", True)

        elif opcion == "5":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()