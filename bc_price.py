import requests
from datetime import datetime
from typing import Dict, Union

def get_bitcoin_price() -> Dict[str, Union[float, str]]:
    """Fetch the current Bitcoin price from CoinGecko API."""
    try:
        # CoinGecko API endpoint for Bitcoin price in USD
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': 'bitcoin',
            'vs_currencies': 'usd',
            'include_last_updated_at': 'true'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        data = response.json()
        price = data['bitcoin']['usd']
        last_updated = datetime.fromtimestamp(data['bitcoin']['last_updated_at'])
        
        return {
            'price': price,
            'currency': 'USD',
            'last_updated': last_updated.strftime('%Y-%m-%d %H:%M:%S UTC')
        }
        
    except requests.RequestException as e:
        print(f'Error fetching Bitcoin price: {e}')
        return None

def main():
    """Main function to fetch and display Bitcoin price."""
    price_data = get_bitcoin_price()
    
    if price_data:
        print('\nBitcoin Price Information:')
        print(f'Price: ${price_data["price"]:,.2f} {price_data["currency"]}')
        print(f'Last Updated: {price_data["last_updated"]}')
    else:
        print('Failed to fetch Bitcoin price. Please try again later.')

if __name__ == '__main__':
    main()