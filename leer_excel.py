import pandas as pd
import logging

from sqlalchemy import Column, Integer, String, MetaData, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Config.database import get_database_connection

# Configura el logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def leer_excel_a_dataframe(ruta_archivo: str) -> pd.DataFrame:
    """
    Lee un archivo Excel y retorna un DataFrame de pandas, usando la segunda fila como cabecera.
    """
    try:
        # header=1 indica que la fila 2 (índice 1) es la cabecera
        df = pd.read_excel(ruta_archivo, header=1)
        logger.info(f'Archivo {ruta_archivo} leído correctamente. Filas: {len(df)}')
        return df
    except Exception as e:
        logger.error(f'Error al leer el archivo Excel: {e}')
        raise

def limpiar_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza una limpieza básica del DataFrame:
    - Elimina filas completamente vacías
    - Elimina columnas completamente vacías
    - Elimina espacios en los nombres de columnas
    - Elimina filas duplicadas
    - Rellena NaN con string vacío
    """
    df = df.dropna(how='all')
    df = df.dropna(axis=1, how='all')
    df.columns = [str(col).strip() for col in df.columns]
    df = df.drop_duplicates()
    df = df.fillna("")
    return df


# --- MODELO SQLALCHEMY ---
Base = declarative_base()


# Modelo dinámico generado según las columnas del DataFrame
InventarioActivo = None

def crear_modelo_dinamico(df):
    global InventarioActivo
    attrs = {
        '__tablename__': 'inventario_activos',
        'id': Column(Integer, primary_key=True, autoincrement=True)
    }
    for col in df.columns:
        # Reemplaza caracteres no válidos para nombres de variables
        col_name = str(col).replace(' ', '_').replace('(', '').replace(')', '').replace('.', '').replace('/', '_').replace('-', '_')
        attrs[col_name] = Column(Text)
    InventarioActivo = type('InventarioActivo', (Base,), attrs)

def insertar_dataframe(df: pd.DataFrame, engine):
    """
    Inserta los datos del DataFrame en la tabla inventario_activos.
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        # Convertir cada fila del DataFrame en un objeto InventarioActivo
        for _, row in df.iterrows():
            data = row.to_dict()
            # Adaptar claves a los nombres de atributos del modelo
            data_fixed = {str(k).replace(' ', '_').replace('(', '').replace(')', '').replace('.', '').replace('/', '_').replace('-', '_'): str(v) for k, v in data.items()}
            obj = InventarioActivo(**data_fixed)
            session.add(obj)
        session.commit()
        logger.info('Datos insertados correctamente en la base de datos.')
    except Exception as e:
        session.rollback()
        logger.error(f'Error al insertar datos: {e}')
        raise
    finally:
        session.close()

if __name__ == "__main__":
    ruta = "Files/inventario_de_activos_de_la_informacion_foncep_2024.xlsx"
    df = leer_excel_a_dataframe(ruta)
    # Renombrar penúltima y última columna
    cols = list(df.columns)
    if len(cols) >= 2:
        cols[-2] = 'INFORMACIÓN (PUBLICADA O DISPONIBLE)'
        cols[-1] = 'LUGAR DE CONSULTA'
        df.columns = cols
    # Limpiar el DataFrame
    df = limpiar_dataframe(df)
    print('Nombres de columnas:')
    print(list(df.columns))
    print(df.head())

    # --- Conexión e inserción a la base de datos ---
    engine = get_database_connection()
    # Crear modelo dinámico según columnas
    crear_modelo_dinamico(df)
    # Crear la tabla si no existe
    Base.metadata.create_all(engine)
    # Insertar datos
    insertar_dataframe(df, engine)
