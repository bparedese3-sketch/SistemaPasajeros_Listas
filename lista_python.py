from bisect import bisect_left


class ListaPython:

    def __init__(self):
        self.pasajeros = []

    # AÑADIR
    def añadir(self, pasajero):
        if self.buscar(pasajero.numero) != -1:
            print("El número de pasajero ya existe.")
            return

        self.pasajeros.append(pasajero)

    # LISTAR
    def listar(self):
        if len(self.pasajeros) == 0:
            print("La lista está vacía.")
        else:
            for i, pasajero in enumerate(self.pasajeros):
                print(f"[{i}] {pasajero}")

    # INSERTAR
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print("Posición no válida.")
            return

        if self.buscar(pasajero.numero) != -1:
            print("El número de pasajero ya existe.")
            return

        self.pasajeros.insert(posicion, pasajero)

    # BUSCAR
    def buscar(self, numero):
        posiciones = [
            i for i, p in enumerate(self.pasajeros)
            if p.numero == numero
        ]

        if len(posiciones) > 0:
            return posiciones[0]

        return -1

    # BÚSQUEDA BINARIA
    def buscar_binaria(self, numero):
        numeros = [p.numero for p in self.pasajeros]

        pos = bisect_left(numeros, numero)

        if pos < len(numeros) and numeros[pos] == numero:
            return pos

        return -1

    # MODIFICAR
    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)

        if pos == -1:
            print("El pasajero no existe.")
            return

        self.pasajeros[pos].destino = nuevo_destino
        self.pasajeros[pos].asiento = nuevo_asiento

    # ELIMINAR POR POSICIÓN
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("Posición no válida.")
            return None

        return self.pasajeros.pop(posicion)

    # ELIMINAR POR VALOR
    def eliminar_por_valor(self, numero):
        cantidad_anterior = len(self.pasajeros)

        self.pasajeros = [
            p for p in self.pasajeros if p.numero != numero
        ]

        return len(self.pasajeros) < cantidad_anterior

    # ORDENAR ASCENDENTE
    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    # ORDENAR DESCENDENTE
    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    # REVERSAR
    def reversar(self):
        self.pasajeros.reverse()

    # COPIAR
    def copiar(self):
        nueva = ListaPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    # LONGITUD
    def longitud(self):
        return len(self.pasajeros)

    # FILTRAR POR DESTINO
    def filtrar_por_destino(self, destino):
        return [
            p for p in self.pasajeros if p.destino == destino
        ]

    # MAYORES DE EDAD
    def mayores_de_edad(self):
        return [
            p for p in self.pasajeros if p.es_mayor_de_edad()
        ]