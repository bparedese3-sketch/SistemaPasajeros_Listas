class MiLista:
    # El constructor: prepara un arreglo con espacios vacíos (None)
    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad  # los "cajones"
        self.capacidad = capacidad       # cuántos cajones hay en total
        self.cantidad = 0                # cuántos están ocupados

    # AÑADIR: funciona como .append (no permite números repetidos)
    def añadir(self, pasajero):
        if self.cantidad == self.capacidad:
            print("No hay espacio para añadir más elementos.")
            return
        if self.buscar(pasajero.numero) != -1:
            print("El número de pasajero ya existe.")
            return
        self.datos[self.cantidad] = pasajero   # primer cajón libre
        self.cantidad += 1

    # INSERTAR: corre los demás a la derecha (de atrás hacia adelante)
    def insertar(self, posicion, pasajero):
        i = self.cantidad
        if self.cantidad == self.capacidad:
            print("No hay espacio para insertar más elementos.")
            return
        if posicion < 0 or posicion > self.cantidad:
            print("Posición no válida.")
            return
        if self.buscar(pasajero.numero) != -1:
            print("El número de pasajero ya existe.")
            return
        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i -= 1
        self.datos[posicion] = pasajero
        self.cantidad += 1

    # BUSCAR: revisa uno por uno. Retorna la posición o -1
    # (se compara el NÚMERO del pasajero, no el objeto completo)
    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    # BUSCAR BINARIA: parte la lista por la mitad. ¡Debe estar ORDENADA por número!
    def buscar_binaria(self, numero):
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio].numero == numero:
                return medio
            elif self.datos[medio].numero < numero:
                izq = medio + 1
            else:
                der = medio - 1
        return -1

    # MODIFICAR: busca por número y cambia destino y asiento
    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            print("El pasajero no existe.")
            return
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento

    # ELIMINAR POR POSICIÓN: corre a la izquierda y retorna el eliminado
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print("Posición no válida.")
            return None
        valor = self.datos[posicion]
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return valor

    # ELIMINAR POR VALOR: busca la posición y reutiliza eliminar_por_posicion
    # Retorna True si eliminó, False si no existía (igual que ListaPython)
    def eliminar_por_valor(self, numero):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.eliminar_por_posicion(pos)
        return True

    # ORDENAR ASC (burbuja) por número
    def ordenar_asc(self):
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].numero > self.datos[i + 1].numero:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux

    # ORDENAR DESC (burbuja): igual, pero con "<"
    def ordenar_desc(self):
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].numero < self.datos[i + 1].numero:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux

    # REVERSAR: extremos hacia el centro
    def reversar(self):
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq += 1
            der -= 1

    # COPIAR: crea otra MiLista con los mismos pasajeros
    def copiar(self):
        nueva = MiLista(self.capacidad)
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva

    # LONGITUD
    def longitud(self):
        return self.cantidad

    # LISTAR
    def listar(self):
        if self.cantidad == 0:
            print("La lista está vacía.")
            return
        for i in range(self.cantidad):
            print(f"[{i}] {self.datos[i]}")


# Las pruebas van SOLO aquí: así no se ejecutan cuando main.py importa este archivo
if __name__ == "__main__":
    from pasajero import Pasajero
    mi = MiLista(5)
    mi.añadir(Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito", "12A"))
    mi.añadir(Pasajero(1002, "Ana", "0923456780", 28, "2026-11-15", "Lima", "03C"))
    mi.listar()
    print(mi.buscar(1002))