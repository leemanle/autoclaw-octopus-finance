# Tushare Skills 安装指南

## 当前状态

- ✅ Python 环境已就绪
- ✅ Tushare 包已安装 (v1.4.25)
- ✅ Skills 目录已创建
- ⚠️ 需要手动复制 SKILL.md 文件

## 手动安装步骤

### 步骤 1: 下载 Tushare Skills 源码

访问以下任一链接下载 zip 文件：

- GitHub: https://github.com/waditu-tushare/skills/archive/refs/heads/main.zip
- Gitee: https://gitee.com/lwdt/skills/repository/archive/master.zip

### 步骤 2: 解压并复制

将下载的 zip 文件解压，将 `SKILL.md` 文件复制到：

```
C:\Users\Administrator\.agents\skills\tushare-data\SKILL.md
```

SKILL.md 内容如下（可直接保存）：

```markdown
# Tushare Skills

专注领域：中国金融数据（股票、基金、期货、宏观经济等）
触发场景：提到股票行情、财务数据、指数数据、宏观经济、基金信息、期货数据，或直接用自然语言查询金融数据

## 技能说明

Tushare Skills 是一个专门为中国金融数据分析设计的超能力包，让 AI 助手能够实时获取股票、基金、期货、宏观经济等各类金融数据。

### 核心能力

- 💬 **自然语言交互** - 直接用中文描述需求即可获取数据
- 📊 **丰富的数据类型** - 股票、财务、指数、宏观经济等
- 🚀 **开箱即用** - AI Skill 即插即用
- 📚 **完整的接口文档** - 包含 235+ Tushare API 接口

## 安装与配置

### 1. 安装 Tushare Python 包

```bash
pip install tushare -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2. 获取 Tushare Token

访问 [Tushare Pro](https://tushare.pro/register) 注册账号并获取 API Token

### 3. 配置 Token

在 Windows PowerShell 中设置环境变量：

```powershell
$env:TUSHARE_TOKEN = "your_token_here"
```

或者在交互时直接提供 token。

## 使用场景示例

### 股票数据查询

- "获取平安银行最近 30 天的股价数据"
- "查询茅台股票的实时行情"
- "帮我查找所有银行股并分析最近表现"

### 财务分析

- "查看招商银行最近的财务报表，分析营收和净利润"
- "对比腾讯和阿里的最新财务指标"
- "分析某公司的盈利能力趋势"

### 指数数据

- "获取上证指数最近的行情数据"
- "查看沪深300指数的历史走势"

### 宏观经济数据

- "查询最近一年的 GDP 和 CPI 数据"
- "获取最新的货币供应量数据"
- "查看最近的社会融资规模"

### 基金与期货

- "查看某基金的净值走势"
- "查询近期热门期货品种的行情"

## 数据接口支持

支持 220+ 个金融数据接口，包括但不限于：

- **股票行情**: daily, daily_basic, adj_factor 等
- **财务数据**: income, balancesheet, cashflow, fina_indicator 等
- **参考数据**: trade_cal, namechange, new_share 等
- **宏观经济**: gdp, cpi, ppi, m 等
- **指数行情**: index_daily, index_dailybasic 等
- **市场数据**: margin, moneyflow_hsgt 等
- **基金数据**: fund_etf_basic, fund_daily 等
- **期货数据**: fut_daily, fut_open_interest 等

完整接口文档: https://tushare.pro/document/2

## 注意事项

- 本技能仅供学习和研究使用
- 请遵守 Tushare 的使用条款和服务协议
- 不同积分等级可调用的数据接口不同
- 建议在获取大量数据前先了解接口的限制

## 官方资源

- Tushare 官网: https://tushare.pro
- 文档中心: https://tushare.pro/document
- GitHub 仓库: https://github.com/waditu-tushare/skills
```

### 步骤 3: 配置 Tushare Token

1. 访问 https://tushare.pro/register 注册账号
2. 进入个人中心获取 Token
3. 设置环境变量（可选，或在对话时提供）

```powershell
# 临时设置（当前会话有效）
$env:TUSHARE_TOKEN = "your_token_here"

# 永久设置（添加到系统环境变量）
[System.Environment]::SetEnvironmentVariable('TUSHARE_TOKEN', 'your_token_here', 'User')
```

## 验证安装

完成安装后，在 OpenClaw 中尝试以下命令：

- "获取平安银行最近 10 天的股价数据"
- "查询上证指数最新的行情"

如果能正常返回数据，说明安装成功！

## 支持的数据类型

- 股票行情、财务报表、指数数据
- 宏观经济（GDP、CPI、货币供应量等）
- 基金数据、期货数据
- 市场情绪、资金流向等

## 故障排查

如果遇到问题：

1. 确认 Tushare Token 已正确设置
2. 检查网络连接
3. 查看积分等级是否足够
4. 检查 SKILL.md 文件是否正确放置
