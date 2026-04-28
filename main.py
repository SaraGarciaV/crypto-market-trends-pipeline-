import os
from dotenv import load_dotenv
from loguru import logger

from src.extraction.extractor import (
    get_coins_markets,
    get_global_data,
    save_raw_data
)

from src.transformation.transformer import convert_to_parquet
from src.load.loader import upload_to_s3

load_dotenv()

# Configurar logging
logger.add("logs/pipeline.log", rotation="1 MB")


def main():

    logger.info("Starting ELT pipeline")

    # 1. EXTRACTION

    logger.info("Extracting data from CoinGecko")

    coins_data = get_coins_markets()
    global_data = get_global_data()

    coins_file = save_raw_data(coins_data, "coins_markets")
    global_file = save_raw_data(global_data, "global")


    # 2. TRANSFORMATION

    logger.info("Transforming JSON to Parquet")

    coins_parquet = convert_to_parquet(coins_data, "coins_markets")
    global_parquet = convert_to_parquet(global_data["data"], "global")


    # 3. LOAD (S3)

    logger.info("Uploading files to S3")

    upload_to_s3(
        filepath=coins_parquet,
        s3_key=f"bronze/coins_markets/{os.path.basename(coins_parquet)}"
    )

    upload_to_s3(
        filepath=global_parquet,
        s3_key=f"bronze/global/{os.path.basename(global_parquet)}"
    )

    logger.success("Pipeline executed successfully")


if __name__ == "__main__":
    main()