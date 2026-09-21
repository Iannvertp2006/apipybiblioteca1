from pydantic import BaseModel, Field

class Editorial(BaseModel):
    idEd: int = Field(..., ge=1, description="Identificador único de la editorial")
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre de la editorial")
    pais: str = Field(..., min_length=1, max_length=50, description="País de la editorial")

    # Métodos POO (Getters / Setters tradicionales de apoyo)
    def get_idEd(self) -> int:
        return self.idEd

    def get_nombre(self) -> str:
        return self.nombre

    def get_pais(self) -> str:
        return self.pais


class Libro(BaseModel):
    ISBN: str = Field(..., min_length=5, max_length=25, description="Número estándar internacional del libro")
    titulo: str = Field(..., min_length=1, max_length=150, description="Título del libro")
    autor: str = Field(..., min_length=1, max_length=100, description="Autor del libro")
    precio: float = Field(..., gt=0, description="Precio del libro en formato decimal")
    idEd: int = Field(..., ge=1, description="Clave foránea / Identificador de la editorial que lo publica")

    # Métodos POO (Getters / Setters tradicionales de apoyo)
    def get_isbn(self) -> str:
        return self.ISBN

    def get_titulo(self) -> str:
        return self.titulo

    def get_autor(self) -> str:
        return self.autor

    def get_precio(self) -> float:
        return self.precio

    def get_idEd(self) -> int:
        return self.idEd
