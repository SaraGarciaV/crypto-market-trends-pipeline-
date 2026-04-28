import pandas as pd
from datetime import datetime
from loguru import logger
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
logger.add("logs/transformer.log", rotation="1 MB")


def convert_to_parquet(data, filename_prefix):
    """
    Convierte datos en un DataFrame de pandas y los guarda en formato Parquet.

    Este proceso incluye:
    - Transformación de datos crudos a DataFrame
    - Generación de un archivo con timestamp para versionado
    - Guardado en la carpeta data/raw/
    - Registro del proceso mediante logs

    Args:
        data (list or dict): Datos obtenidos de la API o etapa de extracción.
        filename_prefix (str): Prefijo del nombre del archivo de salida.

    Returns:
        str: Ruta del archivo Parquet generado.
    """
    try:
        logger.info("Converting data to DataFrame...")

        # Convertir datos a DataFrame
        df = pd.DataFrame(data)

        logger.info(f"DataFrame created with shape: {df.shape}")

        # Crear timestamp para versionado del archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Construir nombre del archivo
        filename = f"{filename_prefix}_{timestamp}.parquet"

        # Definir ruta de guardado
        filepath = os.path.join("data", "raw", filename)

        # Asegurar que el directorio exista
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        logger.info(f"Saving Parquet file to {filepath}...")

        # Guardar DataFrame como Parquet
        df.to_parquet(filepath, index=False)

        logger.info("Parquet file saved successfully.")

        return filepath

    except Exception as e:
        logger.error(f"Error converting to parquet: {e}")
        raise

if __name__ == "__main__":
    logger.info("Transformer module loaded successfully.")