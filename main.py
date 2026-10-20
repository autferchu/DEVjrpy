from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Inicializamos la aplicación
app = FastAPI(title="Mi Primera API Junior", version="1.0")


class CasoPrueba(BaseModel):
    id: int
    modulo: str
    estado: str


# Base de datos simulada en memoria (una lista de diccionarios)
base_datos_pruebas = [
    {"id": 1, "modulo": "Login", "estado": "Aprobado"},
    {"id": 2, "modulo": "Checkout", "estado": "Fallido"}
]


def convertir_caso(caso: CasoPrueba):
    if hasattr(caso, "model_dump"):
        return caso.model_dump()
    return caso.dict()


@app.get("/pruebas")
def obtener_pruebas():
    return {"total": len(base_datos_pruebas), "resultados": base_datos_pruebas}


@app.get("/pruebas/{id_caso}")
def obtener_prueba_por_id(id_caso: int):
    for prueba in base_datos_pruebas:
        if prueba["id"] == id_caso:
            return {"resultado": prueba}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Caso de prueba no encontrado"
    )


@app.post("/pruebas", status_code=status.HTTP_201_CREATED)
def crear_prueba(caso: CasoPrueba):
    if any(prueba["id"] == caso.id for prueba in base_datos_pruebas):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un caso de prueba con ese ID"
        )

    nuevo_caso = convertir_caso(caso)
    base_datos_pruebas.append(nuevo_caso)
    return {"mensaje": "Caso creado con éxito", "data": nuevo_caso}