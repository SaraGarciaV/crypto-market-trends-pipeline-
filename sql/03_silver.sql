-- Cleansed and structured tables
-- Data is typed, renamed and validated

CREATE TABLE IF NOT EXISTS CRYPTO_DB.SILVER.SILVER_CRYPTO_PRICES (
    id STRING,
    symbol STRING,
    name STRING,
    current_price FLOAT,
    market_cap FLOAT,
    market_cap_rank INT,
    total_volume FLOAT,
    pct_change_24h FLOAT,
    pct_change_7d FLOAT,
    last_updated TIMESTAMP_NTZ,
    loaded_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE IF NOT EXISTS CRYPTO_DB.SILVER.SILVER_GLOBAL_METRICS (
    coin_id STRING,
    dominance_pct FLOAT,
    last_updated TIMESTAMP_NTZ,
    loaded_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);