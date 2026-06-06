-- Raw data tables - stores data exactly as it arrives from S3
-- Data stored as VARIANT (semi-structured JSON)

CREATE TABLE IF NOT EXISTS CRYPTO_DB.BRONZE.STG_COINS_MARKETS (
    raw_data VARIANT,
    loaded_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE IF NOT EXISTS CRYPTO_DB.BRONZE.STG_GLOBAL (
    raw_data VARIANT,
    loaded_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);