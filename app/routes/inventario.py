from fastapi import APIRouter, Depends, HTTPException
import logging
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import SessionLocal


# Configuración del logger
logger = logging.getLogger("inventario_api")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(handler)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import SessionLocal
import logging

# Configuración del logger
logger = logging.getLogger("inventario_api")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(handler)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/inventario/", response_model=List[schemas.InventarioActivoOut])
def read_inventario_activos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return crud.get_inventario_activos(db, skip=skip, limit=limit)
    except Exception as e:
        logger.error(f"Error al obtener activos: {e}")
        raise HTTPException(status_code=500, detail="Error interno al obtener activos")

@router.get("/inventario/{activo_id}", response_model=schemas.InventarioActivoOut)
def read_inventario_activo(activo_id: int, db: Session = Depends(get_db)):
    try:
        db_activo = crud.get_inventario_activo(db, activo_id)
        if db_activo is None:
            logger.warning(f"Activo con id {activo_id} no encontrado")
            raise HTTPException(status_code=404, detail="Activo no encontrado")
        return db_activo
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error al obtener activo {activo_id}: {e}")
        raise HTTPException(status_code=500, detail="Error interno al obtener activo")

@router.post("/inventario/", response_model=schemas.InventarioActivoOut)
def create_inventario_activo(activo: schemas.InventarioActivoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_inventario_activo(db, activo)
    except Exception as e:
        logger.error(f"Error al crear activo: {e}")
        raise HTTPException(status_code=500, detail="Error interno al crear activo")

@router.put("/inventario/{activo_id}", response_model=schemas.InventarioActivoOut)
def update_inventario_activo(activo_id: int, activo: schemas.InventarioActivoUpdate, db: Session = Depends(get_db)):
    try:
        db_activo = crud.update_inventario_activo(db, activo_id, activo)
        if db_activo is None:
            logger.warning(f"Intento de actualizar activo no existente: {activo_id}")
            raise HTTPException(status_code=404, detail="Activo no encontrado")
        return db_activo
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error al actualizar activo {activo_id}: {e}")
        raise HTTPException(status_code=500, detail="Error interno al actualizar activo")

@router.delete("/inventario/{activo_id}", response_model=schemas.InventarioActivoOut)
def delete_inventario_activo(activo_id: int, db: Session = Depends(get_db)):
    try:
        db_activo = crud.delete_inventario_activo(db, activo_id)
        if db_activo is None:
            logger.warning(f"Intento de eliminar activo no existente: {activo_id}")
            raise HTTPException(status_code=404, detail="Activo no encontrado")
        return db_activo
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error al eliminar activo {activo_id}: {e}")
        raise HTTPException(status_code=500, detail="Error interno al eliminar activo")
