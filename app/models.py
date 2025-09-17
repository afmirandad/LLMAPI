from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InventarioActivo(Base):
    __tablename__ = 'inventario_activos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    NOMBRE_DEL_ACTIVO = Column(Text)
    DESCRIPCION = Column(Text)
    TIPO_DE_ACTIVO = Column(Text)
    MEDIO_DE_CONSERVACIÓN = Column(Text)
    FORMATO = Column(Text)
    IDIOMA = Column(Text)
    PROCESO = Column(Text)
    DUEÑO_DE_ACTIVO = Column(Text)
    TIPO_DE_DATOS_PERSONALES = Column(Text)
    FINALIDAD_DE_LA_RECOLECCIÓN = Column(Text)
    CONFIDENCIALIDAD = Column(Text)
    INTEGRIDAD = Column(Text)
    DISPONIBILIDAD = Column(Text)
    CRITICIDAD_TOTAL_DEL_ACTIVO = Column(Text)
    INFORMACIÓN_PUBLICADA_O_DISPONIBLE = Column(Text)
    LUGAR_DE_CONSULTA = Column(Text)
