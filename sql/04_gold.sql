-- Curated views ready for Power BI dashboard
-- Views instead of physical tables to avoid storage duplication

CREATE OR REPLACE VIEW CRYPTO_DB.GOLD.VW_GOLD_MARKET_DASHBOARD AS
SELECT
    symbol,
    name,
    current_price,
    market_cap_rank,
    total_volume,
    pct_change_24h,
    pct_change_7d,
    last_updated
FROM CRYPTO_DB.SILVER.SILVER_CRYPTO_PRICES;

CREATE OR REPLACE VIEW CRYPTO_DB.GOLD.VW_GOLD_TOP_MOVERS AS
SELECT
    symbol,
    name,
    pct_change_24h,
    pct_change_7d,
    RANK() OVER (ORDER BY pct_change_24h DESC) AS rank_24h,
    RANK() OVER (ORDER BY pct_change_7d DESC) AS rank_7d
FROM CRYPTO_DB.SILVER.SILVER_CRYPTO_PRICES;

CREATE OR REPLACE VIEW CRYPTO_DB.GOLD.VW_GOLD_GLOBAL_SUMMARY AS
SELECT
    symbol,
    name,
    market_cap_rank,
    current_price,
    total_volume,
    pct_change_24h,
    pct_change_7d
FROM CRYPTO_DB.SILVER.SILVER_CRYPTO_PRICES
ORDER BY market_cap_rank ASC;