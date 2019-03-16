# Nombre del módulo: recursos.py
# Propósito: mostrar uso de recursos del sistema
# Licencia: GPL v3 (www.gnu.org/licenses/gpl.html)

# HISTORIAL DE CAMBIOS
#
# Cuándo		Qué										Quién
# -----------	-------------------------------------	---------------------------------------	
# 16-Feb-2019   Versión inicial                         Gabriel Cánepa (Carrera Linux Argentina)

# NOTA IMPORTANTE: En este módulo utilizamos diccionarios como tipo de datos de salida por simplicidad.
# Luego de profundizar en el uso de Python, es recomendable cambiar esto y utilizar tuplas con nombre.

import psutil

def uso_almacenamiento(disco = None):
	'''
	Devuelve un diccionario con el uso del disco indicado, 
	o una lista de diccionarios con todos los sistemas de 
	archivos si no se indica ningún argumento
	'''
	if not disco:
		discos = [elemento.mountpoint for elemento in psutil.disk_partitions()]
		info_discos = []
		for disco in discos:
			info_disco = psutil.disk_usage(disco)
			uso_disco = info_disco.percent
			info_discos.append({disco: uso_disco})
		return info_discos
	else:
		info_disco = psutil.disk_usage(disco)
		return {disco: info_disco.percent}
		
		
def uso_memoria():
	'''
	Devuelve un número de punto flotante que indica el porcentaje 
	de utilización actual de memoria
	'''
	return psutil.virtual_memory().percent
	
def uso_cpus():
	'''
	Devuelve un diccionario con la cantidad de CPUs y el uso actual
	'''
	return {'cantidad_cpus': psutil.cpu_count(), 'uso_cpu': psutil.cpu_percent()}
