---
name: eastmoney_financial_data
description: 本 Skill 基于东方财富权威数据库及最新行情底层数据构建，支持通过自然语言查询行情类数据（股票、行业、板块、指数、基金、债券的实时行情、主力资金流向、估值等）、财务类数据（上市公司基本信息、财务指标、高管信息、主营业务等）、关系与经营类数据（关联关系、企业经营数据）。避免模型基于过时知识回答金融数据问题，提供权威及时的金融数据。
required_env_vars:
  - EASTMONEY_APIKEY
credentials:
  - type: api_key
    name: EASTMONEY_APIKEY
    description: 从东方财富技能市场 (https://marketing.dfcfs.com/views/finskillshub/indexuNdYscEA?appfenxiang=1) 获取的 API Key
---

# 东方财富金融数据skill (eastmoney_financial_data)

通过**文本输入**查询金融相关数据（股票、板块、指数等），接口返回 JSON格式内容。

## 使用方式

1. 首先检查环境变量`EASTMONEY_APIKEY`是否存在：
   ```bash
   echo $EASTMONEY_APIKEY
   ```

   如果不存在，提示用户在东方财富Skills页面(https://marketing.dfcfs.com/views/finskillshub/indexuNdYscEA?appfenxiang=1)获取apikey并设置到环境变量。

   > ⚠️ **安全注意事项**
   >
   > - **外部请求**: 本 Skill 会将您的查询文本发送至东方财富官方 API 域名 ( `mkapi2.dfcfs.com` ) 以获取金融数据。
   > - **凭据保护**: API Key 仅通过环境变量 `EASTMONEY_APIKEY` 在服务端或受信任的运行环境中使用，不会在前端明文暴露。

2. 使用POST请求调用接口：
   ```bash
   curl -X POST --location 'https://mkapi2.dfcfs.com/finskillshub/api/claw/query' \
   --header 'Content-Type: application/json' \
   --header "apikey: $EASTMONEY_APIKEY" \
   --data '{"toolQuery":"用户的查询内容"}'
   ```

## 适用场景

当用户查询以下类型的内容时使用本skill：

- **行情类数据**：股票、行业、板块、指数、基金、债券的实时行情、主力资金流向、估值等数据
- **财务类数据**：上市公司与非上市公司的基本信息、财务指标、高管信息、主营业务、股东结构、融资情况等数据
- **关系与经营类数据**：股票、非上市公司、股东及高管之间的关联关系数据，以及企业经营相关数据

## 数据限制说明

请谨慎查询大数据范围的数据，如某只股票3年的每日最新价，可能会导致返回内容过多，模型上下文爆炸问题。

## 示例

```python
import os
import requests

api_key = os.getenv("EASTMONEY_APIKEY")
if not api_key:
    raise ValueError("请先设置EASTMONEY_APIKEY环境变量")

url = "https://mkapi2.dfcfs.com/finskillshub/api/claw/query"
headers = {
    "Content-Type": "application/json",
    "apikey": api_key
}
data = {
    "toolQuery": "东方财富最新价"
}

response = requests.post(url, headers=headers, json=data)
response.raise_for_status()
result = response.json()
print(result)
```

## 异常处理

- 如果数据结果为空，提示用户到东方财富妙想AI查询
- 如果请求失败，检查API Key是否正确，网络是否正常
