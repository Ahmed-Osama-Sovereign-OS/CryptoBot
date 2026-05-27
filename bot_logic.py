# bot_logic.py
from connection import connect_to_blockchain
from price_engine import get_token_price
from config import MIN_PROFIT_THRESHOLD

def run_bot_logic():
    print("Bot is starting its analysis...")
    
    # 1. التأكد من الاتصال
    w3 = connect_to_blockchain()
    if not w3:
        return

    # 2. مراقبة السعر
    current_price = get_token_price("BTC")
    
    if current_price:
        print(f"Analyzing market. Current BTC Price: {current_price}")
        
        # 3. منطق القرار (في هذا المثال البسيط نتحقق من تقلب السعر)
        # هنا سنضع لاحقاً خوارزمية الربح الخاصة بك
        if current_price > 0:
            print("Market is active. Monitoring for opportunities...")
            # هنا سيقوم البوت بالتنفيذ بمجرد توفر الشروط
        else:
            print("Price data error.")
    else:
        print("Failed to get market data.")

if __name__ == "__main__":
    run_bot_logic()
