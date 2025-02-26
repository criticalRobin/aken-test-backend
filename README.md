# Instrucciones para Configurar y Ejecutar el Proyecto

## Backend (Django)

1. Clona el repositorio: `git clone https://github.com/tuusuario/turepositorio.git` y luego `cd turepositorio`.
2. Crea y activa un entorno virtual: `python -m venv venv` y `source venv/bin/activate` (en Windows: `venv\Scripts\activate`).
3. Instala las dependencias: `pip install -r requirements.txt`.
4. Aplica las migraciones: `python manage.py migrate`.
5. Ejecuta el servidor de desarrollo: `python manage.py runserver`. El backend estará en `http://127.0.0.1:8000/`.

## Frontend (Angular)

1. Navega al directorio del frontend: `cd frontend`.
2. Instala las dependencias: `npm install`.
3. Ejecuta el servidor de desarrollo: `ng serve`. El frontend estará en `http://localhost:4200/`.

## Uso

- **Endpoint del backend**: `http://127.0.0.1:8000/api/news/`.
- **Frontend**: Accede a `http://localhost:4200/` para ver la noticia.
