# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import requests, json
from datetime import datetime

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def get_hot_sectors():
    url = "https://push2.eastmoney.com/api/qt/clist/get"
    params = {"pn":1,"pz":10,"po":1,"np":1,"fltt":2,"invt":2,"fid":"f3","fs":"m:90+t:2","fields":"f2,f3,f4,f12,f14"}
    try:
        r = requests.get(url, params=params, timeout=10)
        return r.json().get("data",{}).get("diff",[])[:10]
    except: return []

def get_leader_stocks(bk_code):
    url = "https://push2.eastmoney.com/api/qt/clist/get"
    params = {"pn":1,"pz":5,"po":1,"np":1,"fltt":2,"invt":2,"fid":"f3","fs":f"b:{bk_code}","fields":"f2,f3,f4,f12,f14,f5,f6"}
    try:
        r = requests.get(url, params=params, timeout=10)
        return r.json().get("data",{}).get("diff",[])[:5]
    except: return []

def get_kline(code, days=5):
    market = "sh" if code.startswith("6") else "sz"
    url = f"https://web.ifzq.gtimg.cn/appstock/app/fqkline/get"
    params = {"param":f"{market}{code},day,,,{days},qfq"}
    try:
        r = requests.get(url, params=params, timeout=10)
        return r.json().get("data",{}).get(f"{market}{code}",{}).get("qfqday",[])[-5:]
    except: return []

def check_first_board(kline_data, current_change):
    if not kline_data or len(kline_data) < 4: return False
    try:
        closes = [float(d[2]) for d in kline_data[:-1] if len(d) >= 3]
        if len(closes) < 3: return False
        changes = [(closes[i] - closes[i-1])/closes[i-1] for i in range(1, len(closes))]
        if all(c <= 0.085 for c in changes[:3]) and current_change >= 3.5:
            return True
        return False
    except: return False

def select_stocks():
    log("="*50)
    log(f"{datetime.now().strftime('%H:%M:%S')} 选股开始")
    log("="*50)
    
    sectors = get_hot_sectors()
    if not sectors:
        log("获取板块失败")
        return []
    
    log(f"获取到 {len(sectors)} 个热门板块")
    
    candidates = []
    for s in sectors[:5]:
        bk_code = s.get("f12","")
        bk_name = s.get("f14","")
        bk_change = s.get("f3",0)
        
        if bk_change < 1: continue
        
        leaders = get_leader_stocks(bk_code)
        for stock in leaders:
            code = stock.get("f12","")
            name = stock.get("f14","")
            price = stock.get("f2",0)
            change = stock.get("f3",0)
            
            if change < 3: continue
            
            kline = get_kline(code)
            is_first = check_first_board(kline, change)
            
            candidates.append({
                "code":code,"name":name,"sector":bk_name,
                "change":change,"price":price,
                "first_board":is_first,
                "score":change*10+(1000000 if is_first else 0)
            })
    
    candidates.sort(key=lambda x:x["score"],reverse=True)
    top3 = candidates[:3]
    
    log(f"选出 Top3:")
    for i,s in enumerate(top3,1):
        fb = "[首板]" if s["first_board"] else ""
        log(f"  {i}. {s['code']} {s['name']} {s['sector']} 涨幅:{s['change']:.2f}% {fb}")
    
    return top3

# 模拟交易
portfolio = {"cash":100000,"positions":{},"trades":[]}

def simulate_trade(stocks):
    global portfolio
    
    log(f"模拟账户: 现金={portfolio['cash']}")
    
    # 卖出
    to_sell = []
    for code,pos in list(portfolio["positions"].items()):
        secid = f"0.{code}" if not code.startswith("6") else f"1.{code}"
        url = f"https://push2.eastmoney.com/api/qt/ulist.np/get"
        params = {"fltt":2,"secids":secid,"fields":"f2,f3"}
        try:
            r = requests.get(url, params=params, timeout=5)
            data = r.json().get("data",{}).get("diff",[{}])[0]
            price = data.get("f2",0)
            change = data.get("f3",0)
            if price>0:
                profit_pct = (price-pos["cost"])/pos["cost"]*100
                if change>9 or profit_pct>9 or profit_pct<-5:
                    to_sell.append(code)
                    portfolio["cash"] += price*pos["shares"]
                    log(f"卖出 {code} {pos['name']} 现价:{price:.2f} 盈亏:{price*pos['shares']-pos['cost']*pos['shares']:+,.0f}")
                    del portfolio["positions"][code]
        except: pass
    
    # 买入
    if stocks and len(portfolio["positions"])<3:
        available = [s for s in stocks if s["code"] not in portfolio["positions"]]
        for stock in available[:3-len(portfolio["positions"])]:
            code,price,name = stock["code"],stock["price"],stock["name"]
            if price<=0 or portfolio["cash"]<30000: continue
            shares = int(30000/price/100)*100
            if shares>0:
                cost = shares*price
                portfolio["cash"] -= cost
                portfolio["positions"][code] = {"name":name,"shares":shares,"cost":price,"buy_time":datetime.now().strftime("%H:%M")}
                log(f"买入 {code} {name} {shares}股 @{price:.2f} 成本:{cost:,.0f}")
    
    log(f"持仓({len(portfolio['positions'])}只):")
    total = portfolio["cash"]
    for code,pos in portfolio["positions"].items():
        secid = f"0.{code}" if not code.startswith("6") else f"1.{code}"
        url = f"https://push2.eastmoney.com/api/qt/ulist.np/get"
        params = {"fltt":2,"secids":secid,"fields":"f2,f3"}
        try:
            r = requests.get(url, params=params, timeout=5)
            data = r.json().get("data",{}).get("diff",[{}])[0]
            price = data.get("f2",0)
            if price>0:
                value = price*pos["shares"]
                profit = (price-pos["cost"])*pos["shares"]
                pct = (price-pos["cost"])/pos["cost"]*100
                log(f"  {code} {pos['name']} {pos['shares']}股 现价:{price:.2f} 盈亏:{profit:+,.0f}({pct:+.1f}%)")
                total += value
        except: pass
    
    log(f"总资产: {total:,.0f}")
    log("="*50)
    
    result = {"time":datetime.now().strftime("%Y-%m-%d %H:%M"),"stocks":stocks,"portfolio":portfolio,"total":total}
    with open("C:\\Users\\Administrator\\.openclaw-autoclaw\\workspace\\reports\\sim_trade.json","w",encoding="utf-8") as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
    return result

if __name__ == "__main__":
    stocks = select_stocks()
    result = simulate_trade(stocks)
    log("完成")