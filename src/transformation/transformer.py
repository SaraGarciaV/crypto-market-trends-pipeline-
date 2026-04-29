import pandas as pd
from datetime import datetime
from loguru import logger
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
logger.add("logs/transformer.log", rotation="1 MB")


def convert_to_parquet(data, filename_prefix):
    """
    Converts data into a pandas DataFrame and saves it in Parquet format.

    This process includes:
    - Transformation of raw data into a DataFrame
    - Generation of a timestamped file for versioning
    - Saving into the data/raw/ folder
    - Process logging

    Args:
        data (list or dict): Data obtained from the API or extraction stage.
        filename_prefix (str): Prefix for the output file name.

    Returns:
        str: Path of the generated Parquet file.
    """
    try:
        logger.info("Converting data to DataFrame...")

        # Convert data to DataFrame
        df = pd.DataFrame(data)

        logger.info(f"DataFrame created with shape: {df.shape}")

        # Create timestamp for file versioning
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Build file name
        filename = f"{filename_prefix}_{timestamp}.parquet"

        # Define save path
        filepath = os.path.join("data", "raw", filename)

        # Ensure directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        logger.info(f"Saving Parquet file to {filepath}...")

         # Save DataFrame as Parquet
        df.to_parquet(filepath, index=False)

        logger.info("Parquet file saved successfully.")

        return filepath

    except Exception as e:
        logger.error(f"Error converting to parquet: {e}")
        raise

if __name__ == "__main__":
    logger.info("Transformer module loaded successfully.")