import pandas as pd
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

df = pd.read_csv(r'C:\Users\Administrator\.openclaw-autoclaw\workspace\temp_zhengzhou.csv', skiprows=5)
df.columns = ['No', 'Product', 'Wholesale', 'Retail', 'BigPrice', 'Note']
df = df.dropna(subset=['Product'])

# Calculate profit
df['Profit'] = df['Retail'] - df['Wholesale']
df['ProfitPct'] = ((df['Retail'] - df['Wholesale']) / df['Wholesale'] * 100).round(1)

# Top 10 by profit
top = df.sort_values('Profit', ascending=False).head(10)
print('=== TOP 10 High Profit Cigarettes ===')
for i, row in top.iterrows():
    print(f"{row['Product'][:20]:20} | W:{row['Wholesale']:6.1f} | R:{row['Retail']:6.1f} | Profit:{row['Profit']:6.1f} ({row['ProfitPct']:.1f}%)")

# Statistics
print('\n=== Statistics ===')
print(f"Total products: {len(df)}")
print(f"Avg Wholesale: {df['Wholesale'].mean():.1f} yuan")
print(f"Avg Retail: {df['Retail'].mean():.1f} yuan")
print(f"Avg Profit: {df['Profit'].mean():.1f} yuan")
print(f"Avg Profit Rate: {df['ProfitPct'].mean():.1f}%")

# Products with BigPrice
print('\n=== Products with Big Buyer Price ===')
has_bp = df[df['BigPrice'].notna()].copy()
has_bp['Diff'] = has_bp['Retail'] - has_bp['BigPrice']
for i, row in has_bp.iterrows():
    print(f"{row['Product'][:20]:20} | Retail:{row['Retail']:6.1f} | Big:{row['BigPrice']:6.1f} | Diff:{row['Diff']:6.1f}")
