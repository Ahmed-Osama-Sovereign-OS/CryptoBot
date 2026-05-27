# bot_logic.py
from connection import connect_to_blockchain
from price_engine import get_token_price
from config import MIN_PROFIT_THRESHOLD

def calculate_arbitrage(price_a, price_b):
    # حساب نسبة الربح بين منصتين
    profit = price_b - price_a
    return profit

def run_bot_logic():
    print("Bot is analyzing market opportunities...")
    
    # 1. جلب الأسعار من مصدرين مختلفين (مثال تجريبي)
    price_binance = get_token_price("BTC") # سعر المنصة 1
    price_kucoin = price_binance * 1.005   # سعر افتراضي للمنصة 2 (للتوضيح)
    
    if price_binance and price_kucoin:
        profit = calculate_arbitrage(price_binance, price_kucoin)
        print(f"Spread detected: {profit} USDT")
        
        # 2. منطق اتخاذ القرار
        if profit > MIN_PROFIT_THRESHOLD:
            print(f"!!! OPPORTUNITY FOUND: {profit} USDT !!!")
            # هنا سنضع لاحقاً كود تنفيذ الصفقة (Execution)
        else:
            print("No profitable opportunity currently.")

if __name__ == "__main__":
    run_bot_logic()
