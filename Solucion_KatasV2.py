# %%
# Importamos la función "reduce()" para los ejercicios 17, 22, 23 y 24

from functools import reduce

# %%
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados

def frecuencias_letras(cadena):
    cadena=cadena.replace(" ","") # esto es para eliminar los espacios
    frecuencias = {}
    for caracter in cadena:
        frecuencias[caracter]=frecuencias.get(caracter,0)+1
    return frecuencias

# %%
# Ejecución n.1

texto = "Me llamo Juan Pablo"
print (frecuencias_letras(texto))

# %%
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def doblar_lista(lista):
    return list(map(lambda x: x* 2, lista))

# %%
# Ejecución n.2

lista=[1,2,3,4]
print(doblar_lista(lista))

# %%
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo

def filtrar_palabra(lista,objetivo):
    return[palabra for palabra in lista if objetivo in palabra] 

# Corrección ejercicio: he cambiado lista_palabras por lista en el código "return[palabra for palabra in lista_palabras if objetivo in palabra]" por "return[palabra for palabra in lista if objetivo in palabra]"

# %%
# Ejecución n.3

lista=["panaderia", "carniceria", "pescaderia", "supermercado", "panadero", "perfumeria", "empanada"]
objetivo="pan"

resultado=filtrar_palabra(lista,objetivo)
print(resultado)

# Corrección ejercicio: he cambiado el parámetro "lista_palabras=[XX]" por "lista=[XX]"


# %%
# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    return list(map(lambda x,y: x-y, lista1, lista2))

# %%
# Ejecución n.4

lista1=[10, 15, 20, 25, 30]
lista2=[5, 13, 8, 25, 35]

resultado=diferencia_listas(lista1,lista2)
print(resultado)

# %%
# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado

def media_notas (numeros, nota_aprobado=5):
    if not numeros: # por si no hay nota, para que no divida entre 0
        return (0,"suspenso")

    media = sum (numeros)/len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (round(media,2), estado)

# %%
# Ejecución n.5

notas = [0, 2, 3, 6, 7, 5, 3.5]
resultado=media_notas(notas)
print(resultado)

# %%
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n==0 or n==1: 
        return 1 # utilizamos este condicional para garantizar el final del cálculo
    else:
        return n*factorial(n-1)

# %%
# Ejecución n.6

n=10
resultado = factorial(n)
print(f"El factorial de {n} es: {resultado}")

# %%
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def lista_tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: str(t), lista_tuplas))

# %%
# Ejecución n.7

lista_tuplas=[(4, 5), ("a","b"), (7, 8)]
resultado= lista_tuplas_a_strings(lista_tuplas)
print (resultado)

# %%
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero,
# maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    resultado = num1 / num2
    print(f"La división fue exitosa. Resultado: {resultado}")

except ValueError:
    print("Error: Debes ingresar valores numéricos.")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# %%
# Ejecución n.8

# Caso 1
# Valor num1: 20
# Valor num2: 10
# Resultado:
#   La división fue exitosa. Resultado: 2.0

# Caso 2
# Valor num1: 20
# Valor num2: 0
# Resultado:
#   Error: No se puede dividir entre cero.

# Caso 3
# Valor num1: 0
# Valor num2: 10
# Resultado:
#   La división fue exitosa. Resultado: 0.0


# %%
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()

def filtrar_lista_mascotas(mascotas):
    prohibidas=["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"] 

    # Convertimos en minúscula para comparar sin tener en cuenta las mayúsculas o minúsculas
    prohibidas_lower = [p.lower() for p in prohibidas] 

    return list(filter(lambda mascota: mascota.lower() not in prohibidas_lower, mascotas))

# %%
# Ejecución n.9

lista_mascotas=["tiGre", "Oso", "perro", "gato", "COCOdrilo", "loro"]
resultado= filtrar_lista_mascotas(lista_mascotas)
print(resultado)

# %%
# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception): #excepción personalizada
    pass

def calcular_promedio(lista):
    if not lista:
        raise ListaVaciaError("La lista está vacía. No se puede calcular el promedio")
    return round(sum(lista)/len(lista),2)



# %%
# Ejecución n. 10

try:
    print(calcular_promedio([1,3,5,7,2,8]))
except ListaVaciaError as e:
    print (e)

# Ejecución 10.1
try:
    print(calcular_promedio([]))
except ListaVaciaError as e:
    print (e)

# %%
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

while True:
    try:
        edad = int(input("Introduce tu edad: "))

        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años.")

        print(f"Edad válida: {edad}")
        break  # Salimos del bucle si todo es válido

    except ValueError:
        print("Error: Debes ingresar un número válido entre 0 y 120.\n")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}\n")


# %%
# Ejecución n. 11

# Caso 1
# Edad: 80
# Resultado:
#   Edad válida: 80

# Caso 2
# Edad: 80
# Resultado:
#   Edad válida: 80

# %%
# Nota ejercicio 11.1 Planteo otra opción de hacerlo, ya que en la anterior si introduzco una edad erronea, sigue el bucle esperando hasta que ponga una edad correcta.

edad = input("Introduce tu edad: ")

if not edad.isdigit():
    print("Error: debes introducir un número.")
else:
    edad = int(edad)
    
    if edad < 0:
        print("Error: la edad no puede ser negativa.")
            
    elif edad > 120:
        print("Error: la edad no puede ser mayor de 120 años.")
    else:    
        print(f"Tu edad es {edad} años.")


# Ejecución
# Si pongo 130 años, el resultado es: Error: la edad no puede ser mayor de 120 años.

# %%
# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    palabras=frase.split()  # utilizamos split para separar por espacios
    return list(map(len,palabras))


# %%
# Ejecución n. 12

resultado=longitud_palabras('Me llamo Juan Pablo')
print(resultado)

# %%
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. 
# Usa la función map()

def mayus_minus_unicas(caracteres):
    unicos=sorted(set(c.lower() for c in caracteres)) #convertimos a un conjunto para eliminar los caracteres repetidos
    
    # creamos las tuplas (tanto en mayuscula-upper como minuscula-lower)
    return list(map(lambda c: (c.upper(), c.lower()), unicos))


# %%
# Ejecución n. 13

resultado=mayus_minus_unicas("aJAbBcdCf")
print (resultado)

# %%
# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def palabras_con_letra(lista_de_palabras, letra):
    letra=letra.lower() # para no distinguir entre mayúscula ni minúscula
    return list(filter(lambda palabra: palabra.lower().startswith(letra),lista_de_palabras))



# %%
# Ejecución n. 14

lista_de_palabras=["Carnicería","panadería","coche","bicicleta","sofá","cama"]
resultado=palabras_con_letra(lista_de_palabras,"c")
print (resultado)

# %%
# 15. Crea una función lambda que sume 3 a cada número de una lista dada

sumar_tres=lambda numeros: list(map(lambda x: x+3, numeros))


# %%
# Ejecución n. 15

resultado=sumar_tres([3,5,7,9])
print (resultado)

# %%
# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. 
# Usa la función filter()

def palabras_mas_larga(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda palabra: len(palabra)>n, palabras))

# %%
# Ejecución n. 16

cadena = "Me gustaría viajar a Laponia, ver auroras boreales y la ciudad de Papa Noel"
resultado = palabras_mas_larga(cadena, 5)
print(resultado)

# %%
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). 
# Usa la función reduce()

# Buenas prácticas: importamos la función reduce utilizando el módulo functools al inicio del archivo

def lista_a_número(dígitos):
    return reduce(lambda acumulado, d: acumulado * 10 + d, dígitos)

# %%
# Ejecución n. 17 
resultado = lista_a_número([8,9,6])
print(resultado)

# Buenas prácticas: importamos la función reduce utilizando el módulo functools al inicio del archivo

# %%
# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación)
# y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

# Lista de diccionarios con información de estudiantes
estudiantes = [
    {"nombre": "Pepe", "edad": 20, "calificacion": 95},
    {"nombre": "Daniela", "edad": 22, "calificacion": 88},
    {"nombre": "María", "edad": 19, "calificacion": 90},
    {"nombre": "Carmen", "edad": 21, "calificacion": 72},
    {"nombre": "Elena", "edad": 23, "calificacion": 99}
]

# Filtrar estudiantes con calificación >= 90
excelentes = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))



# %%
# Ejecución n. 18

# Mostrar resultados
print("Estudiantes con calificación mayor o igual a 90:")
for est in excelentes:
    print(est)


# %%
# 19. Crea una función lambda que filtre los números impares de una lista dada.

filtrar_impares = lambda numeros: list(filter(lambda x: x % 2 !=0, numeros))
# utilizamos el operador módulo "% 2 ! = 0" que devuelve el resto de una división. Si el resto al dividir por 2 es diferente de 0, quiere decir que es un número impar.

# %%
# Ejecución n. 19

resultado = filtrar_impares ([10, 20, 33, 42, 55, 68, 123, 231])
print (resultado)

# %%
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def filtrar_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))



# %%
# Ejecución n. 20

lista = [2, 5, "dos", "cinco", 32, "hola"]
resultado = filtrar_enteros(lista)
print (resultado)

# %%
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.

cubo = lambda x : x**3

# Ejecución n. 21
print(cubo(5))
print(cubo(4))

# %%
# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().

# Buenas prácticas: importamos la función "reduce()" utilizando el módulo functools al inicio del archivo 
numeros = [1, 43, 5, 87]
producto_total = reduce (lambda x, y: x * y, numeros)

# Ejecución n. 22
print ("El producto total es:", producto_total)

# %%
# 23. Concatena una lista de palabras.Usa la función reduce().

# Buenas prácticas: importamos la función "reduce()" utilizando el módulo functools al inicio del archivo 
lista_de_palabras = ["Hola", "me", "llamo", "Juan", "Pablo"]

# Ejecución n. 23

resultado = reduce (lambda x, y: x + " " + y, lista_de_palabras)
print ("La frase concatenada es:", resultado)

# %%
# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

# Buenas prácticas: importamos la función "reduce()" utilizando el módulo functools al inicio del archivo 
lista_de_numeros =[25, 30, 15, 5]

# Ejecución n. 24

resultado = reduce (lambda x, y: x - y, lista_de_numeros)
print ("La diferencia total es:", resultado)

# %%
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    return len(cadena)

# %%
# Ejecución n. 25

cadena = "Hola, me llamo Juan Pablo"
print (contar_caracteres (cadena))

# %%
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x, y: x % y

# Ejecución n. 26

print (resto(3, 5))
print (resto(39, 2))
print (resto(22, 3))

# %%
# Nota: Repetimos el ejercicio 26 pero con manejo de error para evitar dividir entre 0

resto = lambda x, y: (_ for _ in ()).throw(ZeroDivisionError("No se puede dividir entre 0")) if y == 0 else x % y

try:
    print (resto(3, 5))
    print (resto(39, 2))
    print (resto(22, 0))
except ZeroDivisionError as e:
    print("Error, no se puede dividir entre 0")

# %%
# 27. Crea una función que calcule el promedio de una lista de números.

def promedio(lista):
    if len(lista) == 0: # para que no haga la división entre 0
        return 0 
    return sum(lista)/len(lista)

# %%
lista = [0, 5, 12, 24]
print(promedio(lista))

# %%
# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set() # conjunto para guardar los elementos ya vistos

    for elementos in lista:
        if elementos in vistos: # si ya está en el conjunto, es un duplicado
            return elementos
        vistos.add(elementos) # se guarda si es el primera vez que aparece en la lista

    return "None: no hay números duplicados"

# Corrección ejercicio: cambio "none" por "None", ya que había escrito "none" en minúscula

# %%
lista_numeros = [1, 2, 4, 5, 7, 3]
print(primer_duplicado(lista_numeros))

# %%
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarar(variable):
    texto = str (variable)
    if len(texto) <=4:
        return texto   # si el texto es menor de 4 caracteres, no se enmascara
    return "#" * (len(texto) - 4) + texto [-4:]

# %%
print(enmascarar("123456789"))
print(enmascarar("Me llamo Juan Pablo"))
print(enmascarar("123"))

# %%
# 30.Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    p1 = palabra1.replace(" ", "").lower()
    p2 = palabra2.replace(" ", "").lower()
# eliminamos los espacios y convertimos en minúscula para comparar de forma correcta
    
    return sorted (p1) == sorted (p2)

# %%
print (son_anagramas("animal", "lamina"))
print (son_anagramas("futbol", "pelota"))
print (son_anagramas("Roma", "amor"))
print (son_anagramas("Ecuador", "acuerdo"))

# %%
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. 
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre_en_lista(lista):
    # 1. Solicitar la lista de nombres
    entrada = input("Ingresa una lista de nombres separados por comas: ")
    
    # Convertimos la cadena de texto en una lista y limpiamos espacios en blanco
    lista_nombres = [nombre.strip() for nombre in entrada.split(',')]
    
    # 2. Solicitar el nombre a buscar
    nombre_buscado = input("Ingresa el nombre que quieres buscar: ")
    
    # 3. Lógica de búsqueda
    if nombre_buscado in lista_nombres:
        print(f"¡Éxito! El nombre '{nombre_buscado}' fue encontrado en la lista.")
    else:
        # Lanzamos la excepción si no está
        raise ValueError(f"El nombre '{nombre_buscado}' no se encuentra en la lista ingresada.")

# Ejecutar la función para probarla
buscar_nombre_en_lista("Ana, Carlos, Antonio, Juan")
nombre_buscado = ("Juan")


# Corrección ejercicio. Añado argumento en "buscar_nombre_en_lista(lista)" e introduzco la lista como input.

# %%
# código propuesto por el profesor

def buscar_nombre_en_lista(lista_entrada=None, nombre=None):
    if lista_entrada is None:
        lista_entrada = input("Ingresa una lista de nombres separados por comas: ")
    lista_nombres = [n.strip() for n in lista_entrada.split(',')]

    if nombre is None:
        nombre = input("Ingresa el nombre a buscar: ").strip()

    if nombre in lista_nombres:
        print(f"Éxito. El nombre '{nombre}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre}' no se encuentra en la lista.")


# %%
# código propuesto por el profesor

buscar_nombre_en_lista("Ana, Carlos, Antonio, Juan", "Juan")

# %%
# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista,
# de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto(nombre_completo, lista_empleados):
    # buscamos el nombre del empleado para devolver el puesto de trabajo
    # str (nombre_completo); nombre completo a buscar
    # lista_empleados: lista de diccionarios con claves tipo "nombre"
    for empleado in lista_empleados:
        if empleado ["nombre"].lower() == nombre_completo.lower():
            return f"{nombre_completo} ocupa el puesto de {empleado['puesto']}"
    return f"{nombre_completo} no trabaja aquí"

# %%
# Ejecución n. 32

empleados = [
    {"nombre": "Juan Pablo Planelles", "puesto": "Departamento I+D"},
    {"nombre": "Antonio González", "puesto": "Administrativo"},
    {"nombre": "María Martínez", "puesto": "Profesora"},
    {"nombre": "Mari Carmen", "puesto": "Gerente"}
]
print (buscar_puesto("Juan Pablo Planelles", empleados))
print (buscar_puesto("Mari Carmen", empleados))
print (buscar_puesto("Felipe Juan", empleados))

# %%
# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda l1, l2: [a + b for a, b in zip(l1, l2)]

# %%
# Ejecución n. 33

lista1 = [1, 2, 3]
lista2 = [7, 8, 9]
print (sumar_listas(lista1, lista2))

# %%
# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama ,
# crecer_ramas , quitar_rama e info_arbol. El objetivo es implementar estos métodos para manipular la estructura del árbol. Código a seguir:

class Arbol:
    def __init__(self): # correccion ejercicio. Había puesto sólo 1 guión bajo en lugar de 2 que tiene que llevar.

    ## 34.1 Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
        self.tronco = 1
        self.ramas = []
    
    ## 34.2 Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.

    def crecer_tronco(self):
        self.tronco += 1

    ## 34.3 Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.

    def nueva_rama(self):
        self.ramas.append(1)

    ## 34.4 Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    ## 34.5 Implementar el método quitar_rama para eliminar una rama en una posición específica.

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición errónea: no existe esta rama")
    
    ## 34.6 Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.

    def info_arbol(self):
        return {
            "longitud_del_tronco": self.tronco,
            "numero_de_ramas": len(self.ramas),
            "longitud_ramas": self.ramas
        }


# %%
# Ejecución n. 34: Caso de uso:

## 1. Crear un árbol.
mi_arbol = Arbol()

## 2. Hacer crecer el tronco del árbol una unidad.
mi_arbol.crecer_tronco()

## 3. Añadir una nueva rama al árbol.
mi_arbol.nueva_rama()

## 4. Hacer crecer todas las ramas del árbol una unidad.
mi_arbol.crecer_ramas()

## 5. Añadir dos nuevas ramas al árbol.
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

## 6. Retirar la rama situada en la posición 2.
mi_arbol.quitar_rama(2)

## 7. Obtener información sobre el árbol.
info = mi_arbol.info_arbol()
print(info)

# %%
# 35. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones
# como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo. Código a seguir:

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):

## 35.1 Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .

        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

## 35.2  Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad tiene que ser mayor que cero.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene saldo suficiente.")
        self.saldo -= cantidad

## 35.3 Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad tiene que ser mayor que cero.")    
        if not otro_usuario.cuenta_corriente:
            raise ValueError(f"{otro_usuario.nombre} no tiene cuenta corriente.")
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene saldo suficiente para transferir.")

    # Transferencia
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

## 35.4 Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad tiene que ser mayor que cero.")
        self.saldo += cantidad

    def info(self):
        return f"Usuario: {self.nombre}, saldo: {self.saldo}, cuenta corriente: {self.cuenta_corriente}"




# %%
# Ejecución n. 35: Caso de uso:

## 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.

Alicia = UsuarioBanco("Alicia", 100, True)
Bob = UsuarioBanco("Bob", 50, True)

## 2. Agregar 20 unidades de saldo de "Bob". 

Bob.agregar_dinero(20)

## 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
""" Con esta cantidad de 80 ud de saldo, Bob no tiene suficiente, ya que partimos de 50ud iniciales + 20 ud que agregamos en el punto 2, por lo que dará ValueError"""

Alicia.transferir_dinero(Bob, 80)

## 4. Retirar 50 unidades de saldo a "Alicia".

Alicia.retirar_dinero(50)

# Mostramos la información final

print(Alicia.info())
print(Bob.info())


# %%
# Ejecución n. 35.1: Caso de uso --> Cambiamos alguna cantidad de saldo para que no me de error y comprobar que es ok.

## 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.

Alicia = UsuarioBanco("Alicia", 100, True)
Bob = UsuarioBanco("Bob", 50, True)

## 2. Agregar 200 unidades de saldo de "Bob". ATENCIÓN, aquí hago el cambio, agrego 200 unidades de saldo en lugar de los 20 iniciales.

Bob.agregar_dinero(200)

## 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".

Alicia.transferir_dinero(Bob, 80)

## 4. Retirar 50 unidades de saldo a "Alicia".

Alicia.retirar_dinero(50)

# Mostramos la información final

print(Alicia.info())
print(Bob.info())



# %%
# 36. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabra.
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto. Código a seguir:

# 36.1 Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.

def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower()
        conteo [palabra] = conteo.get(palabra, 0) + 1
    return conteo

# 36.2 Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva. Tiene que devolver el texto con el remplazo de palabras.

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

# 36.3 Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra_a_eliminar]
    return " ".join(palabras_filtradas)

# 36.4 Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para 'reemplazar' se necesitan: palabra_original, palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1])
    
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para 'eliminar' se necesita: palabra_a_eliminar")
        return eliminar_palabra(texto, args[0])
    
    else:
        raise ValueError("Opción no válida. Utiliza: 'contar', 'reemplazar', 'eliminar'.")

# %%
# Ejecución n. 36. Caso de uso

# Comprueba el funcionamiento completo de la función procesar_texto.

# Función contar_palabras
procesar_texto("hola Pepe, hola Juan, hola Antonio", "contar")
    # resultado: {'hola': 3, 'pepe,': 1, 'juan,': 1, 'antonio': 1}

# Función reemplazar_palabras
procesar_texto("hola Pepe", "reemplazar", "Pepe", "Juan")
    # resultado: 'hola Juan'


# Función eliminar_palabra
procesar_texto("hola Antonio", "eliminar", "Antonio")
    # resultado: 'hola'

# NOTA: he ido comprobando uno a uno para ver el resultado. Si lo ejecuto todo a la vez, el resultado es 'hola'





# %%

# Ejecución n. 36. Caso de uso. Planteamiento para que se resuelva todo a la vez

# Texto de ejemplo
texto = "hola Pepe, hola Juan, hola Antonio"


print("=== CASO DE USO: CONTAR PALABRAS ===")
resultado_contar = procesar_texto(texto, "contar")
print(resultado_contar)


print("\n=== CASO DE USO: REEMPLAZAR PALABRAS ===")
resultado_reemplazar = procesar_texto(texto, "reemplazar", "Pepe", "Juan")
print(resultado_reemplazar)


print("\n=== CASO DE USO: ELIMINAR PALABRA ===")
resultado_eliminar = procesar_texto(texto, "eliminar", "Antonio")
print(resultado_eliminar)


# %%
# 37. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def momento_del_dia(hora, minuto):
    if not (0 <= hora <= 23 and 0 <= minuto <= 59):
        return "Hora inválida. Debe estar entre 00:00 y 23:59."

    # Definimos rangos según la hora
    if 6 <= hora < 14:
        return "Es de mañana."
    elif 14 <= hora < 20:
        return "Es de tarde."
    else:
        return "Es de noche."


try:
    hora_usuario = input("Introduce la hora en formato HH:MM → ")

    # Separar horas y minutos
    partes = hora_usuario.split(":")
    if len(partes) != 2:
        raise ValueError("Formato incorrecto, usa HH:MM")

    hora = int(partes[0])
    minuto = int(partes[1])

    print(momento_del_dia(hora, minuto))

except ValueError as e:
    print("Error:", e)


# %%
# Ejección n.37 
# voy poniendo horas

# 10:15 - Es de mañana.
# 10 15 - Error: Formato incorrecto, usa HH:MM
# 14:01 - Es de tarde.
# 22:33 - Es de noche.

# %%
# 38. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:

# 0 - 69 insuficiente
# 70 - 79 bien
# 80 - 89 muy bien
# 90 - 100 excelente

def calificacion_alumno(nota):
    if not (0 <= nota <= 100):
        return "La calificación debe estar entre 0 y 100"
    
    if 0 <= nota <= 69:
        return "Insuficiente"
    
    elif 70 <= nota <= 79:
        return "Bien"
    
    elif 80 <= nota <= 89:
        return "Muy bien"
    
    else:
        90 <= nota <= 100
        return "Excelente"


try:
    nota_alumno = int(input("Introduce la calificación (0-100): "))
    print("Tu calificación es: ", calificacion_alumno(nota_alumno))

except ValueError:
    print("Error: debes introducir un número entero")


# %%
# Ejección n.38 
# voy poniendo notas en el input

# 40 - Tu calificación es:  Insuficiente
# 75 - Tu calificación es:  Bien
# 80.5 - Error: debes introducir un número entero


# %%
# 39. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y
# datos (una tupla con los datos necesarios para calcular el área de la figura).

def calcular_area(figura, datos):
    figura = figura.lower()

    if figura == "rectangulo":
        if len(datos) != 2:
            return "Error: un rectángulo necesita (base, altura)."
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        if len(datos) != 1:
            return "Error: un círculo necesita (radio)."
        radio = datos[0]
        return 3.14159 * (radio ** 2)

    elif figura == "triangulo":
        if len(datos) != 2:
            return "Error: un triángulo necesita (base, altura)."
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no reconocida."



# %%
# Ejecución n. 39

print(calcular_area("rectangulo", (3, 4)))
print(calcular_area("triangulo", (3, 4)))
print(calcular_area("pentagono", (3, 4)))

# %%
# 40. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea,
# después de aplicar un descuento. El programa debe hacer lo siguiente:

# 40.1 Solicita al usuario que ingrese el precio original de un artículo.

precio_original = float(input("Introduce el precio original del artículo: "))

# 40.2 Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).

tiene_cupon = input("¿Tienes un cupón de descuento? (si/no): ").lower()

# 40.3 Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.

if tiene_cupon == "sí" or tiene_cupon == "si":
    descuento = float(input("Introduce el valor del cupón de descuento: "))

    # 40.4 Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.

    if descuento > 0:
        precio_final = precio_original - descuento
    
        if precio_final < 0:
            precio_final = 0
    
    elif descuento == 0:
        print("El cupón no aplica descuento.")
        precio_final = precio_original

    else: 
        print("Cupón no válido (descuento negativo).")
        precio_final = precio_original

# el usuario no tiene cupón descuento
elif tiene_cupon =="no":    
    precio_final = precio_original 

# si hubise una respuesta inválida
else:
    print("Respuesta no válida. Se asume que no hay cupón.")
    precio_final = precio_original


# 40.5 Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.

print(f"El precio final de la compra es: {precio_final} €")

# 40.6 Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python

# %%
# Ejecución n. 40

# Caso 1
#   Precio original = 100€
#   Cupón descuento: SI
#   Valor descuento: 20€
#   Resultado: 
#       El precio final de la compra es: 80.0€

# Caso 2
#   Precio original = 100€
#   Cupón descuento: SI
#   Valor descuento: 0€
#   Resultado:
#       El cupón no aplica descuento.
#       El precio final de la compra es: 100.0€

# Caso 3
#   Precio original = 100€
#   Cupón descuento: No
#   Resultado:
#      El precio final de la compra es: 100.0€


