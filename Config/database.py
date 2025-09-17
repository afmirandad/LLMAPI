import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine.base import Engine
from dotenv import load_dotenv

# Configura el logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Carga las variables de entorno desde el archivo .env
load_dotenv()

def get_database_connection() -> Engine:
    """
    Configura y retorna la conexión a la base de datos usando SQLAlchemy.
    La URL de la base de datos debe estar en la variable de entorno DATABASE_URL.
    """
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        logger.error('DATABASE_URL no está definida en el archivo .env')
        raise ValueError('DATABASE_URL no está definida en el archivo .env')
    try:
        engine = create_engine(database_url)
        # Probar la conexión
        with engine.connect() as connection:
            logger.info('Conexión a la base de datos exitosa')
        return engine
    except SQLAlchemyError as e:
        logger.error(f'Error al conectar a la base de datos: {e}')
        raise
