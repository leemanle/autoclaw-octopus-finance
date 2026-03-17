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
    name = qt['name']
    price = float(qt['price'])
    open_price = float(qt['open'])
    high = float(qt['high'])
    low = float(qt['low'])
    last_close = float(qt['last_close'])
    volume = qt['volume']
    amount = qt['amount']
    change = float(qt['change'])
    change_pct = float(qt['changepercent'])
    
    # K线数据
    klines = data['data'][code]['day']
    kline_list = klines.split(';')
    recent_klines = []
    for k in kline_list[-5:]:
        parts = k.split(' ')
        if len(parts) >= 6:
            recent_klines.append({
                'date': parts[0],
                'open': float(parts[1]),
                'close': float(parts[2]),
                'high': float(parts[3]),
                'low': float(parts[4]),
                'volume': float(parts[5])
            })
    
    stock_info = {
        'code': code,
        'name': name,
        'price': price,
        'open': open_price,
        'high': high,
        'low': low,
        'last_close': last_close,
        'volume': volume,
        'amount': amount,
        'change': change,
        'change_pct': change_pct,
        'klines': recent_klines
    }
    stocks.append(stock_info)
    print(f"{name}({code}): 现价={price}, 涨跌幅={change_pct}%, 昨收={last_close}")

# 输出JSON供后续使用
print("\n===JSON_START===")
print(json.dumps(stocks, ensure_ascii=False))
print("===JSON_END===")
