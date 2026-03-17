# 飞书机器人完整配置指南

## 📋 目录
1. [飞书开放平台配置](#步骤1-飞书开放平台配置)
2. [获取凭证信息](#步骤2-获取凭证信息)
3. [配置权限](#步骤3-配置权限)
4. [发布机器人](#步骤4-发布机器人)
5. [OpenClaw 配置](#步骤5-openclaw-配置)
6. [测试连接](#步骤6-测试连接)
7. [常见问题](#常见问题)

---

## 步骤 1: 飞书开放平台配置

### 1.1 访问开放平台
- 打开浏览器访问：https://open.feishu.cn/
- 使用你的飞书账号登录

### 1.2 创建应用
1. 点击右上角 **"创建应用"**
2. 选择 **"企业自建应用"**
3. 填写应用信息：
   - **应用名称**：`AutoClaw`（或你喜欢的名字）
   - **应用描述**：`AI 智能助手，支持对话、文档操作、知识库查询等`
   - **应用图标**：上传一个图标（可选）
4. 点击 **"创建"**

### 1.3 应用创建成功
- 记录下你的 **App ID**，格式如：`cli_a1b2c3d4e5f6g7h8`
- 这个 App ID 稍后需要配置到 OpenClaw

---

## 步骤 2: 获取凭证信息

### 2.1 获取 App ID 和 App Secret
1. 在应用详情页，点击左侧菜单 **"凭证与基础信息"**
2. 你会看到：
   ```
   App ID: cli_a1b2c3d4e5f6g7h8
   App Secret: ••••••••••••••••
   ```
3. 点击 **App Secret** 旁边的 **"查看"** 按钮
4. 复制完整的 App Secret 字符串
5. **重要**：将 `App ID` 和 `App Secret` 保存到安全的地方

### 2.2 获取机器人 open_id
1. 点击左侧菜单 **"机器人"**
2. 如果还没有机器人，点击 **"添加机器人"**
3. 选择 **"用户机器人"**
4. 点击 **"配置机器人"**
5. 在页面中找到 **open_id**，格式如：`ou_xxxxxxxxxxxxxxxxx`
6. 复制这个 open_id

### ✅ 检查清单
- [ ] 已记录 App ID
- [ ] 已记录 App Secret
- [ ] 已记录机器人 open_id

---

## 步骤 3: 配置权限

### 3.1 打开权限管理
- 在应用详情页，点击左侧菜单 **"权限管理"**

### 3.2 申请必需权限
在权限管理页面，搜索并申请以下权限：

#### 消息相关权限
| 权限名称 | 权限标识 | 说明 | 必需 |
|---------|---------|------|------|
| 查看群组与用户信息 | `im:chat` | 获取用户和群组基本信息 | ✅ 是 |
| 发送和接收消息 | `im:message` | 机器人发送和接收消息 | ✅ 是 |
| 读取群组中被@的消息 | `im:message.group_at_msg` | 读取群组@消息 | ✅ 是 |
| 上传和下载文件 | `im:resource` | 发送文件、图片等 | ✅ 是 |

#### 联系人相关权限
| 权限名称 | 权限标识 | 说明 | 必需 |
|---------|---------|------|------|
| 获取用户基本信息 | `contact:user.base:readonly` | 获取发送者信息 | ✅ 是 |
| 获取群组基本信息 | `contact:group.base:readonly` | 获取群组信息 | ✅ 是 |

#### 文档相关权限（可选）
| 权限名称 | 权限标识 | 说明 | 必需 |
|---------|---------|------|------|
| 读取云文档 | `drive:drive:readonly` | 读取飞书文档 | ⭕ 否 |
| 读取文件 | `drive:file:readonly` | 读取文件 | ⭕ 否 |
| 读取知识库 | `wiki:wiki:readonly` | 读取知识库 | ⭕ 否 |

### 3.3 提交权限申请
1. 选择需要的权限（勾选上述必需权限）
2. 点击 **"申请权限"**
3. 等待审核通过（通常即时通过）

---

## 步骤 4: 发布机器人

### 4.1 创建版本
1. 点击左侧菜单 **"版本管理与发布"**
2. 点击 **"创建版本"**
3. 填写版本信息：
   - **版本号**：`1.0.0`
   - **版本描述**：`初始版本，支持基础对话功能`
4. 点击 **"确定"**

### 4.2 发布应用
1. 点击右上角 **"申请发布"**
2. 选择发布范围：
   - **"企业内可用"**：仅企业内成员可使用
   - **"所有人可用"**：所有飞书用户都可使用
3. 选择 **"企业内可用"**（推荐）
4. 点击 **"确认发布"**
5. 等待发布完成（通常 1-2 分钟）

### 4.3 验证机器人可用
1. 打开飞书客户端
2. 在搜索框中搜索你的应用名称（如 `AutoClaw`）
3. 点击进入机器人对话框
4. 发送一条测试消息：`你好`
5. 如果能发送消息，说明机器人已成功发布

---

## 步骤 5: OpenClaw 配置

### 5.1 定位配置文件
OpenClaw 的配置文件通常位于以下位置之一：

#### Windows 系统
```
C:\Users\Administrator\AppData\Roaming\AutoClaw\config\channels\feishu.yml
```

#### 或工作区配置
```
C:\Users\Administrator\.openclaw-autoclaw\workspace\channels\feishu.yml
```

### 5.2 创建/编辑配置文件
如果配置文件不存在，创建 `feishu.yml` 文件并填入以下内容：

```yaml
# 飞书（Lark）机器人配置
enabled: true

# 飞书应用凭证（从飞书开放平台获取）
appId: "cli_a1b2c3d4e5f6g7h8"      # 替换为你的 App ID
appSecret: "xxxxxxxxxxxxxxxx"       # 替换为你的 App Secret

# 机器人配置
robot:
  openId: "ou_xxxxxxxxxxxxxxxxx"   # 替换为机器人的 open_id
  name: "AutoClaw"                  # 机器人的显示名称

# 加密配置（通常留空）
encryptKey: ""
verificationToken: ""

# 事件订阅配置（Webhook 模式）
events:
  enabled: false                    # 通常使用轮询模式
  url: ""
  secret: ""

# 轮询配置（推荐，无需公网服务器）
polling:
  enabled: true                     # 启用轮询模式
  interval: 3000                    # 轮询间隔：3 秒

# 功能开关
features:
  receiveMessages: true
  sendMessages: true
  replyMentions: true
  supportGroups: true
  supportDirect: true

# 日志配置
logging:
  enabled: true
  level: "info"
```

### 5.3 配置说明

#### 重要参数解释

| 参数 | 说明 | 示例 |
|-----|------|------|
| `enabled` | 是否启用飞书频道 | `true` 或 `false` |
| `appId` | 飞书应用 ID | `cli_a1b2c3d4e5f6g7h8` |
| `appSecret` | 飞书应用密钥 | 长字符串，保密 |
| `robot.openId` | `机器人 open_id` | `ou_xxxxxxxxxxxxxxxxx` |
| `polling.enabled` | 使用轮询模式 | `true`（推荐） |
| `polling.interval` | 轮询间隔（毫秒） | `3000`（3秒） |

#### Webhook 模式 vs 轮询模式

**Webhook 模式**（需要公网服务器）
- ✅ 实时性更好
- ❌ 需要公网可访问的服务器
- ❌ 需要配置域名和 SSL

**轮询模式**（推荐用于个人使用）
- ✅ 无需公网服务器
- ✅ 配置简单
- ⚠️ 实时性稍差（最多延迟 3 秒）

### 5.4 保存配置
- 将配置文件保存到正确位置
- 确保 `appId`、`appSecret`、`openId` 都已正确填写
- 确保 `enabled: true`

---

## 步骤 6: 测试连接

### 6.1 重启 OpenClaw
1. 如果 OpenClaw 正在运行，先关闭
2. 重新启动 OpenClaw

### 6.2 测试私聊
1. 打开飞书客户端
2. 搜索并打开机器人对话框
3. 发送测试消息：`你好`
4. 等待机器人回复（轮询模式最多 3 秒延迟）

### 6.3 测试群组（可选）
1. 创建一个测试群组或使用现有群组
2. 添加机器人到群组
3. 在群组中 @机器人 发送消息：`@AutoClaw 你好`
4. 等待机器人回复

### ✅ 成功标志
- 机器人能够接收消息
- 机器人能够回复消息
- 没有报错日志

---

## 常见问题

### Q1: 配置文件应该放在哪里？
**A:** 根据你的 OpenClaw 版本，配置文件可能在以下位置：
- `C:\Users\Administrator\AppData\Roaming\AutoClaw\config\channels\feishu.yml`
- `C:\Users\Administrator\.openclaw-autoclaw\workspace\channels\feishu.yml`

建议检查这两个位置。

### Q2: 机器人无法接收消息？
**A:** 检查以下几点：
1. 权限是否已全部申请并通过审核
2. 机器人是否已发布
3. 配置文件中 `enabled` 是否为 `true`
4. App ID 和 App Secret 是否正确

### Q3: 机器人接收消息但不回复？
**A:** 检查以下几点：
1. 是否有 `im:message` 权限
2. OpenClaw 服务是否正常运行
3. 查看日志文件是否有错误信息

### Q4: 需要公网服务器吗？
**A:** 如果你使用**轮询模式**（推荐），不需要公网服务器。
如果使用 Webhook 模式，则需要公网可访问的 URL。

### Q5: 如何查看 OpenClaw 日志？
**A:** 日志文件通常位于：
```
C:\Users\Administrator\.openclaw-autoclaw\logs\
```
查看最近的日志文件，寻找飞书相关的错误信息。

### Q6: 权限申请被拒绝怎么办？
**A:**
1. 确认你的企业账号有足够权限
2. 某些权限需要企业管理员审批
3. 如果是个人账号，使用"企业内可用"的发布范围

### Q7: 如何将机器人添加到群组？
**A:**
1. 在飞书群组设置中，点击"添加成员"
2. 搜索你的机器人名称（如 `AutoClaw`）
3. 选择并添加

### Q8: 机器人消息延迟很高？
**A:**
- 轮询模式：检查 `polling.interval` 设置，默认 3000ms（3秒）
- Webhook 模式：检查服务器响应速度

---

## 📚 参考文档

- [飞书开放平台](https://open.feishu.cn/)
- [飞书机器人开发指南](https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN)
- [飞书 API 文档](https://open.feishu.cn/document/ukTMukTMukTM/uATMzYDN1TNzMzE1)
- [OpenClaw 文档](https://docs.openclaw.ai)

---

## 🎉 完成！

恭喜！你现在应该已经成功配置了飞书机器人。如果遇到问题，请查看日志文件或参考上面的常见问题部分。

**下一步：**
1. 在飞书中与机器人对话
2. 将机器人添加到你的工作群组
3. 探索更多功能和技能
