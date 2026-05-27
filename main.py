# main.py
from bot_logic import run_bot_logic
import time

def main():
    print("Initializing AhmedOsama Crypto Bot...")
    # حلقة تكرارية تجعل البوت يعمل بدون توقف
    while True:
        try:
            run_bot_logic()
        except Exception as e:
            print(f"Bot cycle error: {e}")
        
        # الانتظار لمدة دقيقة قبل التحليل القادم (لتجنب الحظر من السيرفرات)
        time.sleep(60)

if __name__ == "__main__":
    main()
