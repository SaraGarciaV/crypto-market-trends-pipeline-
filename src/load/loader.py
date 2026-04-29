import boto3
import os
from dotenv import load_dotenv
from loguru import logger

# Load environment variables from the .env file
load_dotenv()

def upload_to_s3(filepath, s3_key):
    """
    Upload a file to an S3 bucket.

    Args:
        filepath (str): Local path to the file to upload.
        s3_key (str): Destination key/path in the S3 bucket.

    Raises:
        Exception: If the upload fails.
    """
    try:
        # Retrieve configuration values from environment variables
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        aws_region = os.getenv("AWS_REGION")
        s3_bucket_name = os.getenv("S3_BUCKET_NAME")

        # Create S3 client with AWS credentials
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region
        )

        logger.info(f"Uploading {filepath} to s3://{s3_bucket_name}/{s3_key}")

        # Upload file to S3 bucket
        s3_client.upload_file(
            filepath,
            s3_bucket_name,
            s3_key
        )

        logger.success(f"Upload successful: {s3_key}")

    except Exception as e:
        logger.error(f"Error uploading {filepath} to S3: {e}")
        raise

if __name__ == "__main__":
    logger.info("Loader module loaded successfully.")