# security.py
import os

def get_private_key():
    # البوت سيحاول قراءة المفتاح من "متغيرات النظام"
    # هذا يمنع تسريب المفتاح الخاص في ملفات الكود
    key = os.getenv("PRIVATE_KEY")
    
    if not key:
        print("CRITICAL: Private Key not found in Environment Variables!")
        return None
    return key

# ملاحظة للمستخدم: 
# لا تضع مفتاحك الحقيقي هنا أبداً. 
# في بيئة الإنتاج، يتم تعيين المفتاح في إعدادات GitHub Secrets.
