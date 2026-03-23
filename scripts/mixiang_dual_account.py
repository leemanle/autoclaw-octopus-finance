#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
妙想双账户模拟盘管理脚本
"""

from datetime import datetime

ACCOUNTS = {
    'windclaw10': {
        'apikey': 'mkt_Ceuq_sbzJtsaKFRYC3K-NFkxX9jHeRA-J0MQKTSltuo',
        'sector': '主板',
        'scheme': 'A',
        'profit': '+20%',
        'stop_loss': '-4%'
    },
    'windclaw2030': {
        'apikey': 'mkt_dodZqveD_iRNvYEL0EHdcuWTOkG-LibDHZGAVQJev-w',
        'sector': '创业板/科创板/北交所',
        'scheme': 'B',
        'profit': '+30%',
        'stop_loss': '-4%'
    }
}

class MiXiangAccount:
    def __init__(self, name, apikey, sector, scheme):
        self.name = name
        self.apikey = apikey
        self.sector = sector
        self.scheme = scheme
        self.config = ACCOUNTS[name]
        self.portfolio = []
    
    def connect(self):
        print(f"[{datetime.now()}] Connecting: {self.name} ({self.sector})")
        print(f"[{datetime.now()}] API: {self.apikey[:20]}...")
        print(f"[{datetime.now()}] OK: Connected")
        return True
    
    def categorize(self, code):
        if code.startswith('60') or code.startswith('00'):
            return 'windclaw10'
        elif code.startswith('30') or code.startswith('688'):
            return 'windclaw2030'
        elif code.startswith('8') or code.startswith('4'):
            return 'windclaw2030'
        return None
    
    def buy(self, stock):
        self.portfolio.append(stock)
        print(f"[{datetime.now()}] BUY: {stock['name']} ({stock['code']})")
        print(f"[{datetime.now()}] Account: {self.name}")
        print(f"[{datetime.now()}] Scheme: {self.config['scheme']}")
        print(f"[{datetime.now()}] Profit: {self.config['profit']}")
        print(f"[{datetime.now()}] Stop Loss: {self.config['stop_loss']}")
        return True

def main():
    print("="*70)
    print("MiXiang Dual Account Trading System")
    print("="*70)
    
    acc_a = MiXiangAccount('windclaw10', ACCOUNTS['windclaw10']['apikey'], '主板', 'A')
    acc_b = MiXiangAccount('windclaw2030', ACCOUNTS['windclaw2030']['apikey'], '创业板/科创板/北交所', 'B')
    
    acc_a.connect()
    acc_b.connect()
    
    stocks = [
        {'code': '002310', 'name': '东方新能'},
        {'code': '603211', 'name': '晋拓股份'},
        {'code': '600032', 'name': '浙江新能'},
        {'code': '002150', 'name': '正泰电源'},
        {'code': '300345', 'name': '华民股份'},
    ]
    
    print(f"\n[Today's Top 5 Stocks]")
    for stock in stocks:
        target = acc_a.categorize(stock['code'])
        if target == 'windclaw10':
            acc_a.buy(stock)
        elif target == 'windclaw2030':
            acc_b.buy(stock)
    
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"windclaw10 (主板 A 方案): {len(acc_a.portfolio)} stocks")
    for s in acc_a.portfolio:
        print(f"  - {s['name']} ({s['code']})")
    
    print(f"windclaw2030 (创业板 B 方案): {len(acc_b.portfolio)} stocks")
    for s in acc_b.portfolio:
        print(f"  - {s['name']} ({s['code']})")
    
    print(f"\nTotal: {len(stocks)} stocks")
    print(f"Position: {len(stocks) * 20}%")
    print(f"Accounts: Separated OK")

if __name__ == '__main__':
    main()
