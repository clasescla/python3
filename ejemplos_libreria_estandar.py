# Nombre del script: ejemplos_libreria_estandar.py
# Propósito: ilustrar mediante ejemplos el uso de la librería estándar de Python
# Licencia: GPL v3 (www.gnu.org/licenses/gpl.html)

# HISTORIAL DE CAMBIOS
#
# Cuándo		Qué										Quién
# -----------	-------------------------------------	---------------------------------------	
# 14-Feb-2019   Versión inicial                         Gabriel Cánepa (Carrera Linux Argentina)
# 18-Feb-2019	Corrección sobre la función strftime	Gabriel Cánepa (Carrera Linux Argentina)	

# Introducción a la librería estándar: https://docs.python.org/3/tutorial/stdlib.html


#########################################################
# EJEMPLO 1 - Interfaz al sistema operativo: el módulo os
#########################################################

# Para ver la lista de funciones disponibles:
# import os
# dir(os)

# Para acceder a la documentación disponible de alguna función, system() por ejemplo:
# help(os.system)

import os

# Directorio actual
directorio_actual = os.getcwd()
print('El directorio actual es {}'.format(directorio_actual))

# Variables de entorno actuales
print(os.environ)

# Ver una variable en particular
directorio_personal = os.environ['HOME']
print(directorio_personal)

# Crear una lista con los contenidos del directorio actual
directorio_actual = os.listdir()
print(directorio_actual)

# Ver contenidos de /var
contenido_var = os.listdir('/var')
print(contenido_var)


#################################################################
# EJEMPLO 2 - Acceso a datos de la plataforma: el módulo platform
#################################################################

# Para ver la lista de funciones disponibles:
# import platform
# dir(platform)

# Para acceder a la documentación disponible de alguna función, machine() por ejemplo:
# help(platform.machine)

import platform

# Ver información de la distribución
distribucion = platform.linux_distribution()
print(distribucion)

# Mostrar información del sistema 
informacion_sistema = platform.uname()
print(informacion_sistema)


############################################################
# EJEMPLO 3 - Horas y fechas con formato: el módulo datetime
############################################################

# Para ver la lista de funciones disponibles:
# import datetime
# dir(datetime)

# Para acceder a la documentación disponible de alguna función, date.today() por ejemplo:
# help(datetime.date.today)

import datetime

# Mostrar fecha actual
# Si solamente se van a usar fechas (no horas), se puede importar solamente la función correspondiente

from datetime import date

# Mostrar la fecha actual en formato YYYY-MM-DD
hoy = date.today()
print(hoy)

# En formato DD/MM/YYYY
hoy = hoy.strftime('%d/%m/%Y')
print(hoy)
# Nota importante: en el video mencioné incorrectamente que strftime es un módulo. 
# En realidad, se trata de una función disponible al importar la función date del módulo datetime.

# Fecha dentro de 55 días
from datetime import timedelta
fecha_futura = date.today() + timedelta(days = 55)
print(fecha_futura)


#############################################################
# EJEMPLO 4 - Utilizar argumentos posicionales: el módulo sys
#############################################################

import sys

# Ver la lista de argumentos posicionales incluyendo el nombre del script
print(sys.argv)