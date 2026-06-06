-- Load raw data from S3 into Bronze staging tables
COPY INTO CRYPTO_DB.BRONZE.STG_COINS_MARKETS (raw_data)
FROM (SELECT $1 FROM @CRYPTO_DB.BRONZE.S3_STAGE/coins_markets/)
FILE_FORMAT = (TYPE = 'PARQUET')
MATCH_BY_COLUMN_NAME = NONE;

COPY INTO CRYPTO_DB.BRONZE.STG_GLOBAL (raw_data)
FROM (SELECT $1 FROM @CRYPTO_DB.BRONZE.S3_STAGE/global/)
FILE_FORMAT = (TYPE = 'PARQUET')
MATCH_BY_COLUMN_NAME = NONE;

-- Transform Bronze to Silver - extract and type fields from VARIANT
INSERT INTO CRYPTO_DB.SILVER.SILVER_CRYPTO_PRICES
SELECT
    raw_data:id::STRING AS id,
    raw_data:symbol::STRING AS symbol,
    raw_data:name::STRING AS name,
    raw_data:current_price::FLOAT AS current_price,
    raw_data:market_cap::FLOAT AS market_cap,
    raw_data:market_cap_rank::INT AS market_cap_rank,
    raw_data:total_volume::FLOAT AS total_volume,
    raw_data:price_change_percentage_24h::FLOAT AS pct_change_24h,
    raw_data:price_change_percentage_7d_in_currency::FLOAT AS pct_change_7d,
    raw_data:last_updated::TIMESTAMP_NTZ AS last_updated,
    CURRENT_TIMESTAMP() AS loaded_at
FROM CRYPTO_DB.BRONZE.STG_COINS_MARKETS
WHERE raw_data:id IS NOT NULL;