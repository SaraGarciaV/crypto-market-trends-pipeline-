import os
import requests
from dotenv import load_dotenv
from loguru import logger
import json
from datetime import datetime
logger.add("logs/extractor.log", rotation="1 MB")

# Load environment variables from the .env file
load_dotenv()

def get_coins_markets():
    """
    Fetch cryptocurrency market data from the CoinGecko API.

    Returns:
        list/dict: JSON response containing market data.
    
    Raises:
        requests.exceptions.HTTPError: If the API request fails.
    """
    try:
        # Retrieve configuration values from environment variables
        api_url = os.getenv("COINGECKO_BASE_URL")
        currency = os.getenv("VS_CURRENCY")
        per_page = os.getenv("PER_PAGE")
        page = os.getenv("PAGE")
        price_change = os.getenv("PRICE_CHANGE_PERCENTAGE")
        
        # Define the API endpoint
        endpoint = f"{api_url}/coins/markets"

        # Build query parameters for the request
        payload = {
            "vs_currency": currency,
            "per_page": per_page,
            "page": page,
            "price_change_percentage": price_change,
        }

        logger.info(f"Extracting data from {endpoint}...")

        response = requests.get(endpoint, params=payload)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e}")
        raise

    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error: {e}")
        raise

def get_global_data():
    """
    Fetch global cryptocurrency market data from the CoinGecko API.

    This function retrieves aggregated statistics about the entire
    cryptocurrency market (e.g., total market cap, total volume,
    number of active cryptocurrencies).

    Returns:
        dict: JSON response containing global market data.

    Raises:
        requests.exceptions.HTTPError: If the API request fails.
    """
    try:
        api_url = os.getenv("COINGECKO_BASE_URL")
        endpoint = f"{api_url}/global"

        logger.info(f"Extracting data from {endpoint}...")

        response = requests.get(endpoint)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e}")
        raise

    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error: {e}")
        raise

def save_raw_data(data, filename_prefix):
    """
    Save raw JSON data into a timestamped file inside data/raw/.

    Args:
        data (dict/list): Data returned from the API.
        filename_prefix (str): Base name for the file (e.g. 'coins_markets').

    Returns:
        str: Path of the file saved.
    """

    # Create timestamp (YYYYMMDD_HHMMSS)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Build full filename
    filename = f"{filename_prefix}_{timestamp}.json"

    # Full path
    filepath = os.path.join("data", "raw", filename)

    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Save JSON file
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    logger.info(f"Data saved to {filepath}")

    return filepath


if __name__ == "__main__":
    data = get_coins_markets()
    logger.info(f"Total coins fetched: {len(data)}")
    save_raw_data(data, "coins_markets")
    
    global_data = get_global_data()
    logger.info(f"Global keys: {global_data['data'].keys()}")
    save_raw_data(global_data, "global")