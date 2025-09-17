from pydantic import BaseModel
from typing import Optional

class InventarioActivoBase(BaseModel):
    NOMBRE_DEL_ACTIVO: Optional[str] = None
    DESCRIPCION: Optional[str] = None
    TIPO_DE_ACTIVO: Optional[str] = None
    MEDIO_DE_CONSERVACIÓN: Optional[str] = None
    FORMATO: Optional[str] = None
    IDIOMA: Optional[str] = None
    PROCESO: Optional[str] = None
    DUEÑO_DE_ACTIVO: Optional[str] = None
    TIPO_DE_DATOS_PERSONALES: Optional[str] = None
    FINALIDAD_DE_LA_RECOLECCIÓN: Optional[str] = None
    CONFIDENCIALIDAD: Optional[str] = None
    INTEGRIDAD: Optional[str] = None
    DISPONIBILIDAD: Optional[str] = None
    CRITICIDAD_TOTAL_DEL_ACTIVO: Optional[str] = None
    INFORMACIÓN_PUBLICADA_O_DISPONIBLE: Optional[str] = None
    LUGAR_DE_CONSULTA: Optional[str] = None

class InventarioActivoCreate(InventarioActivoBase):
    pass

class InventarioActivoUpdate(InventarioActivoBase):
    pass

class InventarioActivoOut(InventarioActivoBase):
    id: int

    class Config:
        orm_mode = True
