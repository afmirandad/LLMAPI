from sqlalchemy.orm import Session
from . import models, schemas

def get_inventario_activos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.InventarioActivo).offset(skip).limit(limit).all()

def get_inventario_activo(db: Session, activo_id: int):
    return db.query(models.InventarioActivo).filter(models.InventarioActivo.id == activo_id).first()

def create_inventario_activo(db: Session, activo: schemas.InventarioActivoCreate):
    db_activo = models.InventarioActivo(**activo.dict())
    db.add(db_activo)
    db.commit()
    db.refresh(db_activo)
    return db_activo

def update_inventario_activo(db: Session, activo_id: int, activo: schemas.InventarioActivoUpdate):
    db_activo = get_inventario_activo(db, activo_id)
    if db_activo:
        for key, value in activo.dict(exclude_unset=True).items():
            setattr(db_activo, key, value)
        db.commit()
        db.refresh(db_activo)
    return db_activo

def delete_inventario_activo(db: Session, activo_id: int):
    db_activo = get_inventario_activo(db, activo_id)
    if db_activo:
        db.delete(db_activo)
        db.commit()
    return db_activo
