# RPA 财经数据采集流程

## 概述
使用 RPA + API 混合方式采集财经数据

## 数据源（已验证可用）

| 数据源 | 类型 | 状态 | URL |
|--------|------|------|-----|
| 腾讯财经 | API | ✅ 可用 | web.ifzq.gtimg.cn |
| 东方财富 | 网页 | ⚠️ 需测试 | data.eastmoney.com |
| 财联社 | 网页 | ⚠️ 需测试 | cls.cn/telegraph |

## 流程

### 第一步：获取沪深指数
```python
# 腾讯财经API（已验证可用）
curl "https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=sh000001,day,,,1,qfq"
```

### 第二步：获取快讯（财联社）
```browser
打开: https://www.cls.cn/telegraph
等待5秒
提取元素: .telegraph-item
```

### 第三步：获取龙虎榜（东方财富）
```browser
打开: http://data.eastmoney.com/stock/tradedata.html
等待8秒
提取表格: #contTbody tr
```

### 第四步：生成报告
```python
# 写入JSON文件
{
  "timestamp": "2026-03-17 13:30:00",
  "market": {
    "sh_index": 4078.08,
    "sz_index": "...",
  }
}
```

### 第五步：发送飞书
```python
# 使用 message 工具发送
```

## 执行命令
说"运行财经数据采集"执行此流程
