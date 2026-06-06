-- S3 external stage configuration
-- Replace placeholders with your actual credentials (never commit real keys)

CREATE OR REPLACE STAGE CRYPTO_DB.BRONZE.S3_STAGE
    URL = 's3://your-bucket-name/bronze/'
    CREDENTIALS = (
        AWS_KEY_ID = 'your_access_key_here'
        AWS_SECRET_KEY = 'your_secret_key_here'
    )
    FILE_FORMAT = (TYPE = 'PARQUET');