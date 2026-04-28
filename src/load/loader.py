import boto3
import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

def upload_to_s3(filepath, s3_key):
    try:
        # Leer variables de entorno
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        aws_region = os.getenv("AWS_REGION")
        s3_bucket_name = os.getenv("S3_BUCKET_NAME")

        #  Crear cliente S3
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region
        )

        logger.info(f"Uploading {filepath} to s3://{s3_bucket_name}/{s3_key}")

        #  Subir archivo
        s3_client.upload_file(
            filepath,
            s3_bucket_name,
            s3_key
        )

        logger.success(f"Upload successful: {s3_key}")

    except Exception as e:
        logger.error(f"Error uploading {filepath} to S3: {e}")
        raise

#if __name__ == "__main__":
 #   import os
 #   os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    
    #upload_to_s3(
    #    filepath="data/raw/coins_markets_20260423_191437.parquet",
    #    s3_key="bronze/coins_markets/coins_markets_20260423_191437.parquet"
    #)
    #upload_to_s3(
    #filepath="data/raw/global_20260423_191630.parquet",
    #s3_key="bronze/global/global_20260423_191630.parquet"
    #)

if __name__ == "__main__":
    logger.info("Loader module loaded successfully.")