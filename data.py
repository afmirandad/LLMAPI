import pandas as pd
import logging

# Configura el logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def leer_excel_a_dataframe(ruta_archivo: str) -> pd.DataFrame:
    """
    Lee un archivo Excel y retorna un DataFrame de pandas.
    """
    try:
        df = pd.read_excel(ruta_archivo)
        logger.info(f'Archivo {ruta_archivo} leído correctamente. Filas: {len(df)}')
        return df
    except Exception as e:
        logger.error(f'Error al leer el archivo Excel: {e}')
        raise

if __name__ == "__main__":
    ruta = "Files/inventario_de_activos_de_la_informacion_foncep_2024.xlsx"
    df = leer_excel_a_dataframe(ruta)
    print(df.head())
