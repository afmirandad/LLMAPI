from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/inventario/", response_model=List[schemas.InventarioActivoOut])
def read_inventario_activos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_inventario_activos(db, skip=skip, limit=limit)

@router.get("/inventario/{activo_id}", response_model=schemas.InventarioActivoOut)
def read_inventario_activo(activo_id: int, db: Session = Depends(get_db)):
    db_activo = crud.get_inventario_activo(db, activo_id)
    if db_activo is None:
        raise HTTPException(status_code=404, detail="Activo no encontrado")
    return db_activo

@router.post("/inventario/", response_model=schemas.InventarioActivoOut)
def create_inventario_activo(activo: schemas.InventarioActivoCreate, db: Session = Depends(get_db)):
    return crud.create_inventario_activo(db, activo)

@router.put("/inventario/{activo_id}", response_model=schemas.InventarioActivoOut)
def update_inventario_activo(activo_id: int, activo: schemas.InventarioActivoUpdate, db: Session = Depends(get_db)):
    db_activo = crud.update_inventario_activo(db, activo_id, activo)
    if db_activo is None:
        raise HTTPException(status_code=404, detail="Activo no encontrado")
    return db_activo

@router.delete("/inventario/{activo_id}", response_model=schemas.InventarioActivoOut)
def delete_inventario_activo(activo_id: int, db: Session = Depends(get_db)):
    db_activo = crud.delete_inventario_activo(db, activo_id)
    if db_activo is None:
        raise HTTPException(status_code=404, detail="Activo no encontrado")
    return db_activo
