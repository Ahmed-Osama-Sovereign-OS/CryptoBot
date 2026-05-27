# config.py
# إعدادات الاتصال بالشبكة (سنستخدم Binance Smart Chain كمثال)

# رابط الاتصال بالشبكة (Node URL)
# في المستقبل سنستخدم Alchemy أو Infura، الآن نستخدم الرابط العام
RPC_URL = "https://bsc-dataseed.binance.org/"

# عنوان محفظتك التجريبية (لا تضع مفتاحك الخاص هنا أبداً)
WALLET_ADDRESS = "0x0000000000000000000000000000000000000000"

# عنوان عقد العملة التي سنراقبها (مثلاً BUSD على شبكة BSC)
TOKEN_ADDRESS = "0xe9e7CEA3dedcA5984780Bafc599bD69ADd087D56"

# حد أدنى للربح لكي ينفذ البوت العملية (مثلاً 0.1 دولار)
MIN_PROFIT_THRESHOLD = 0.1

print("Config Loaded Successfully")
