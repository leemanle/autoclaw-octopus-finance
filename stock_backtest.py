# -*- coding: utf-8 -*-
"""
股票选股策略回测系统
策略：热门板块领涨股 + 首板策略
回测周期：2022-01 至 2026-03
"""

import pandas as pd
import numpy as np
import os
import glob
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ========== 配置 ==========
DATA_DIR = r"E:\BaiduNetdiskDownload"
START_DATE = "2022-01-01"
END_DATE = "2026-03-15"

# 策略参数
TOP_N_SECTORS = 3      # 每日选热门板块数量
TOP_N_STOCKS = 3       # 每板块选领涨股数量
MAX_HOLD_DAYS = 6      # 最长持股天数
STOP_LOSS_PCT = -8     # 止损 -8%
STOP_GAIN_PCT = 23     # 止盈 +23%
POSITION_SIZE = 1/3     # 每只股票仓位 (1/3 = 20%)

# 首板条件 (简化版)
FIRST_BOARD_PCT = 9.8  # 涨停板 threshold

class StockBacktester:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.all_data = {}  # {date: DataFrame}
        self.positions = []  # 持仓记录
        self.trades = []     # 交易记录
        
    def load_all_data(self):
        """加载所有CSV数据"""
        print("加载数据...")
        
        # 遍历各年份
        for year in ["2022", "2023", "2024", "2025", "2026"]:
            year_dir = os.path.join(self.data_dir, year)
            if not os.path.exists(year_dir):
                continue
                
            csv_files = glob.glob(os.path.join(year_dir, "*.csv"))
            for csv_file in csv_files:
                try:
                    # 指定列名，跳过第一行header
                    cols = ['序号','代码','名称','日期','昨收','开盘','收盘','最高','最低','成交量','成交额','振幅','涨跌幅']
                    try:
                        df = pd.read_csv(csv_file, names=cols, encoding='utf-8', skiprows=1)
                        if df.empty or '日期' not in df.columns:
                            continue
                    except:
                        continue
                    
                    # 确保日期格式正确
                    try:
                        df['日期'] = pd.to_datetime(df['日期']).dt.strftime('%Y-%m-%d')
                        date = df['日期'].iloc[0]
                        self.all_data[date] = df
                    except:
                        continue
                except Exception as e:
                    continue
        
        print(f"加载完成: {len(self.all_data)} 个交易日")
        return sorted(self.all_data.keys())
    
    def get_sector_leaders(self, date):
        """获取当日热门板块领涨股"""
        if date not in self.all_data:
            return []
        
        df = self.all_data[date]
        
        # 按涨跌幅排序，取前20作为热门领涨
        df_sorted = df.sort_values('涨跌幅', ascending=False).head(50)
        
        # 筛选首板股票 (涨跌幅接近10%)
        first_board = df_sorted[df_sorted['涨跌幅'] >= FIRST_BOARD_PCT]
        
        # 取前N只
        leaders = first_board.head(TOP_N_STOCKS)
        
        return leaders[['代码', '名称', '涨跌幅', '成交量', '成交额']].to_dict('records')
    
    def run_backtest(self):
        """运行回测"""
        dates = self.load_all_data()
        
        capital = 1000000  # 初始资金100万
        holdings = {}  # {code: {'shares': x, 'cost': y, 'entry_date': z}}
        
        print("\n" + "="*60)
        print("开始回测")
        print("="*60)
        
        for i, date in enumerate(dates):
            # 1. 选股信号
            candidates = self.get_sector_leaders(date)
            
            # 2. 处理持仓
            to_sell = []
            for code, holding in holdings.items():
                # 检查是否需要卖出
                if date in self.all_data:
                    stock_data = self.all_data[date]
                    stock_row = stock_data[stock_data['代码'] == code]
                    
                    if not stock_row.empty:
                        current_price = stock_row['收盘'].values[0]
                        entry_price = holding['cost']
                        change_pct = (current_price - entry_price) / entry_price * 100
                        days_held = (datetime.strptime(date, '%Y-%m-%d') - 
                                   datetime.strptime(holding['entry_date'], '%Y-%m-%d')).days
                        
                        # 止盈/止损/到期卖出
                        if change_pct >= STOP_GAIN_PCT or change_pct <= STOP_LOSS_PCT or days_held >= MAX_HOLD_DAYS:
                            # 卖出
                            sell_price = stock_row['开盘'].values[0] if change_pct <= STOP_LOSS_PCT else current_price
                            proceeds = holding['shares'] * sell_price
                            capital += proceeds
                            
                            self.trades.append({
                                'date': date,
                                'code': code,
                                'action': 'SELL',
                                'price': sell_price,
                                'change_pct': change_pct,
                                'reason': 'STOP_GAIN' if change_pct >= STOP_GAIN_PCT else 
                                         'STOP_LOSS' if change_pct <= STOP_LOSS_PCT else 'TIME_OUT'
                            })
                            to_sell.append(code)
            
            for code in to_sell:
                del holdings[code]
            
            # 3. 买入新股票 (如果有空余仓位且有候选)
            available_capital = capital * (1 - len(holdings) * POSITION_SIZE)
            
            for candidate in candidates[:(3 - len(holdings))]:
                code = candidate['代码']
                if code in holdings:
                    continue
                if available_capital <= 0:
                    break
                    
                if date in self.all_data:
                    stock_data = self.all_data[date]
                    stock_row = stock_data[stock_data['代码'] == code]
                    
                    if not stock_row.empty:
                        buy_price = stock_row['开盘'].values[0]
                        shares = int((available_capital * POSITION_SIZE) / buy_price / 100) * 100  # 整手
                        
                        if shares > 0:
                            cost = shares * buy_price
                            capital -= cost
                            
                            holdings[code] = {
                                'shares': shares,
                                'cost': buy_price,
                                'entry_date': date,
                                'name': candidate['名称']
                            }
                            
                            self.trades.append({
                                'date': date,
                                'code': code,
                                'action': 'BUY',
                                'price': buy_price,
                                'name': candidate['名称']
                            })
                            available_capital -= cost
        
        # 最终平仓
        final_date = dates[-1]
        for code, holding in holdings.items():
            if final_date in self.all_data:
                stock_data = self.all_data[final_date]
                stock_row = stock_data[stock_data['代码'] == code]
                
                if not stock_row.empty:
                    sell_price = stock_row['收盘'].values[0]
                    proceeds = holding['shares'] * sell_price
                    capital += proceeds
                    
                    change_pct = (sell_price - holding['cost']) / holding['cost'] * 100
                    self.trades.append({
                        'date': final_date,
                        'code': code,
                        'action': 'SELL',
                        'price': sell_price,
                        'change_pct': change_pct,
                        'reason': 'FINAL_CLOSE'
                    })
        
        # 统计结果
        self.print_results()
        
    def print_results(self):
        """打印回测结果"""
        print("\n" + "="*60)
        print("回测结果")
        print("="*60)
        
        trades_df = pd.DataFrame(self.trades)
        
        if trades_df.empty:
            print("无交易记录")
            return
        
        # 买入次数
        buy_count = len(trades_df[trades_df['action'] == 'BUY'])
        sell_count = len(trades_df[trades_df['action'] == 'SELL'])
        
        print(f"买入次数: {buy_count}")
        print(f"卖出次数: {sell_count}")
        
        # 盈利统计
        sell_trades = trades_df[trades_df['action'] == 'SELL']
        if not sell_trades.empty:
            wins = len(sell_trades[sell_trades['change_pct'] > 0])
            losses = len(sell_trades[sell_trades['change_pct'] <= 0])
            win_rate = wins / len(sell_trades) * 100
            
            avg_gain = sell_trades[sell_trades['change_pct'] > 0]['change_pct'].mean() if wins > 0 else 0
            avg_loss = sell_trades[sell_trades['change_pct'] <= 0]['change_pct'].mean() if losses > 0 else 0
            
            print(f"盈利次数: {wins}")
            print(f"亏损次数: {losses}")
            print(f"胜率: {win_rate:.1f}%")
            print(f"平均盈利: {avg_gain:.2f}%")
            print(f"平均亏损: {avg_loss:.2f}%")
            
            # 最大回撤
            trades_df['cumsum'] = trades_df[trades_df['action']=='SELL']['change_pct'].cumsum()
            max_drawdown = trades_df['cumsum'].min()
            print(f"最大回撤: {max_drawdown:.2f}%")
        
        print("\n" + "="*60)
        print("交易明细")
        print("="*60)
        print(trades_df.to_string())
        
        # 保存结果
        output_file = r"C:\Users\Administrator\.openclaw-autoclaw\workspace\backtest_result.csv"
        trades_df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"\n结果已保存: {output_file}")

if __name__ == "__main__":
    tester = StockBacktester(DATA_DIR)
    tester.run_backtest()
