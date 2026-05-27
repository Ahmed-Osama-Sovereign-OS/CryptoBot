# logger.py
import datetime

def log_transaction(message):
    # فتح ملف السجلات (سجل العمليات) والكتابة فيه
    with open("bot_history.log", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")
    print(f"Logged: {message}")

if __name__ == "__main__":
    log_transaction("Bot initialization test.")
