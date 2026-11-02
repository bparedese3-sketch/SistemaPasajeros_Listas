#EJERCICOS COLA-FIFOS
#ejercicio1
from collections import deque

cola = deque()

while True:
    print("\n1.Llega cliente 2.Llega cliente VIP 3.Atender 4.Ver frente 5.Ver toda la cola 6.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        cola.append(nom)                      # normal: entra al FINAL
        print(f"{nom} entró a la fila. {len(cola)} clientes en espera.")

    elif op == "2":
        nom = input("Nombre (VIP): ")
        cola.appendleft(nom)                  # VIP: entra al FRENTE
        print(f"{nom} (VIP) pasa al frente. {len(cola)} clientes en espera.")

    elif op == "3":
        if not cola:
            print("No hay clientes")
        else:
            atendido = cola.popleft()
            print(f"Atendiendo a: {atendido}. Quedan {len(cola)}.")

    elif op == "4":
        if not cola:
            print("Fila vacía")
        else:
            print(f"Siguiente: {cola[0]}")

    elif op == "5":
        if not cola:
            print("(vacía)")
        else:
            for i, c in enumerate(cola):
                marca = " ← siguiente" if i == 0 else ""
                print(f"  {i+1}. {c}{marca}")

    elif op == "6":
        break

    else:
        print("Opción no válida")





#ejercicio2
from collections import deque

def procesar_impresora(trabajos):
    cola = deque(trabajos)
    tiempo_total = 0

    while cola:
        print("\nTrabajos pendientes:")
        for trabajo in cola:
            print(trabajo[0])

        opcion = input("\n¿Desea cancelar algún trabajo? (si/no): ")

        if opcion.lower() == "si":
            nombre = input("Ingrese el nombre del documento: ")

            encontrado = False

            for trabajo in cola:
                if trabajo[0] == nombre:
                    cola.remove(trabajo)
                    encontrado = True
                    print(f"{nombre} fue cancelado.")
                    break

            if not encontrado:
                print("El documento no existe en la cola.")

        if cola:
            nombre, paginas = cola.popleft()
            tiempo = paginas * 2
            tiempo_total += tiempo

            print(f"Imprimiendo {nombre}: {paginas} páginas → {tiempo}s "
                  f"(acumulado {tiempo_total}s)")

    return tiempo_total


# --- Uso ---

trabajos = [
    ("Contrato.pdf", 5),
    ("Recibo.pdf", 2),
    ("Manual.pdf", 10),
]

total = procesar_impresora(trabajos)
print(f"\nTiempo total: {total}s")




#ejercicio3
from collections import deque

class ColaPrioridad:
    def __init__(self, niveles=3):
        # Un deque por cada nivel
        self.niveles = niveles
        self.colas = [deque() for _ in range(niveles + 1)]

    def encolar(self, valor, prioridad):
        if not 0 < prioridad <= self.niveles:
            raise ValueError(f"Prioridad entre 1 y {self.niveles}")

        self.colas[prioridad].append(valor)

    def desencolar(self):
        # Recorremos de mayor prioridad a menor
        for i in range(self.niveles, 0, -1):
            if self.colas[i]:
                return self.colas[i].popleft()

        raise IndexError("Cola vacía")

    def cambiar_prioridad(self, valor, nueva_prioridad):
        if not 0 < nueva_prioridad <= self.niveles:
            raise ValueError(f"Prioridad entre 1 y {self.niveles}")

        for i in range(1, self.niveles + 1):
            if valor in self.colas[i]:
                self.colas[i].remove(valor)
                self.colas[nueva_prioridad].append(valor)

                print(f"{valor} cambió a prioridad {nueva_prioridad}")
                return

        print(f"{valor} no se encuentra en la cola")

    def __str__(self):
        s = []
        for i in range(self.niveles, 0, -1):
            if self.colas[i]:
                s.append(f"  P{i}: {list(self.colas[i])}")

        return "\n".join(s) if s else "(vacía)"


# --- Uso ---

cp = ColaPrioridad(3)

cp.encolar("Ana", 1)
cp.encolar("Luis", 3)
cp.encolar("Diana", 1)
cp.encolar("Beto", 2)

print("Cola original:")
print(cp)

# Cambiar prioridad
cp.cambiar_prioridad("Ana", 3)

print("\nCola actualizada:")
print(cp)

# Atender en orden
while True:
    try:
        print("Atendiendo:", cp.desencolar())
    except IndexError:
        break



#Ejercicio4
from collections import deque

cola = deque()
proximo = 1

while True:
    print("\n1.Llega 2.Atender 3.Ver cola 4.Salir")
    op = input("Opción: ")

    if op == "1":
        cola.append(proximo)
        print(f"Ticket {proximo} asignado. {len(cola)} en espera.")
        proximo += 1
    elif op == "2":
        if not cola:
            print("Sin clientes")
        else:
            print(f"Turno {cola.popleft()}")
    elif op == "3":
        print(list(cola))
    elif op == "4":
        break



#Ejercicio5
from collections import deque

jugadores = deque(["Ana", "Beto", "Carlos"])

for turno in range(10):
    actual = jugadores.popleft()      # sale del frente
    print(f"Turno {turno+1}: {actual}")
    jugadores.append(actual)          # vuelve al final




#Ejercicio6
from collections import deque

class ColaConMax:
    def __init__(self):
        self._datos = deque()
        self._max_visto = float("-inf")

    def encolar(self, v):
        self._datos.append(v)
        if v > self._max_visto:
            self._max_visto = v

    def desencolar(self):
        if not self._datos:
            raise IndexError("vacía")
        return self._datos.popleft()

    def maximo_visto(self):
        return self._max_visto


c = ColaConMax()
for x in [5, 3, 8, 2]:
    c.encolar(x)
while c._datos:
    print(c.desencolar())
print("Máximo visto:", c.maximo_visto())



#Ejercicio7
import random
from collections import deque

random.seed(42)                     # para reproducibilidad
cola = deque([f"Cliente-{i+1}" for i in range(10)])

# Dos cajas: cada una guarda (cliente, tiempo_restante) o None si libre
cajas = [None, None]

segundo = 0

while cola or any(cajas):
    # Cada caja libre agarra al primero
    for i in range(2):
        if cajas[i] is None and cola:
            cliente = cola.popleft()
            tiempo = random.randint(30, 90)
            cajas[i] = [cliente, tiempo]
            print(f"[{segundo}s] Caja {i+1}: atendiendo a {cliente} ({tiempo}s)")

    # Cada caja ocupada trabaja 1 segundo
    for i in range(2):
        if cajas[i]:
            cajas[i][1] -= 1
            if cajas[i][1] == 0:
                print(f"[{segundo+1}s] Caja {i+1}: terminó con {cajas[i][0]}")
                cajas[i] = None

    segundo += 1

print(f"\nTiempo total: {segundo}s")










#-------------------------
#  EJERCICIOS DE PILAS
#-------------------------

#Ejercicio1

from collections import deque

def invertir_palabras(s):
    pila = deque()

    # Fase 1: apilar todas las palabras
    for palabra in s.split(" "):
        pila.append(palabra)

    # Fase 2: desapilar formando la salida
    resultado = ""
    while pila:
        resultado += pila.pop() + " "

    return resultado.strip()


print(invertir_palabras("Hola Mundo"))
print(invertir_palabras("Python es genial"))
print(invertir_palabras("Me gusta programar"))




#Ejercicio2

from collections import deque

def paren_balanceado(s):
    pila = deque()
    parejas = {")": "(", "]": "[", "}": "{"}

    for posicion, ch in enumerate(s):
        if ch in "([{":
            # Es apertura, la apilo
            pila.append((ch, posicion))

        elif ch in ")]}":
            # Verificar si existe una apertura
            if not pila:
                return f"Error en posición {posicion}: cierre inesperado '{ch}'"

            apertura, pos_apertura = pila.pop()

            if apertura != parejas[ch]:
                return f"Error en posición {posicion}: '{ch}' no corresponde a '{apertura}'"

    # Verificar si quedaron aperturas sin cerrar
    if pila:
        apertura, posicion = pila.pop()
        return f"Error en posición {posicion}: '{apertura}' sin cerrar"

    return "Expresión balanceada"

# --- Pruebas ---

tests = ["()", "({[]})", "()[]{}", "(]", "({[)]}", "((("]

for t in tests:
    print(f"{t!r:15} → {paren_balanceado(t)}")



#Ejercicio3
from collections import deque

def binario_a_decimal(s):
    pila = deque()

    # Fase 1: apilar los dígitos
    for digito in s:
        pila.append(int(digito))

    # Fase 2: desapilar y convertir a decimal
    decimal = 0
    potencia = 0

    while pila:
        digito = pila.pop()
        decimal += digito * (2 ** potencia)
        potencia += 1

    return decimal

# Pruebas
for s in ["0", "1", "101", "1101", "1100100", "11111111"]:
    print(f"{s:10} → {binario_a_decimal(s)}")




#Ejercicio 4
from collections import deque

historial = deque()

while True:
    print("\n1.Hacer 2.Deshacer 3.Ver historial 4.Salir")
    op = input("Opción: ")

    if op == "1":
        accion = input("Descripción: ")
        historial.append(accion)
        print(f"Hecho: {accion}")

    elif op == "2":
        if not historial:
            print("Nada que deshacer")
        else:
            deshecha = historial.pop()
            print(f"Deshecho: {deshecha}")

    elif op == "3":
        if not historial:
            print("(vacío)")
        else:
            for i, a in enumerate(historial):
                print(f"  {i+1}. {a}")

    elif op == "4":
        break




#Ejercicio5
from collections import deque

def invertir_palabras(frase):
    pila = deque()
    for palabra in frase.split():
        pila.append(palabra)

    resultado = []
    while pila:
        resultado.append(pila.pop())
    return " ".join(resultado)


print(invertir_palabras("Hola Mundo desde Python"))
# Python desde Mundo Hola




#Ejercicio6
from collections import deque

def es_palindromo(s):
    s = s.lower().replace(" ", "")     # normaliza
    pila = deque()

    # Apila la mitad izquierda
    mitad = len(s) // 2
    for i in range(mitad):
        pila.append(s[i])

    # Compara con la mitad derecha (saltando el central si len es impar)
    inicio_der = mitad + (1 if len(s) % 2 == 1 else 0)
    for i in range(inicio_der, len(s)):
        if pila.pop() != s[i]:
            return False
    return True


for p in ["ana", "reconocer", "python", "anita lava la tina"]:
    print(f"{p!r}: {es_palindromo(p)}")




#Ejercicio7
from collections import deque

def evaluar_postfija(expr):
    pila = deque()
    for token in expr.split():
        if token in "+-*/":
            b = pila.pop()      # OJO al orden: b sale primero
            a = pila.pop()
            if token == "+": pila.append(a + b)
            elif token == "-": pila.append(a - b)
            elif token == "*": pila.append(a * b)
            elif token == "/": pila.append(a / b)
        else:
            pila.append(int(token))
    return pila.pop()


print(evaluar_postfija("3 4 +"))         # 7
print(evaluar_postfija("3 4 + 5 *"))     # 35
print(evaluar_postfija("5 1 2 + 4 * + 3 -"))  # 14