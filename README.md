# api_server

API REST desarrollada con FastAPI que permite ejecutar comandos Linux de forma segura mediante autenticación real del sistema usando Pluggable Authentication Modules (PAM). Implementa validación de parámetros, allowlist de comandos y ejecución controlada con subprocess para prevenir inyección y abusos.

## Linux Command Executor API

API desarrollada con FastAPI que permite ejecutar comandos específicos del sistema Linux mediante peticiones HTTP, utilizando autenticación del sistema operativo a través de Pluggable Authentication Modules (PAM).

El objetivo es exponer de forma controlada ciertos comandos del sistema, evitando inyección de comandos y garantizando seguridad mediante una lista blanca de comandos permitidos.

## Características

- Autenticación usando usuarios reales de Linux.
- Ejecución controlada de comandos del sistema.
- Validación de parámetros para evitar inyección
- Lista blanca de comandos permitidos.
- Arquitectura modular
- Manejo de errores y timeout de procesos

## Tecnologías utilizadas

- Python 3
- FastAPI
- Uvicorn
- PAM (autenticación Linux)
- Subprocess (ejecución de comandos)

## Estructura del proyecto

app/
│
├── main.py
│
├── config/
│ └── settings.py
│
├── routes/
│ └── system.py
│
├── security/
│ └── auth.py
│
├── services/
│ └── command_executor.py
│
└── validators/
└── param_validator.py

## Descripción de módulos

### main.py

Es el punto de entrada de la aplicación.
Se encarga de inicializar la aplicación web, registrar las rutas disponibles y preparar el servidor para recibir solicitudes.

### config/settings.py

Contiene las configuraciones del sistema.
En este módulo se define la lista de comandos permitidos que la API puede ejecutar.
Esto permite centralizar configuraciones y facilita modificaciones futuras.

### routes/system.py

Define los endpoints de la API.
Su responsabilidad principal es recibir las solicitudes HTTP, coordinar la ejecución de los módulos necesarios (autenticación, validación y ejecución del comando) y construir la respuesta final que será enviada al cliente.

### security/auth.py

Gestiona el proceso de autenticación de los usuarios.
Utiliza el sistema de autenticación del sistema operativo Linux para verificar que las credenciales proporcionadas por el cliente correspondan a un usuario válido del sistema.

### validators/param_validator.py

Se encarga de validar los parámetros enviados en las solicitudes.
Este módulo aplica reglas de validación para asegurar que los parámetros sean seguros y evitar posibles intentos de inyección de comandos.

### services/command_executor.py

Contiene la lógica encargada de ejecutar los comandos del sistema.
Este módulo verifica que el comando solicitado esté permitido y luego ejecuta el proceso correspondiente, capturando su salida y estado de ejecución.
