# API REST Biblioteca - UNACH

Implementación de una API REST con **FastAPI (Python)** y **Pydantic** desplegada en **Render**.
Práctica desarrollada para la materia de *Taller de Desarrollo III* (Facultad de Contaduría y Administración, Campus I - UNACH), a cargo del Dr. Christian Mauricio Castillo Estrada.

## 📋 Requerimientos Implementados

- **Modelos de datos (`models.py`)**:
  - Clase `Editorial`: `idEd`, `nombre`, `pais`.
  - Clase `Libro`: `ISBN`, `titulo`, `autor`, `precio`, `idEd`.
- **Datos iniciales (`main.py`)**:
  - 5 objetos instanciados de la clase `Libro`.
  - 4 objetos instanciados de la clase `Editorial`.
- **Métodos GET**:
  - `GET /libros/{identificador}`: Consulta un libro por número de ID (1 a 5) o por su código `ISBN`.
  - `GET /editoriales/{id_ed}`: Consulta una editorial por su identificador numérico (`idEd`).
  - `GET /libros`: Listado de todos los libros.
  - `GET /editoriales`: Listado de todas las editoriales.
  - `GET /`: Documentación de bienvenida y catálogo de endpoints.
- **Manejo de Excepciones**:
  - Respuestas HTTP `404 Not Found` en caso de solicitar libros o editoriales que no existan en la base de datos en memoria.

---

## 🚀 Ejecución Local

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Iniciar el servidor local:
   ```bash
   uvicorn main:app --reload
   ```

3. Abrir en el navegador:
   - API Docs interactiva (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Consultar libro 1: [http://127.0.0.1:8000/libros/1](http://127.0.0.1:8000/libros/1)
   - Consultar editorial 1: [http://127.0.0.1:8000/editoriales/1](http://127.0.0.1:8000/editoriales/1)
   - Probar error 404: [http://127.0.0.1:8000/libros/99](http://127.0.0.1:8000/libros/99)

---

## ☁️ Configuración para Despliegue en Render

- **Tipo de Servicio**: Web Service
- **Source Code**: Public Git Repository
- **Language**: Python 3
- **Branch**: main
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
