Aplicación web enfocada en mobile-first que permite visualizar en un mapa interactivo el estado operativo de los ascensores de Valparaíso, calcular distancias hacia ellos y permitir a la comunidad reportar problemas de accesibilidad.
Requisitos Previos
Python 3.x
pip (Gestor de paquetes de Python)
Instrucciones de Instalación
Clonar el repositorio: git clone https://github.com/Blackzama/proyecto-grupo-15-aplicacion-red-ascensores.git cd proyecto-grupo-15-aplicacion-red-ascensores
Crear y activar un entorno virtual:
 En Windows: python -m venv venv 
.- venv\Scripts\activate
En Mac/Linux: python3 -m venv venv 
.- source venv/bin/activate
Instalar las dependencias: pip install django
Pasos para iniciar Django
Aplica las migraciones para inicializar la base de datos: 
python manage.py migrate
python manage.py makemigrations
Inicia el servidor de desarrollo: python manage.py runserver
Abre tu navegador e ingresa a: http://127.0.0.1:8000/
Datos para probar la funcionalidad principal (Corazón de la App)
Permisos de Ubicación: Al abrir la aplicación web, el navegador solicitará acceso a tu ubicación. Debes aceptarlo para que el mapa trace y calcule tu distancia exacta a los ascensores.
