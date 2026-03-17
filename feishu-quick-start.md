# 飞书机器人快速启动清单

## 🔑 需要从飞书开放平台获取的 3 个关键信息

1. **App ID**（格式：`cli_a1b2c3d4e5f6g7h8`）
   - 位置：凭证与基础信息
   - 用途：标识你的飞书应用

2. **App Secret**（长字符串）
   - 位置：凭证与基础信息 → 点击"查看"
   - 用途：API 调用认证

3. **机器人 open_id**（格式：`ou_xxxxxxxxxxxxxxxxx`）
   - 位置：机器人 → 配置机器人
   - 用途：机器人身份标识

---

## 📝 快速配置步骤

### 第 1 步：创建飞书应用（5 分钟）
1. 访问 https://open.feishu.cn/
2. 登录你的飞书账号
3. 创建"企业自建应用"
4. 命名为：`AutoClaw`

### 第 2 步：获取凭证（2 分钟）
1. 进入"凭证与基础信息"
2. 复制 App ID：`_____________`
3. 点击"查看"，复制 App Secret：`_____________`
4. 进入"机器人"，配置机器人，复制 open_id：`_____________`

### 第 3 步：申请权限（2 分钟）
申请以下必需权限：
- ✅ `im:chat` - 查看群组与用户信息
- ✅ `im:message` - 发送和接收消息
- ✅ `im:message.group_at_msg` - 读取群组@消息
- ✅ `im:resource` - 上传和下载文件
- ✅ `contact:user.base:readonly` - 获取用户基本信息
- ✅ `contact:group.base:readonly` - 获取群组基本信息

### 第 4 步：发布机器人（1 分钟）
1. 进入"版本管理与发布"
2. 创建版本：`1.0.0`
3. 发布到：`企业内可用`
4. 等待发布完成

### 第 5 步：配置 OpenClaw（3 分钟）
编辑配置文件 `feishu.yml`：

```yaml
enabled: true

appId: "cli_a1b2c3d4e5f6g7h8"      # ← 替换为你的 App ID
appSecret: "xxxxxxxxxxxxxxxx"       # ← 替换为你的 App Secret

robot:
  openId: "ou_xxxxxxxxxxxxxxxxx"   # ← 替换为 open_id
  name: "AutoClaw"

encryptKey: ""
verificationToken: ""

events:
  enabled: false
  url: ""
  secret: ""

polling:
  enabled: true
  interval: 3000
```

保存配置文件到以下任一位置：
- `C:\Users\Administrator\AppData\Roaming\AutoClaw\config\channels\feishu.yml`
- `C:\Users\Administrator\.openclaw-autoclaw\workspace\channels\feishu.yml`

### 第 6 步：测试连接（1 分钟）
1. 重启 OpenClaw
2. 在飞书中搜索并打开机器人
3. 发送消息：`你好`
4. 等待回复（最多 3 秒延迟）

---

## ✅ 完成检查清单

- [ ] 飞书应用已创建
- [ ] 已获取 App ID
- [ ] 已获取 App Secret
- [ ] 已获取机器人 open_id
- [ ] 权限已申请并通过审核
- [ ] 机器人已发布
- [ ] OpenClaw 配置文件已编辑
- [ ] OpenClaw 已重启
- [ ] 机器人能够接收消息
- [ ] 机器人能够回复消息

---

## 🎯 配置文件位置

根据你的 OpenClaw 安装方式，配置文件可能位于以下位置之一：

| 位置 | 说明 |
|-----|------|
| `C:\Users\Administrator\AppData\Roaming\AutoClaw\config\channels\feishu.yml` | AutoClaw 客户端配置 |
| `C:\Users\Administrator\.openclaw-autoclaw\workspace\channels\feishu.yml` | 工作区配置 |

**推荐使用第一个位置**（AutoClaw 客户端配置），如果该目录不存在，请创建：
```
C:\Users\Administrator\AppData\Roaming\AutoClaw\config\channels\
```

---

## 🚀 下一步

配置完成后，你可以：
1. 在飞书中与机器人私聊
2. 将机器人添加到群组
3. 使用各种技能（文档操作、搜索、等等）

---

## 💡 提示

- **App Secret** 是敏感信息，请妥善保管
- 使用**轮询模式**（polling.enabled=true）无需公网服务器
- 如果遇到问题，查看日志文件：`C:\Users\Administrator\.openclaw-autoclaw\logs\`
- 详细配置指南请查看：`feishu-setup-guide.md`
