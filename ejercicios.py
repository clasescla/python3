# Nombre del script: ejercicios.py
# Propósito: practicar temas tratados durante el desarrollo del curso de scripting con Python 3
# Licencia: GPL v3 (www.gnu.org/licenses/gpl.html)

# HISTORIAL DE CAMBIOS
#
# Cuándo		Qué										Quién
# -----------	-------------------------------------	---------------------------------------	
# 27-Feb-2019   Versión inicial                         Gabriel Cánepa (Carrera Linux Argentina)


#############################################
# EJERCICIO 1 - Tipos de datos y conversiones
#############################################

# Para este ejercicio podemos pasarle a la función type() datos ingresados manualmente o que resulten de la ejecución de otra función.

# ¿A qué tipo de dato corresponden las siguientes variables?

a = '2'
b = 'Hoy es un día soleado'
c = 2
d = [1, 2, 3, 4, 5]
e = (1, 2, 3, 4, 5)
f = True
g = False
h = None
jugador = {'nombre': 'Fulano', 'apellido': 'De tal', 'camiseta': 15, 'en_actividad': True}
autos = [{'marca': 'Ford', 'modelo': 2005, 'registra_deuda': False}, {'marca': 'Peugeot', 'modelo': 2010, 'registra_deuda': True}]


############################################
# EJERCICIO 2 - Acceder a la ayuda de Python
############################################

# ¿Qué función disponible para las cadenas de texto (str) permite cambiar una oración a mayúscula?

# Por ejemplo, teniendo el mensaje 'mi nombre es Mengano' se necesita convertirlo en 'MI NOMBRE ES MENGANO'

nombre = 'mi nombre es Mengano'


######################################
# EJERCICIO 3 - Operadores aritméticos
######################################

# Dadas las siguientes variables, realizar las operaciones que se indican y guardar el resultado en una variable separada

numero1 = 35
numero2 = 13.3

# Suma de ambos números


# Resta de numero1 menos numero2


# División entera de numero1 por numero2 y convertir el resultado a entero


# División con punto flotante de numero1 por numero2 redondeada a dos digitos decimales


# Multiplicación de ambos números


##################################
# EJERCICIO 4 - Operadores lógicos
##################################

# Utilizar los operadores lógicos and, not, y or para crear una expresión que utilice las siguientes variables y devuelva True

booleano1 = True
booleano2 = False
booleano3 = True


#####################################################
# EJERCICIO 5 - Uso de la librería estándar de Python
#####################################################

# Importar un módulo completo e ilustrar el uso de una función cualquiera disponible en el mismo


# De un módulo cualquiera, importar una sola función y utilizarla para generar un resultado que se guarde en una variable


#######################################################################
# EJERCICIO 6 - Búsquedas en el índice de paquetes de Python (pypi.org)
#######################################################################

# Buscar algún paquete que se utilice para reducir el tamaño de imágenes, instalarlo con pip y utilizarlo


################################
# EJERCICIO 7 - Control de flujo
################################

# Utilizar la función input() para pedir al usuario que ingrese un punto de montaje y guardarlo en la variable sistema_archivos:

sistema_archivos = input('Ingrese un sistema de archivos: ')

# Importar el módulo recursos.py y emplear la función uso_almacenamiento para obtener el porcentaje de uso del sistema de archivos en cuestión. 
# Nota: al importar un módulo representado por un archivo con la extensión .py, solamente se utiliza el nombre del archivo en la importación.

# Si el porcentaje de uso...
# ... está por debajo de 40, mostrar el mensaje 'Todo está bien'.
# ... es mayor o igual que 40 y menor que 75, mostrar el mensaje 'Hay que tener cuidado'
# ... es mayor o igual que 75, mostrar el mensaje 'Pronto te puedes quedar sin espacio'


########################################################
# EJERCICIO 8 - Tipos de errores y manejo de excepciones
########################################################

# Identificar al menos un tipo de error que puede suceder durante la ejecución del ejercicio anterior y agregar los bloques try, except, y finally para controlarlo.


############################
# EJERCICIO 9 - El bucle for
############################

# Iterar sobre la siguiente lista, multiplicar cada número por sí mismo, y agregar cada resultado en la lista llamada cuadrados (vacía inicialmente)

numeros = [1, 3, 5, 7, 9]
cuadrados = []


#####################################################
# EJERCICIO 10 - Desarrollo de funciones (1era parte)
#####################################################

# Escribir un módulo llamado estadisticas_simples.py y desarrollar tres funciones llamadas promedio, mediana, y moda.
# Al pasarle una lista de números a cada función, debe devolver el valor promedio, la mediana, y la moda.
# Repaso del significado de estas medidas estadísticas: https://www.varsitytutors.com/hotmath/hotmath_help/spanish/topics/mean-median-mode
# Aclaración: Si bien existe un módulo que devuelve las medidas mencionadas (statistics), este ejercicio puede considerarse como integrador del curso en su totalidad.
# Para estar correctamente resuelto, este ejercicio no debe importar ningún módulo externo, aunque sí se permite emplear funciones incorporadas existentes (sum(), por ejemplo).
# Ayuda: consultar en la ayuda de Python las funciones disponibles para las listas.


####################################################
# EJERCICIO 11 - Desarrollo de funciones (2da parte)
####################################################

# Implementar las funciones llenar_tabla y dar_formato en el archivo informe_sistema.py según se indica en este.