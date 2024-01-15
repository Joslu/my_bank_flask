# Información del Proyecto - Backend 🐍

## Descripción
Este proyecto backend está desarrollado utilizando Flask, un marco de trabajo de Python para la construcción de aplicaciones web. La lógica del servidor proporciona endpoints API para la comunicación con el frontend y maneja la persistencia de datos utilizando SQLite como base de datos.

## Estructura del Proyecto
El backend sigue una estructura organizada en varias carpetas y archivos:

- **`database`:** Contiene la lógica relacionada con la base de datos, como la creación de tablas y la manipulación de datos.
- **`venv`:** Entorno virtual para gestionar las dependencias del proyecto.
- **`main.py`:** Archivo principal que inicia la aplicación Flask y define las rutas y la lógica del servidor.
- **`model.py`:** Archivo que define la estructura de la base de datos utilizando SQLAlchemy u otra biblioteca ORM.
- **`requirements.txt`:** Archivo que lista las dependencias del proyecto.

## Tecnologías Utilizadas
- **Framework:** Flask (Python) 🐍
- **Base de Datos:** SQLite 🗃️
- **ORM:** SQLAlchemy (Posiblemente, según la implementación)
- **Servidor Web:** Nginx 🚀
- **Instancia AWS EC2:** t2.micro (Ubuntu) ☁️

## Funcionalidades Principales
- **Registro y Autenticación:** Implementa rutas y controladores para el registro y autenticación de usuarios.
- **Operaciones CRUD:** Proporciona endpoints para realizar operaciones de crear, leer, actualizar y eliminar.
- **Integración con Belvo:** Consumimos información de Belvo para proporcionar datos financieros a los usuarios.

## Instalación y Ejecución
1. Clona el repositorio: `git clone [URL del Repositorio]`
2. Crea y activa un entorno virtual: `python -m venv venv` y `source venv/bin/activate` (o `venv\Scripts\activate` en Windows)
3. Instala las dependencias: `pip install -r requirements.txt`
4. Ejecuta el servidor Flask: `python main.py`
5. Accede a la aplicación en tu navegador: [http://localhost:5000](http://localhost:5000)

# Despliegue en AWS E2C 

Este proyecto ha sido desplegado en E2C para su implementación en un entorno de producción. A continuación se detallan los pasos necesarios para replicar el despliegue:
