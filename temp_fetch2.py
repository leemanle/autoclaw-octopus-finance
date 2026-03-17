import urllib.request
import json

codes = ['sh600313', 'sh601975', 'sz300606']
stocks = []

for code in codes:
    url = f"https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={code},day,,,10,qfq"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
    
    qt = data['data'][code]['qt']
    # 打印所有key
    print(f"=== {code} qt keys ===")
    for k, v in qt.items():
        print(f"  {k}: {v}")
    
    price = float(qt.get('price', qt.get('_price', 0)))
    name = qt.get('stock_name', qt.get('name', code))
    
    stock_info = {
        'code': code,
        'name': name,
        'price': price,
        'change_pct': float(qt.get('changepercent', 0)),
        'last_close': float(qt.get('last_close', 0)),
    }
    stocks.append(stock_info)

print("\n===JSON_START===")
print(json.dumps(stocks, ensure_ascii=False))
print("===JSON_END===")
