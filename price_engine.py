# price_engine.py
import requests

def get_token_price(symbol="BTC"):
    # استخدام API عام لجلب السعر الحالي
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
    try:
        response = requests.get(url)
        data = response.json()
        if 'price' in data:
            return float(data['price'])
        else:
            return None
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

if __name__ == "__main__":
    price = get_token_price("BTC")
    if price:
        print(f"Current BTC Price: {price} USDT")
    else:
        print("Could not fetch price.")
