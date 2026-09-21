from typing import List, Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models import Libro, Editorial

app = FastAPI(
    title="API REST Biblioteca - UNACH",
    description="API REST desarrollada con FastAPI para gestión y consulta de Libros y Editoriales. Taller de Desarrollo III.",
    version="1.0.0"
)

# -------------------------------------------------------------
# Instanciación de los 4 objetos de la clase Editorial
# -------------------------------------------------------------
editorial1 = Editorial(idEd=1, nombre="Editorial Planeta", pais="España")
editorial2 = Editorial(idEd=2, nombre="Fondo de Cultura Económica", pais="México")
editorial3 = Editorial(idEd=3, nombre="Penguin Random House", pais="Reino Unido")
editorial4 = Editorial(idEd=4, nombre="Alianza Editorial", pais="España")

editoriales_db = [editorial1, editorial2, editorial3, editorial4]

# -------------------------------------------------------------
# Instanciación de los 5 objetos de la clase Libro
# -------------------------------------------------------------
libro1 = Libro(
    ISBN="978-0307474728",
    titulo="Cien años de soledad",
    autor="Gabriel García Márquez",
    precio=299.50,
    idEd=1
)
libro2 = Libro(
    ISBN="978-9681601287",
    titulo="El llano en llamas",
    autor="Juan Rulfo",
    precio=185.00,
    idEd=2
)
libro3 = Libro(
    ISBN="978-8437604947",
    titulo="Rayuela",
    autor="Julio Cortázar",
    precio=320.00,
    idEd=1
)
libro4 = Libro(
    ISBN="978-8420685670",
    titulo="Don Quijote de la Mancha",
    autor="Miguel de Cervantes",
    precio=250.00,
    idEd=4
)
libro5 = Libro(
    ISBN="978-0142437230",
    titulo="Ficciones",
    autor="Jorge Luis Borges",
    precio=210.00,
    idEd=3
)

libros_db = [libro1, libro2, libro3, libro4, libro5]


# -------------------------------------------------------------
# Métodos GET principales (Requerimiento Funcional 2 y 3)
# -------------------------------------------------------------

@app.get("/", tags=["Inicio"])
async def root():
    """Ruta raíz de bienvenida e instrucciones de uso."""
    return {
        "mensaje": "Bienvenido a la API REST de Biblioteca - UNACH",
        "documentacion": "/docs",
        "endpoints_disponibles": {
            "consultar_libro_por_id_o_isbn": "/libros/{identificador}",
            "consultar_editorial_por_id": "/editoriales/{id_ed}",
            "listar_todos_los_libros": "/libros",
            "listar_todas_las_editoriales": "/editoriales"
        }
    }


@app.get("/libros/{identificador}", response_model=Libro, tags=["Libros"])
@app.get("/books/{identificador}", response_model=Libro, tags=["Libros"], include_in_schema=False)
async def obtener_libro(identificador: str):
    """
    Consulta un libro por su ID numérico (1 a 5) o por su código ISBN.
    Lanza una excepción HTTP 404 si el recurso no es encontrado.
    """
    # 1. Búsqueda si se envió como número entero (1, 2, 3, 4, 5)
    if identificador.isdigit():
        indice = int(identificador)
        if 1 <= indice <= len(libros_db):
            return libros_db[indice - 1]

    # 2. Búsqueda por ISBN
    for libro in libros_db:
        if libro.ISBN.lower() == identificador.strip().lower():
            return libro

    # 3. Manejo de excepción si no se encuentra
    raise HTTPException(
        status_code=404,
        detail="Libro no encontrado"
    )


@app.get("/editoriales/{id_ed}", response_model=Editorial, tags=["Editoriales"])
async def obtener_editorial(id_ed: int):
    """
    Consulta una editorial por su idEd numérico (1 a 4).
    Lanza una excepción HTTP 404 si el recurso no es encontrado.
    """
    for editorial in editoriales_db:
        if editorial.idEd == id_ed:
            return editorial

    # Manejo de excepción si no se encuentra
    raise HTTPException(
        status_code=404,
        detail="Editorial no encontrada"
    )


# -------------------------------------------------------------
# Métodos GET complementarios para listados completos
# -------------------------------------------------------------

@app.get("/libros", response_model=List[Libro], tags=["Libros"])
async def listar_libros():
    """Retorna la lista completa de los 5 libros registrados."""
    return libros_db


@app.get("/editoriales", response_model=List[Editorial], tags=["Editoriales"])
async def listar_editoriales():
    """Retorna la lista completa de las 4 editoriales registradas."""
    return editoriales_db
