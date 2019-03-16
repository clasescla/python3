# Nombre del script: ventajas_ejemplo.py
# Propósito: ilustrar mediante ejemplos algunas ventajas de Python 3 sobre Bash como lenguaje de scripting
# Licencia: GPL v3 (www.gnu.org/licenses/gpl.html)

# HISTORIAL DE CAMBIOS
#
# Cuándo		Qué										Quién
# -----------	-------------------------------------	---------------------------------------	
# 09-Feb-2019   Versión inicial                         Gabriel Cánepa (Carrera Linux Argentina)


###################################################################################################
# EJEMPLO 1 - Obtener el nombre del equipo y subrayarlo con la cantidad de guiones que correspondan
###################################################################################################

# Por ejemplo, si el nombre del equipo es cenicienta:
# cenicienta
# ----------

import platform
nombre_equipo = platform.uname().node
print(nombre_equipo)
print('-' * len(nombre_equipo))

# Para hacer lo mismo con Bash:
# NOMBRE_EQUIPO=$(hostname)
# echo $NOMBRE_EQUIPO
# echo $(yes - | head -${#NOMBRE_EQUIPO}) | tr -d ' '


####################################################################################
# EJEMPLO 2 - Mostrar los sistemas de archivos cuyo uso supera un umbral establecido
####################################################################################

# Por ejemplo, indicar el punto de montaje y el porcentaje de uso si es mayor a 40%:
# /home: 55%

import shutil
sistemas_de_archivos = ['/var', '/tmp', '/home', '/']
for sistema_de_archivos in sistemas_de_archivos:
	info = shutil.disk_usage(sistema_de_archivos)
	uso = round (info.used * 100 / info.total, 2)
	if uso > 40:
		print('{}: {}'.format(sistema_de_archivos, uso))

# Para hacer algo parecido con Bash:
# for SISTEMA_DE_ARCHIVOS in /home /var /tmp /; 
# do 
#  	INFO=$(df -h -t ext4 $SISTEMA_DE_ARCHIVOS | sed '1d' | awk '{ print $6 " " $5 }')
#	USO=$(echo $INFO | awk '{ print $2 }' | cut -d'%' -f1)	
#	if [ $USO -ge 40 ];
#	then
#		echo $INFO
#	fi
# done


############################################################################
# EJEMPLO 3 - Leer archivos de configuración y utilizar valores de variables
############################################################################

# Por ejemplo, si el archivo config.txt tiene las siguientes [SECCIONES] y contenido:
# [SERVIDOR]
# url_base_api = https://www.misitio.com.ar
# produccion = /produccion/v1
# 
# [DATOS_CLIENTE]
# nombre = /cla
# mes = /febrero

# Podemos acceder a las secciones y variables de la siguiente manera con Python:

import configparser
config = configparser.ConfigParser()
config.read('config.txt')
print('{}{}{}{}'.format(config['SERVIDOR']['url_base_api'], 
						config['SERVIDOR']['produccion'], 
						config['DATOS_CLIENTE']['nombre'], 
						config['DATOS_CLIENTE']['mes']))