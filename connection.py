# connection.py
from web3 import Web3
from config import RPC_URL

def connect_to_blockchain():
    # إنشاء الاتصال
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    
    # التحقق من نجاح الاتصال
    if w3.is_connected():
        print("Successfully connected to the Blockchain!")
        return w3
    else:
        print("Failed to connect to the Blockchain.")
        return None

# اختبار الاتصال عند تشغيل الملف
if __name__ == "__main__":
    w3 = connect_to_blockchain()
    if w3:
        # طباعة رقم آخر كتلة تم إنشاؤها في الشبكة للتأكد من النشاط
        print(f"Latest Block Number: {w3.eth.block_number}")
