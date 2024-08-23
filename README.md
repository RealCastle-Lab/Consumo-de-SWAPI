# Aplicación de Datos de Vacunación con Flask, Gunicorn y Nginx

## Descripción del Proyecto
Esta aplicación web proporciona acceso a datos históricos sobre la vacunación contra el sarampión en Panamá, destinada a niños entre 12-23 meses. La aplicación utiliza Flask como framework web, Gunicorn como servidor WSGI, Nginx como servidor web frontal y ahora incluye la funcionalidad de envío de correos electrónicos a través de Celery para tareas asíncronas.

## Características Principales
- **Interfaz Web**: Interactúa con los datos a través de una interfaz web intuitiva.
- **Consulta de Datos**: Visualiza y filtra los datos de vacunación por año.
- **Envío de Correos Electrónicos**: Envía correos electrónicos de manera asíncrona utilizando Celery y Flask-Mail.

## Tecnologías Utilizadas
- **Flask**: Framework web para construir la aplicación.
- **Jinja2**: Motor de plantillas para renderizar vistas HTML.
- **Gunicorn**: Servidor WSGI para manejar solicitudes HTTP.
- **Nginx**: Servidor web para servir contenido estático y actuar como proxy inverso.
- **Celery**: Framework para manejar tareas asíncronas y en segundo plano.
- **Flask-Mail**: Extensión para manejar el envío de correos electrónicos.
- **Redis**: Utilizado como broker de mensajes para Celery.

## Estructura del Proyecto
yourapp/ ├── app/ │ ├── init.py # Configuración inicial de Flask con Celery y Flask-Mail │ ├── celery.py # Configuración de Celery │ ├── routes.py # Rutas de la aplicación, incluyendo el envío de correos │ ├── templates/ # Plantillas Jinja2 para la interfaz de usuario │ └── static/ # Archivos estáticos (CSS, JS) ├── config/ │ ├── nginx/ # Configuración de Nginx │ └── systemd/ # Configuración del servicio systemd para Gunicorn ├── tests/ # Pruebas unitarias ├── requirements.txt # Dependencias ├── .gitignore # Archivos excluidos de Git └── README.md # Documentación del proyecto


## Instalación y Configuración

### Requisitos Previos
- Python 3.8+
- Redis
- Nginx
- Gunicorn

### Pasos de Instalación
1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd yourapp

   python3 -m venv venv
source venv/bin/activate


pip install -r requirements.txt


gunicorn --bind 0.0.0.0:8000 app:app

celery -A app.celery worker

