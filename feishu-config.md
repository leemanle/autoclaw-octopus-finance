# 飞书机器人配置指南

## 步骤 1: 在飞书开放平台创建机器人

1. 访问 [飞书开放平台](https://open.feishu.cn/)
2. 登录你的飞书账号
3. 点击"创建企业自建应用"
4. 填写应用信息：
   - **应用名称**：AutoClaw（或你喜欢的名字）
   - **应用描述**：AI 助手机器人
   - **应用图标**：上传一个图标
5. 点击"创建"

## 步骤 2: 获取必要凭证

创建完成后，进入应用详情页，获取以下信息：

### 2.1 App ID 和 App Secret
- 在左侧菜单点击 **"凭证与基础信息"**
- 复制以下内容：
  - **App ID**: `cli_axxxxxxxxxxxxxxx` (记录下来)
  - **App Secret**: 点击查看并复制 (记录下来)

### 2.2 机器人 UserID
- 在左侧菜单点击 **"机器人"**
- 点击 **"配置机器人"**
- 如果还没有机器人，点击 **"添加机器人"** → 选择 **"用户机器人"**
- 复制 **open_id** (格式类似 `ou_xxxxxxxxxxxxxxxxx`)

## 步骤 3: 配置权限

在飞书开放平台的 **"权限管理"** 中，申请以下权限：

### 必需权限
- ✅ **im:chat** - 查看群组与用户信息
- ✅ **im:message** - 发送和接收消息
- ✅ **im:message.group_at_msg** - 读取群组中被@的消息
- ✅ **im:resource** - 上传和下载文件
- ✅ **contact:user.base:readonly** - 获取用户基本信息
- ✅ **contact:group.base:readonly** - 获取群组基本信息

### 可选权限（根据需要）
- **drive:drive:readonly** - 读取云文档
- **drive:file:readonly** - 读取文件
- **wiki:wiki:readonly** - 读取知识库

## 步骤 4: 发布机器人

1. 在左侧菜单点击 **"版本管理与发布"**
2. 点击 **"创建版本"**
   - 填写版本号：`1.0.0`
   - 版本描述：初始版本
3. 点击右上角 **"申请发布"**
4. 选择发布范围：**"企业内可用"** 或 **"所有人可用"**
5. 点击 **"确认发布"**

## 步骤 5: 在飞书中测试

1. 打开飞书应用
2. 在搜索框中搜索你创建的应用名称（如"AutoClaw"）
3. 点击进入机器人对话框
4. 发送一条测试消息，确保机器人能接收

## 步骤 6: 配置 OpenClaw 连接

将你获取的信息填入下面的配置文件模板：

```yaml
# 文件位置：~/.openclaw-autoclaw/config/channels/feishu.yml

enabled: true

# 飞书应用凭证
appId: "cli_axxxxxxxxxxxxxxx"      # 从飞书开放平台获取
appSecret: "xxxxxxxxxxxxxxxx"       # 从飞书开放平台获取
encryptKey: ""                     # 留空（不使用加密）
verificationToken: ""              # 留空（不使用验证令牌）

# 机器人配置
robot:
  openId: "ou_xxxxxxxxxxxxxxxxx"   # 机器人的 open_id
  name: "AutoClaw"                  # 机器人显示名称

# 事件订阅
events:
  - type: "im.message.receive_v1"  # 接收消息事件

# 可选：Webhook 配置（如果使用事件订阅）
webhook:
  enabled: false                    # 是否启用 webhook
  url: ""                          # 你的公网 webhook 地址
  secret: ""                       # webhook 密钥
```

## 步骤 7: 验证配置

1. 保存配置文件
2. 重启 OpenClaw Gateway
3. 在飞书中发送消息给机器人
4. 如果配置成功，机器人应该能够响应

## 常见问题

### Q: 机器人无法接收消息？
**A:**
- 检查权限是否已全部通过审核
- 确认机器人已发布并启用
- 检查配置文件中的 `appId` 和 `appSecret` 是否正确

### Q: 机器人无法发送消息？
**A:**
- 确认 `im:message` 权限已通过审核
- 检查机器人已被添加到目标群组中

### Q: 如何将机器人添加到群组？
**A:**
1. 在飞书群组设置中，点击"添加群成员"
2. 搜索你的应用名称
3. 选择并添加机器人到群组

### Q: 需要公网服务器吗？
**A:**
如果你使用飞书的 **事件订阅**（Webhook），需要公网服务器。
如果你使用 **轮询模式**（Polling），则不需要（OpenClaw 支持轮询）。

## 下一步

配置完成后，你可以在飞书中：
- 直接对话机器人
- 将机器人添加到群组
- 使用 `@机器人` 触发回复

---

**需要帮助？**
- 飞书开放平台文档：https://open.feishu.cn/document/
- 飞书机器人开发指南：https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN
