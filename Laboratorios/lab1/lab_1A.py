# Lab A
# Nombre: Joan Alexis Villa García
# Cod Estudiante: 202320166

######################################  
#                                   #  
#             Punto #1               #  
#                                   #  
######################################

# Escriba una función llamada primos_hasta(N) que calcule los números primos desde 0 hasta N, donde N es un parámetro de la función. Considere que N nunca va a ser un número mayor a 10000.
# Calcule el contador de frecuencias de cada línea y el orden de magnitud del algoritmo

# INICIO_SOLUCION
def primos_hasta(N):
    if N < 2:  # Frecuencia: 1
        return []  # Frecuencia: 1

    es_primo = [True] * (N + 1)  # Frecuencia: 1
    es_primo[0] = es_primo[1] = False  # Frecuencia: 1

    for i in range(2, int(N**0.5) + 1):  # Frecuencia: sqrt(N)
        if es_primo[i]:  # Frecuencia: sqrt(N)
            for j in range(i * i, N + 1, i):  # Frecuencia: N log log N
                es_primo[j] = False  # Frecuencia: N log log N

    primos = [num for num in range(N + 1) if es_primo[num]]  # Frecuencia: N
    return primos  # Frecuencia: 1

# Contador de frecuencias total:
# 1 (if N < 2) + 1 (return []) + 1 (es_primo = [True] * (N + 1)) + 1 (es_primo[0] = es_primo[1] = False) +
# sqrt(N) (for i in range(2, int(N**0.5) + 1)) + sqrt(N) (if es_primo[i]) +
# N log log N (for j in range(i * i, N + 1, i)) + N log log N (es_primo[j] = False) +
# N (primos = [num for num in range(N + 1) if es_primo[num]]) + 1 (return primos)

# Orden de magnitud: O(N log log N)

print(primos_hasta(10))
print(primos_hasta(20))
print(primos_hasta(30))
print(primos_hasta(40))
print(primos_hasta(50))
# FIN_SOLUCION


######################################  
#                                   #  
#             Punto #2               #  
#                                   #  
######################################

# Escriba una función llamada potencia_mas_cercana(N,M) que calcule el exponente de la potencia de N más cercana a M, por ejemplo, potencia_mas_cercana(2,1000) devolvera 10, potencia_mas_cercana(4,40) devolverá 2 y potencia_mas_cercana(10,10000010) devolverá 7.
# Calcule el contador de frecuencias de cada línea, el contador de frecuencias total y el orden de magnitud del algoritmo

# INICIO_SOLUCION
def potencia_mas_cercana(N, M):
    if N == 1:  # Frecuencia: 1
        return 0  # Frecuencia: 1

    exponente = 0  # Frecuencia: 1  
    while N**exponente <= M:  # Frecuencia: log_N(M) + 1
        exponente += 1  # Frecuencia: log_N(M) + 1

    potencia_anterior = N**(exponente - 1)  # Frecuencia: 1  
    potencia_siguiente = N**exponente  # Frecuencia: 1  

    if abs(M - potencia_anterior) <= abs(M - potencia_siguiente):  # Frecuencia: 1
        return exponente - 1  # Frecuencia: 1
    else:
        return exponente  # Frecuencia: 1

print(potencia_mas_cercana(2, 1000))
print(potencia_mas_cercana(4, 40))
print(potencia_mas_cercana(10, 10000010)) 
# FIN_SOLUCION

######################################  
#                                   #  
#             Punto #3               #  
#                                   #  
######################################

# Escriba una función llamada repetidos(v) donde v es un arreglo unidimensional, retorne un nuevo arreglo con los elementos que se repiten 2 o más veces dentro del arreglo.
# Calcule el contador de frecuencias de cada línea, el contador de frecuencias total y el orden de magnitud del algoritmo

# INICIO_SOLUCION
def repetidos(v):
    contador = {}  # Frecuencia: 1
    
    for num in v:  # Frecuencia: N
        if num in contador:  # Frecuencia: N
            contador[num] += 1  # Frecuencia: N
        else:
            contador[num] = 1  # Frecuencia: N

    resultado = [num for num, count in contador.items() if count >= 2]  # Frecuencia: N
    
    return resultado  # Frecuencia: 1

# Contador de frecuencias total:
# 1 (contador = {}) + N (for num in v) + N (if num in contador) +
# N (contador[num] += 1 o contador[num] = 1) + N (filtrar elementos repetidos) + 1 (return resultado)

# Orden de magnitud: O(N)

print(repetidos([1, 2, 3, 2, 4, 5, 6, 4, 4]))  
print(repetidos([10, 20, 10, 30, 40, 50, 50, 10])) 
print(repetidos([1, 2, 3, 4, 5]))  
# FIN_SOLUCION


######################################  
#                                   #  
#             Punto #4               #  
#                                   #  
######################################

# Escriba un método adicional en la clase LSL (Lista Simplemente Ligada) vista en clase llamado eliminar_pos(i), este método eliminará el elemento en la posición i de la lista. Considere que si no existe el elemento debe lanzar un error. En la medida de lo posible, use los métodos ya existentes en la clase, evite reinventar la rueda.
# Calcule el contador de frecuencias de cada línea, el contador de frecuencias total y el orden de magnitud del algoritmo


# INICIO_SOLUCION
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.liga = None

class LSL:
    def __init__(self):
        self.primero = None

    def esVacia(self):
        return self.primero is None

    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.esVacia():
            self.primero = nodo
        else:
            temp = self.primero
            while temp.liga:
                temp = temp.liga
            temp.liga = nodo

    def mostrar(self):
        temp = self.primero
        while temp:
            print(temp.dato, end=" -> ")
            temp = temp.liga
        print("None")

    def eliminar_pos(self, i):
        if self.esVacia():  # Frecuencia: 1
            raise IndexError("La lista está vacía")  # Frecuencia: 1

        if i == 0:  # Frecuencia: 1
            self.primero = self.primero.liga  # Frecuencia: 1
            return

        temp = self.primero  # Frecuencia: 1
        contador = 0  # Frecuencia: 1

        while temp is not None and contador < i - 1:  # Frecuencia: i
            temp = temp.liga  # Frecuencia: i
            contador += 1  # Frecuencia: i

        if temp is None or temp.liga is None:  # Frecuencia: 1
            raise IndexError("Índice fuera de rango")  # Frecuencia: 1

        temp.liga = temp.liga.liga  # Frecuencia: 1

# Contador de frecuencias total:
# 1 (if self.esVacia()) + 1 (raise IndexError) + 1 (if i == 0) + 1 (self.primero = self.primero.liga) + 
# 1 (temp = self.primero) + 1 (contador = 0) + i (while temp is not None and contador < i - 1) + 
# i (temp = temp.liga) + i (contador += 1) + 1 (if temp is None or temp.liga is None) +
# 1 (raise IndexError) + 1 (temp.liga = temp.liga.liga)

# Orden de magnitud: O(i) (búsqueda del nodo a eliminar)

lista = LSL()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)
lista.insertar(50)

print("Lista antes de eliminar:")
lista.mostrar()

lista.eliminar_pos(2)

print("Lista después de eliminar el elemento en la posición 2:")
lista.mostrar()

lista2 = LSL()
lista2.insertar(1)
lista2.insertar(2)
lista2.insertar(3)

print("\nLista antes de eliminar:")
lista2.mostrar()

try:
    lista2.eliminar_pos(5)
except IndexError as e:
    print(f"Error capturado: {e}")

print("Lista después de intentar eliminar una posición fuera de rango:")
lista2.mostrar()
# FIN_SOLUCION

######################################  
#                                   #  
#             Punto 5               #  
#                                   #  
######################################

# Escriba un método adicional en la clase LSL (Lista Simplemente Ligada) vista en clase llamado insertar_pos(i,dato), este método insertara el elemento 'dato' en la posición i de la lista. Considere que si no existe la posición se debe lanzar un error, esto a menos que se trate de una lista vacia y se quiera insertar en la primera posición o que se quiera insertar al final, en caso tal se debe insertar en esas posiciones. En la medida de lo posible, use los métodos ya existentes en la clase, evite reinventar la rueda.
# Calcule el contador de frecuencias de cada línea, el contador de frecuencias total y el orden de magnitud del algoritmo.


# INICIO_SOLUCION
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.liga = None

class LSL:
    def __init__(self):
        self.primero = None

    def esVacia(self):
        return self.primero is None

    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.esVacia():
            self.primero = nodo
        else:
            temp = self.primero
            while temp.liga:
                temp = temp.liga
            temp.liga = nodo

    def mostrar(self):
        temp = self.primero
        while temp:
            print(temp.dato, end=" -> ")
            temp = temp.liga
        print("None")

    def insertar_pos(self, i, dato):
        nuevo_nodo = Nodo(dato)  # Frecuencia: 1

        if i == 0:  # Frecuencia: 1
            nuevo_nodo.liga = self.primero  # Frecuencia: 1
            self.primero = nuevo_nodo  # Frecuencia: 1
            return

        temp = self.primero  # Frecuencia: 1
        contador = 0  # Frecuencia: 1

        while temp is not None and contador < i - 1:  # Frecuencia: i
            temp = temp.liga  # Frecuencia: i
            contador += 1  # Frecuencia: i

        if temp is None:  # Frecuencia: 1
            raise IndexError("Índice fuera de rango")  # Frecuencia: 1

        nuevo_nodo.liga = temp.liga  # Frecuencia: 1
        temp.liga = nuevo_nodo  # Frecuencia: 1

# **Contador de frecuencias total:**
# 1 (nuevo_nodo = Nodo(dato)) + 1 (if i == 0) + 1 (nuevo_nodo.liga = self.primero) +
# 1 (self.primero = nuevo_nodo) + 1 (temp = self.primero) + 1 (contador = 0) +
# i (while temp is not None and contador < i - 1) + i (temp = temp.liga) + i (contador += 1) +
# 1 (if temp is None) + 1 (raise IndexError) + 1 (nuevo_nodo.liga = temp.liga) + 1 (temp.liga = nuevo_nodo)

# **Orden de magnitud:** O(i) (búsqueda de la posición a insertar)

lista = LSL()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)

print("Lista antes de insertar:")
lista.mostrar()

lista.insertar_pos(1, 15)
print("Lista después de insertar 15 en posición 1:")
lista.mostrar()

lista.insertar_pos(0, 5)
print("Lista después de insertar 5 en la primera posición:")
lista.mostrar()

lista.insertar_pos(5, 40)
print("Lista después de insertar 40 en la última posición:")
lista.mostrar()

try:
    lista.insertar_pos(10, 50)  
except IndexError as e:
    print(f"Error capturado: {e}")

print("Lista final:")
lista.mostrar()
# FIN_SOLUCION

######################################  
#                                   #  
#             Punto 6               #  
#                                   #  
######################################

# Escriba un método adicional en la clase LSL (Lista Simplemente Ligada) vista en clase llamada invertir(), este método invertirá la lista por completo.
# Calcule el contador de frecuencias de cada línea, el contador de frecuencias total y el orden de magnitud del algoritmo.


# INICIO_SOLUCION
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.liga = None

class LSL:
    def __init__(self):
        self.primero = None

    def esVacia(self):
        return self.primero is None

    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.esVacia():
            self.primero = nodo
        else:
            temp = self.primero
            while temp.liga:
                temp = temp.liga
            temp.liga = nodo

    def mostrar(self):
        temp = self.primero
        while temp:
            print(temp.dato, end=" -> ")
            temp = temp.liga
        print("None")

    def invertir(self):
        prev = None  # Frecuencia: 1
        actual = self.primero  # Frecuencia: 1

        while actual is not None:  # Frecuencia: n
            siguiente = actual.liga  # Frecuencia: n
            actual.liga = prev  # Frecuencia: n
            prev = actual  # Frecuencia: n
            actual = siguiente  # Frecuencia: n

        self.primero = prev  # Frecuencia: 1

# Contador de frecuencias total:
# 1 (prev = None) + 1 (actual = self.primero) + n (while actual is not None) +
# n (siguiente = actual.liga) + n (actual.liga = prev) + n (prev = actual) + n (actual = siguiente) + 1 (self.primero = prev)
# Orden de magnitud: **O(n)**

lista = LSL()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)
lista.insertar(50)

print("Lista antes de invertir:")
lista.mostrar()

lista.invertir()

print("Lista después de invertir:")
lista.mostrar()
# FIN_SOLUCION

######################################  
#                                   #  
#             Punto 7               #  
#                                   #  
######################################

# Escriba un método adicional en la clase LSL (Lista Simplemente Ligada) vista en clase llamada duplicar(), este método duplicará la lista por completo poniendo el duplicado al final de la lista original.
# Calcule el contador de frecuencias de cada línea, el contador de frecuencias total y el orden de magnitud del algoritmo.


# INICIO_SOLUCION
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.liga = None

class LSL:
    def __init__(self):
        self.primero = None

    def esVacia(self):
        return self.primero is None

    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.esVacia():
            self.primero = nodo
        else:
            temp = self.primero
            while temp.liga:
                temp = temp.liga
            temp.liga = nodo

    def mostrar(self):
        temp = self.primero
        while temp:
            print(temp.dato, end=" -> ")
            temp = temp.liga
        print("None")

    def duplicar(self):
        if self.esVacia():  # Frecuencia: 1
            return  # Frecuencia: 1

        temp = self.primero  # Frecuencia: 1
        nuevo_inicio = None  # Frecuencia: 1
        nuevo_ultimo = None  # Frecuencia: 1
        
        # Crear una copia de la lista original
        while temp:  # Frecuencia: n
            nuevo_nodo = Nodo(temp.dato)  # Frecuencia: n
            if nuevo_inicio is None:  # Frecuencia: 1
                nuevo_inicio = nuevo_nodo  # Frecuencia: 1
                nuevo_ultimo = nuevo_nodo  # Frecuencia: 1
            else:
                nuevo_ultimo.liga = nuevo_nodo  # Frecuencia: n - 1
                nuevo_ultimo = nuevo_nodo  # Frecuencia: n - 1
            temp = temp.liga  # Frecuencia: n

        # Conectar la lista duplicada al final de la original
        temp = self.primero  # Frecuencia: 1
        while temp.liga:  # Frecuencia: n
            temp = temp.liga  # Frecuencia: n
        temp.liga = nuevo_inicio  # Frecuencia: 1

        # Contador de frecuencias total:
        # 1 (if self.esVacia()) + 1 (return) + 1 (temp = self.primero) + 1 (nuevo_inicio = None) +
        # 1 (nuevo_ultimo = None) + n (while temp) + n (nuevo_nodo = Nodo(temp.dato)) + 1 (if nuevo_inicio is None) +
        # 1 (nuevo_inicio = nuevo_nodo) + 1 (nuevo_ultimo = nuevo_nodo) + (n-1) (nuevo_ultimo.liga = nuevo_nodo) +
        # (n-1) (nuevo_ultimo = nuevo_nodo) + n (temp = temp.liga) + 1 (temp = self.primero) +
        # n (while temp.liga) + n (temp = temp.liga) + 1 (temp.liga = nuevo_inicio)
        # Complejidad total: **O(n)**

lista = LSL()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)

print("Lista antes de duplicar:")
lista.mostrar()

lista.duplicar()

print("Lista después de duplicar:")
lista.mostrar()

lista_vacia = LSL()

print("Lista antes de duplicar (vacía):")
lista_vacia.mostrar()

lista_vacia.duplicar()

print("Lista después de duplicar (vacía):")
lista_vacia.mostrar()
# FIN_SOLUCION
