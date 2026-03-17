---
summary: "Tushare Pro A-share data query skill"
version: "1.0.0"
---

# Tushare Data Skill

Use Tushare Pro API to query Chinese A-share market data including daily quotes, stock info, indices, financials, and more.

## Configuration

Set Tushare token in TOOLS.md or pass directly:
- Token: `981d54b4f6d2a390364f5bf05fdce9e2795ffb0db5cee124f3625c45`
- Note: New accounts need to request API permissions at https://tushare.pro/document/1?doc_id=108

## Python Path

Always use full path: `C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe`

## Common Commands

Use `exec` tool with the Python path to run Tushare queries. Template:

```
& "C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe" -c "
import tushare as ts
ts.set_token('981d54b4f6d2a390364f5bf05fdce9e2795ffb0db5cee124f3625c45')
pro = ts.pro_api()
<QUERY>
"
```

### 1. Daily Quotes (pro.daily)
```python
df = pro.daily(ts_code='000001.SZ', start_date='20260101', end_date='20260311')
```

### 2. Stock List (pro.stock_basic)
```python
df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
```

### 3. Index Daily (pro.index_daily)
```python
# Shanghai Composite: 000001.SH, Shenzhen Component: 399001.SZ, CSI 300: 000300.SH
df = pro.index_daily(ts_code='000001.SH', start_date='20260301')
```

### 4. Top List / Limit Up (pro.stk_limit)
```python
df = pro.stk_limit(trade_date='20260311', limit_type='U')  # limit up
```

### 5. Money Flow (pro.money_flow)
```python
df = pro.money_flow(trade_date='20260311')
```

### 6. Daily Basic (valuation, turnover, etc.)
```python
df = pro.daily_basic(trade_date='20260311', fields='ts_code,turnover_rate,pe,pb,ps,total_mv,circ_mv')
```

### 7. Financial Indicators (pro.fina_indicator)
```python
df = pro.fina_indicator(ts_code='000001.SZ', start_date='20250101')
```

### 8. Dividend Data (pro.dividend)
```python
df = pro.dividend(ts_code='000001.SZ', fields='ts_code,div_proc,stk_div,record_date,ex_date')
```

### 9. Industry Classification (pro.industry)
```python
df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,industry')
```

### 10. News / Announcements (pro.news)
```python
df = pro.news(src='sina', start_date='20260311', end_date='20260311')
```

## Data Saving

To save data as CSV:
```python
df = pro.daily(ts_code='000001.SZ', start_date='20260301')
df.to_csv('data/000001_daily.csv', index=False, encoding='utf-8-sig')
```

## Rate Limits

- Free tier: ~120 calls/minute
- If rate limited, add `time.sleep(0.5)` between calls

## Common Stock Codes

| Code | Stock | ts_code |
|------|-------|---------|
| 000001 | Ping An Bank | 000001.SZ |
| 600519 | Moutai | 600519.SH |
| 000001.SH | Shanghai Composite | Index |
| 399001.SZ | Shenzhen Component | Index |
| 000300.SH | CSI 300 | Index |
| 399006.SZ | ChiNext | Index |

## Workflow for Analysis

1. Fetch data with Tushare or AKShare
2. Save to workspace data/ folder
3. Analyze with pandas
4. Present findings in clear format
