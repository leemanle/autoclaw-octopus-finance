# 桌面炒股软件自动化控制方案

## 技术可行性分析

是的，**可以**控制你的同花顺、大智慧等桌面版软件，并实时读取数据进行选股。

## 核心技术方案

### 方案 1: pywinauto（推荐 - Windows 专用）

**优势：**
- 原生 Windows UI 自动化
- 支持窗口操作、控件识别、文本提取
- 可模拟鼠标点击、键盘输入
- 适合中国本土软件

**实现步骤：**
```python
import pywinauto
from pywinauto import application
from pywinauto.keyboard import send_keys
import time
import pandas as pd

# 1. 启动或连接到同花顺
app = application.Application().connect(path='同花顺.exe')

# 2. 获取主窗口
main_window = app.window(title='同花顺')

# 3. 导航到指定股票
main_window.set_focus()
send_keys('^f')  # Ctrl+F 搜索
main_window.child_window(class_name='Edit').set_text('000001')
send_keys('{ENTER}')

# 4. 切换到K线或分时图
# 根据实际界面布局定位控件

# 5. 截图并提取数据
from PIL import ImageGrab
screenshot = ImageGrab.grab()
```

### 方案 2: PyAutoGUI（跨平台）

**优势：**
- 跨平台（Windows/macOS/Linux）
- 简单易用
- 基于坐标的鼠标键盘操作

```python
import pyautogui
import time

# 点击指定位置
pyautogui.click(x=100, y=200)

# 输入文字
pyautogui.write('平安银行')

# 滚动页面
pyautogui.scroll(-10)

# 截图
screenshot = pyautogui.screenshot()
```

### 方案 3: OCR + 计算机视觉（智能识别）

**优势：**
- 可识别界面中的数字、文字
- 不依赖控件结构
- 更灵活的数据提取

```python
import pytesseract
from PIL import Image
import cv2

# 截图
screenshot = pyautogui.screenshot()

# OCR 识别
text = pytesseract.image_to_string(screenshot, lang='chi_sim+eng')
print(text)

# 识别特定区域
roi = screenshot.crop((x1, y1, x2, y2))
price = pytesseract.image_to_string(roi)
```

## 完整选股流程设计

### 第一步：安装依赖

```powershell
# 主 Python 环境安装
pip install pywinauto psutil Pillow pyautogui opencv-python pytesseract

# Tesseract OCR 引擎（需要单独安装）
# 下载地址：https://github.com/UB-Mannheim/tesseract/wiki
```

### 第二步：启动并连接目标软件

```python
import pywinauto
import psutil

def launch_trading_software(software_name='同花顺'):
    """启动或连接到交易软件"""

    # 检查进程是否已运行
    for proc in psutil.process_iter(['name']):
        if software_name in proc.info['name']:
            print(f'{software_name} 已运行')
            # 连接到现有进程
            app = pywinauto.Application().connect(
                process=proc.pid,
                timeout=10
            )
            return app

    # 否则启动新进程
    # app = pywinauto.Application().start(f'{software_name}.exe')
    print('请手动启动交易软件')
    return None

app = launch_trading_software('同花顺')
```

### 第三步：定义选股条件

```python
class StockSelector:
    def __init__(self):
        self.stocks = []
        self.conditions = {
            'min_price': 5,
            'max_price': 50,
            'min_volume': 1000000,
            'min_pe': 0,
            'max_pe': 30,
            'trend': 'uptrend'  # uptrend, downtrend, any
        }

    def check_conditions(self, stock_data):
        """检查股票是否符合选股条件"""
        # 价格范围
        if not (self.conditions['min_price'] <= stock_data['price'] <= self.conditions['max_price']):
            return False

        # 成交量
        if stock_data['volume'] < self.conditions['min_volume']:
            return False

        # 市盈率
        if not (self.conditions['min_pe'] <= stock_data['pe'] <= self.conditions['max_pe']):
            return False

        # 趋势判断
        if self.conditions['trend'] == 'uptrend':
            if stock_data['ma5'] < stock_data['ma20']:
                return False

        return True
```

### 第四步：扫描和提取数据

```python
def scan_market_screener(app):
    """扫描市场选股器"""
    # 导航到"选股器"功能
    main_window = app.window(title='同花顺')

    # 执行选股
    # 等待结果加载

    # 提取股票列表
    stocks = []

    # 使用表格控件或 OCR 识别
    # ...

    return stocks

def extract_stock_data(app, stock_code):
    """提取单只股票的详细数据"""
    # 输入股票代码
    # ...

    # 提取关键指标
    data = {
        'code': stock_code,
        'name': '',  # 股票名称
        'price': 0,  # 当前价格
        'change': 0,  # 涨跌幅
        'volume': 0,  # 成交量
        'pe': 0,  # 市盈率
        'ma5': 0,  # 5日均线
        'ma20': 0,  # 20日均线
        # ... 更多指标
    }

    return data
```

### 第五步：自动选股执行

```python
def auto_select_stocks(software='同花顺'):
    """自动选股主流程"""
    print('=== 自动选股系统启动 ===')

    # 1. 连接交易软件
    app = launch_trading_software(software)
    if not app:
        return

    # 2. 初始化选股器
    selector = StockSelector()

    # 3. 获取股票池（可选：扫描指定板块/行业）
    # 这里可以手动指定或自动扫描

    # 示例：手动扫描几只测试股票
    test_stocks = ['000001', '000002', '600000', '600036']

    selected_stocks = []

    # 4. 逐个检查
    for code in test_stocks:
        print(f'正在检查: {code}...')

        try:
            # 提取数据
            data = extract_stock_data(app, code)

            # 检查条件
            if selector.check_conditions(data):
                print(f'✅ 符合条件: {data["name"]} ({code})')
                selected_stocks.append(data)
            else:
                print(f'❌ 不符合条件: {code}')

            # 等待避免过快
            time.sleep(0.5)

        except Exception as e:
            print(f'❌ 检查失败 {code}: {e}')

    # 5. 输出结果
    print(f'\n=== 选股完成 ===')
    print(f'符合条件股票数: {len(selected_stocks)}')

    for stock in selected_stocks:
        print(f"- {stock['name']} ({stock['code']}): "
              f"价格 {stock['price']}, 涨跌幅 {stock['change']}%, "
              f"市盈率 {stock['pe']}")

    return selected_stocks
```

## 实时监控方案

### 定时扫描模式

```python
import schedule
import time

def job():
    """定时任务"""
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 开始选股...")
    auto_select_stocks()

# 每分钟执行一次
schedule.every(1).minutes.do(job)

# 每5分钟执行一次
# schedule.every(5).minutes.do(job)

# 每天上午9:30执行
# schedule.every().day.at('09:30').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

### 数据预警

```python
def monitor_and_alert(app, watch_list, conditions):
    """监控指定股票并预警"""
    import win10toast  # Windows 通知

    toaster = win10toast.ToastNotifier()

    while True:
        for code in watch_list:
            data = extract_stock_data(app, code)

            # 检查触发条件
            if data['change'] > 9.5:  # 涨停预警
                toaster.show_toast(
                    '涨停预警',
                    f'{data["name"]} 涨停！价格: {data["price"]}',
                    duration=5
                )

        time.sleep(60)  # 每分钟检查
```

## 注意事项

### 1. 软件差异
- **同花顺**：结构相对稳定，pywinauto 识别度高
- **大智慧**：可能需要结合 OCR
- **通达信**：定制化强，建议研究其脚本语言

### 2. 稳定性考虑
- 软件界面可能随版本更新变化
- 需要加入异常处理和重试机制
- 重要操作建议人工确认

### 3. 数据准确性
- OCR 识别率不是 100%
- 关键数字建议校验
- 对比多个数据源

### 4. 风险控制
- 不要完全依赖自动交易
- 设置止损止盈
- 实时监控异常情况

## 快速开始

### 安装准备

1. **安装 Tesseract OCR**
   - 下载：https://github.com/UB-Mannheim/tesseract/wiki
   - 安装后记下安装路径

2. **安装 Python 包**
```powershell
pip install pywinauto psutil Pillow pyautogui opencv-python pytesseract win10toast schedule
```

3. **测试连接**
```python
python trading_automation.py test
```

## 需要我帮你做什么？

1. **编写完整控制脚本**（包括具体软件的界面定位）
2. **实现特定选股策略**（根据你的条件定制）
3. **设置实时监控**（涨跌预警、条件触发）
4. **优化数据提取**（OCR 识别、表格解析）

告诉我你的需求，我立即为你实现！
