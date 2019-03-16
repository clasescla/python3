# Scripting con Python 3 para sysadmins GNU/Linux

Este curso está dirigido a Administradores de Sistemas GNU/Linux que deseen aprender a utilizar Python 3, uno de los lenguajes de programación más utilizados, como lenguaje de scripting.

Aprender Python es conveniente para un programador por su multiplicidad de usos. Entre otros, es una poderosa herramienta para escribir scripts, crear una aplicación web y abrir puertas al apasionante campo de Data Science y Machine Learning.

Se aconseja referirse a la documentación de Python en línea para profundizar estos conceptos, así como para aprender otros que por cuestiones de brevedad y de alcance no forman parte de este curso:

- [Página oficial de Python](https://www.python.org/)
- [Documentación](https://docs.python.org/3/) de la última versión disponible
- [Tutorial](https://docs.python.org/3/tutorial/index.html)

## Material de lectura

En los siguientes posts del [blog](https://blog.carreralinux.com.ar) de Carrera Linux Argentina (CLA), el tutor Gabriel Cánepa explica en detalle los temas del curso, con excepción de las últimas dos secciones donde se genera el informe del sistema y se detalla el uso de git y GitHub.

Aunque en el curso utilizamos la consola de Python para probar código de forma rápida, también podemos instalar un IDE (_Integrated Development Environment_) para hacerlo desde un entorno gráfico. Esta herramienta permite la ejecución de código y la creación de archivos **.py**.

- [Instalar un IDE para Python en Linux para comenzar a programar] (https://blog.carreralinux.com.ar/2017/04/instalar-un-ide-para-python-comenzar-programar/)
- [Ejecutar programas Python desde fuera del IDLE](https://blog.carreralinux.com.ar/2017/06/ejecutar-programas-python-fuera-idle/)

> La versión de Python 3 que se encuentra disponible en los repositorios de Debian es suficiente para el curso, también podemos [actualizar a una versión más reciente](https://blog.carreralinux.com.ar/2018/04/python-3-en-linux-version-mas-reciente/) si lo deseamos. Esto nos permitirá acceder a nueva funcionalidad disponible en la misma.

### Operaciones simples y conversiones

- [Operaciones matemáticas con Python utilizando el IDLE](https://blog.carreralinux.com.ar/2017/04/operaciones-matematicas-con-python-idle/)
- [Conversión de tipos de datos en Python utilizando funciones nativas](https://blog.carreralinux.com.ar/2017/04/conversion-de-tipos-de-datos-en-python/)
- [Uso de distintos tipos de datos en Python de manera conjunta](https://blog.carreralinux.com.ar/2017/04/uso-de-distintos-tipos-de-datos-en-python/)

### Control de flujo y bucles

- [Control de flujo en Python mediante operadores lógicos y de comparación](https://blog.carreralinux.com.ar/2017/04/control-de-flujo-en-python-operadores-logicos/)
- [Ejemplos del uso de condicionales en Python: if, elif, y else](https://blog.carreralinux.com.ar/2017/05/ejemplos-del-uso-de-condicionales-en-python/)
- [Uso del bucle while en Python: concepto y ejemplos](https://blog.carreralinux.com.ar/2017/05/uso-del-bucle-while-en-python-concepto-ejemplos/)
- [Ejecución del bucle while en Python: uso de continue y break](https://blog.carreralinux.com.ar/2017/05/ejecucion-del-bucle-while-en-python-continue-break/)
- [Uso del bucle for en Python: introducción y ejemplos](https://blog.carreralinux.com.ar/2017/05/uso-del-bucle-for-en-python/)

### Listas

- [Listas en Python: las estructuras de datos más utilizadas](https://blog.carreralinux.com.ar/2017/05/listas-en-python-estructuras-de-datos/)
- [Ejemplos del uso de listas en Python: operaciones adicionales](https://blog.carreralinux.com.ar/2017/05/ejemplos-del-uso-de-listas-en-python/)
- [Similitudes entre strings y las listas en Python](https://blog.carreralinux.com.ar/2017/06/similitudes-entre-strings-y-las-listas-python/)
- [Diferencias entre listas y strings en Python](https://blog.carreralinux.com.ar/2017/06/diferencias-entre-listas-y-strings-python/)
- [Prácticas en Python: uso de condicionales, bucles, y listas](https://blog.carreralinux.com.ar/2017/05/practicas-en-python/)

### La librería estándar

- [Funciones de la librería estándar de Python: cómo utilizarlas](https://blog.carreralinux.com.ar/2017/06/funciones-de-la-libreria-estandar-de-python/)
- [Más ejemplos del uso de la librería estándar](https://blog.carreralinux.com.ar/2017/06/la-libreria-estandar-de-python-ejemplos/)

### Creación de funciones

- [Crear funciones en Python: nuestro primer programa](https://blog.carreralinux.com.ar/2017/06/crear-funciones-en-python/)
- [Try y except en Python: capturando errores](https://blog.carreralinux.com.ar/2017/06/try-y-except-en-python-excepciones/)

### Diccionarios

- [Diccionarios en Python: otra estructura de datos](https://blog.carreralinux.com.ar/2017/06/diccionarios-en-python/)
- [Llaves en diccionarios: get y setdefault](https://blog.carreralinux.com.ar/2017/06/llaves-en-diccionarios-get-setdefault/)
- [Uso de diccionarios en Python: ejemplo](https://blog.carreralinux.com.ar/2017/06/uso-de-diccionarios-en-python-ejemplos/)
- [Conteo y orden con Python: diccionarios al rescate](https://blog.carreralinux.com.ar/2017/07/conteo-y-orden-con-python-diccionarios/)

### Manipulación de cadenas de texto y números enteros

- [Métodos de strings en Python mediante ejemplos](https://blog.carreralinux.com.ar/2017/07/metodos-de-strings-python/)
- [Uso de las funciones split y join en Python](https://blog.carreralinux.com.ar/2017/07/uso-split-y-join-python/)
- [Manipular strings con Python: más ejemplos](https://blog.carreralinux.com.ar/2017/07/manipular-strings-con-python-ejemplos/)
- [Formato de strings en Python](https://blog.carreralinux.com.ar/2017/07/formato-de-strings-python/)
- [La función format en Python: ejemplos](https://blog.carreralinux.com.ar/2017/07/la-funcion-format-python-ejemplos/)
- [Formato de enteros en Python](https://blog.carreralinux.com.ar/2017/07/formato-de-enteros-python/)

### Lectura de archivos de configuración

- [Archivos de configuración: acceso desde Python](https://blog.carreralinux.com.ar/2017/09/archivos-de-configuracion-acceso-desde-python/)
- [El módulo configparser: leer archivos .ini](https://blog.carreralinux.com.ar/2017/09/el-modulo-configparser-leer-archivos-ini/)
