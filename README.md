# Python Logger v1.0 final
![Logs de ejemplo](https://i.ibb.co/j5KzTds/sample-log.png, "Algunos ejemplos de logs")

### Descripción
Se trata de un logger que, además de mostrar por consola las notificaciones, registra los eventos en un archivo de texto de forma automática.

#### Finalidad
Facilitar el proceso de creación de logs para nuevas aplicaciones.

#### Beneficios de usar esta librería
Solo necesitas configurar unas pocas variables para tener listo un eficiente, complejo y completo logger en tu aplicación o script de Python en unos minutos.

### Requisitos
- Python -> 3+
- Colorify -> 1.1.0

### Sistema Operativo
Detecta si estás empleando un sistema Linux o Windows y utiliza los formatos de línea de ambos sistemas.

### Instalación
Descargar el archivo _logger.py_ dentro de tu proyecto.

Instalar el paquete _colorify_ desde pip:
```
pip install colorify
```

### Forma de uso
En el/los archivos que quieras ejecutar el proceso de logging, debes incluir en la parte superior:
```
import logger
```

Tras todas las declaraciones pertinentes, deberás instanciar un nuevo objeto de la clase logger de la siguiente manera:
```
obj_logger = Logger('nombre_identificador')
```

El formato de fecha por defecto es: **DD/MM/AAAA hh:mm:ss**
Ejemplo: **12/07/2021 09:55:32**

Puedes modificarlo desde la propia clase editando el parámetro:
```
self.datetime_format = '%d/%m/%Y %H:%M:%S'
```

O bien, tras instanciar el objeto de la clase _Logger_, puedes emplear el método _set_datetime_format()_ aplicando un formato personalizado:
```
nuevo_formato = '%H:%M:%S.%f %d-%m-%Y'
obj_logger.set_datetime_format(nuevo_formato)
```

### Modificar el formato de logging
Puedes modificar el formato propuesto por defecto a tu antojo, según las necesidades de tu aplicación, editando la propiedad _self.string_format_ inicializada al principio de la clase.

![Ejemplo de formato de registros](https://i.ibb.co/c89MyFz/sample-log5.png, "Ejemplo de formato de registros")

Los parámetros disponibles son:
-- %DATETIME%
-- %THREAD%
-- %USERNAME%
-- %CATEGORY%
-- %MESSAGE%
> NOTA: Se puede usar cualquier carácter como separador, excepto, el símbolo de porcentaje %

### Logging de eventos
Una vez instanciada la clase, se lanzan nuevos registros como cualquier logger.
> info() | exception() | error() | warning() | critical()

Sistema de identificación de usuarios
> Puedes añadir además el nombre de usuario que esté ejecutando la aplicación para identificar más fácilmente los errores o el uso de la aplicación por parte de los usuarios.

```
obj_logger.info('Mensaje de tipo informativo de ejemplo')
obj_logger.exception('Error de ejecución en el metodo modificar_persona() de la clase Persona()', username='johnsmith')
obj_logger.exception('Error de ejecución en el metodo modificar_persona() de la clase Persona()', 'johnsmith')
```
![Ejemplo de logging con usuarios](https://i.ibb.co/6FVqxBs/sample-log2.png, "Ejemplo de logging con usuarios")

### Logging con multithreading
Se ha implementado una opción para el caso de ser una aplicación compleja con hilos múltiples.

> Al hacer la llamada al objeto logger, debes añadir el parámetro _thread='identificadorDelHilo'_ para identificar más claramente el evento registrado.
> Además, en la configuración del logger deberás solicitud que muestre el parámetro con _%THREAD%_

![Ejemplo de logging con multithreading](https://i.ibb.co/6vSS0KB/sample-log3.png, "Ejemplo de logging con varios hilos")

### Personalización de las rutas y los ficheros
Existen diferentes métodos que podemos modificar para personalizar el proceso de logging.

> get_logs_path

- Determina la ruta dónde se guardaran los diferentes logs.
- Por defecto, se creará una carpeta llamada _**logs**_ en el mismo directorio donde se ejecute el archivo que instancia el logger y dentro de la misma, una carpeta con el nombre identificativo que se utilizó al declarar el objeto.
- Ejemplo:
-- obj_logger = Logger('my_bot_name')
-- Ruta donde se guardarán los logs = ./logs/my_bot_name/

> get_filename()

- Determina el nombre por el cual se identificarán los logs.
- Cada inicio de semana, es decir, cada Lunes, se creará un nuevo archivo de registro.
- En caso de que se empiece a ejecutar un día distinto del Lunes, o que se borre el archivo de registro en uso, la fecha que se empleará será el del Lunes de la semana en curso.
- Por defecto, el formato por el que se emplearán los nuevos registros será:
-- <nombre_identificativo>_DIAMESAÑO.log
-- appName_12072021.log
- Al iniciar el proceso, comprobará que el archivo exista y, en caso de que no, lo creará.
-- **Para evitar errores de ejecución,** siempre que vaya a escribir en el archivo comprobará que éste exista.

> create_new_log()

- Puedes modificar la cabecera del archivo de registro a tu gusto.
- La cabecera será la misma para todos los logs que cree la aplicación, aunque puedes añadirle contenido dinámico, como por ejemplo, por defecto varia la fecha cada semana.

### Personalización de colores
Puedes modificar la configuración de colores por defecto que hemos propuesto para mostrar los diferentes eventos.

![Personalización de colores](https://i.ibb.co/4jzFmrG/sample-log4.png, "Personalización de la paleta de colores")
- Dispones de toda la gama cromática que ofrece colorify desde la documentación oficial.
-- [Enlace a la documentación oficial de colorify](https://pypi.org/project/colorify/)

> NOTA: Para cambiar un color, DEBES usar la nomenclatura definida por el objeto **colorify**
> Es decir, para usar el color gris deberás escribir C.gray
> Para el color verde: C.green
