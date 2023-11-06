# Project-Olympiad
Olimpiada COPA 2023, TeamGreen4

1.- Clonar el repositorio:

$ git clone https://github.com/jhosua2388/Project-Olympiad.git

$ cd Project_Olympiad

2.- Instalar Python:
Visitar la página oficial python.org y encontraras con toda la documentación oficial (Guías para principiantes, guías de instalación, etc.) y también la sección de descargas que es lo que nos ocupa a nosotros en este momento.

    https://www.python.org/downloads/
    
    Version usado = Python 3.11.6
    https://www.python.org/downloads/release/python-3116/

3.- Verificar la instalación de Python:
Abrir la consola (CMD en Windows y tipear el comando "python"), con esto nos aseguraremos que Python a quedado bien instalado.
La respuesta esperada es : Python 3.11.6

4.- Configurar un entorno virtual:
Para crear un entorno virtual para su proyecto, abra un nuevo símbolo del sistema (CMD en Windows), navegue hasta la carpeta donde donde guardo el proyecto y luego ingrese lo siguiente:

    python3 -m venv Project-Olympiad

Esto creará una carpeta llamada "Project-Olympiad" si aún no existe y configurará el entorno virtual. Para activar el entorno, ejecute:

    Project-Olympiad\Scripts\activate

El entorno virtual se activará y verá "(Project-Olympiad)" junto al símbolo del sistema para designarlo. Cada vez que inicie un nuevo símbolo del sistema, deberá activar el entorno nuevamente para trabajar con ese proyecto.

5.- Instalar Django:
Django se puede instalar fácilmente usando pip dentro de su entorno virtual.
En el símbolo del sistema, asegúrese de que su entorno virtual esté activo y ejecute el siguiente comando:

    python3 -m pip install Django==4.2.6


6.- Instalar PostgreSql:

    6.1.- Descargar PostSql
    Descargar el instalador del programa de la página oficial https://www.postgresql.org/ en la menú descargar, elegir el instalador acuerdo a su sistema operativo (https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) con la versión 15.4
    
    6.2.- Intalar PostgreSql
    
    *Ejecutar el archivo descargado, dar siguiente a las ventanas.
    *Dejar por defecto los componentes
    *Ingresar como contraseña j18428128
    *Dejar por defecto el puerto de conexión 5432 y la configuración regional

7.- Crear base de dato en PostgreSql

    *Abrir el archivo pgAdmin 4 (PostgreSql)
    *Introducir la contraseña j18428128
    *Abrir las pestaña Servers>PostSQL 15>Databases
    *En Database, dar click derecho y crea una database con el nombre ong_proyecto

8.- Instalar Psycopg2
Se puede instalar fácilmente usando pip dentro de su entorno virtual activo.

    pip install psycopg2-binary

9.- Desplegar la base de datos
Ingresar el siguiente comando para desplegar la base de datos hacia PostgreSql

    python manage.py migrate

10.- Crear Superusuario
En la línea de comandos, escribe el siguiente codigo y pulsa enter

    python manage.py createsuperuser
    
Cuando te lo pida, escribe tu nombre de usuario (en minúscula, sin espacios), email y contraseña.

    Ejemplo.
    Username: ejemplo
    Email address: ejemplo@example.com
    Password: 1234
    Password (again): 1234

11.- Levantar el servidor Django
En la línea de comandos, escribe el siguiente codigo y pulsa enter

    python manage.py runserver
    
Ingresar a la ip suministrada

    Ejemplo.
    http://127.0.0.1:8000/


