# SKILL-LEARNER.md - 已学习技能记录

## 2026-03-14 学习的技能

### 🎬 自媒体短视频自动制作 (video-creator)
- **功能**: 从选题到成片的完整短视频自动化流程
- **核心能力**:
  - 自动获取热点话题/财经资讯
  - 生成短视频脚本
  - 搜索下载免费视频素材
  - AI中文配音
  - 视频合成
- **依赖**: ffmpeg, yt-dlp, edge-tts, moviepy
- **状态**: ✅ 已安装到 workspace/.opencode/skills/video-creator/

### 📰 新闻视频素材免费资源大全 (news-video-resources)
- **功能**: 整理全球免费可商用新闻视频素材网站
- **支持的素材库**:
  - Pexels Videos (CC0, 免费商用)
  - Pixabay (CC0)
  - Coverr (电影级素材)
  - Videvo
  - Mixkit
- **下载工具**: yt-dlp
- **状态**: ✅ 已安装到 workspace/.opencode/skills/news-video-resources/

### 🌐 AutoGLM 浏览器自动化代理 (autoglm-browser-agent)
- **功能**: 智能浏览器自动化，支持各种网页操作
- **核心能力**:
  - 搜索信息 (百度/谷歌/必应)
  - 浏览社交媒体 (微博/小红书/知乎/抖音/B站)
  - 点赞/评论/转发/收藏
  - 发帖/发消息
  - 登录网站/填写表单
  - 截图/采集网页内容
  - 在线购物比价
  - 操作在线文档 (飞书/腾讯文档)
- **依赖**: 浏览器扩展 + MCP Server
- **状态**: ✅ 已验证可用！成功打开并操作了百度、新浪财经、东方财富、抖音等网站

### 🔍 AutoGLM 网络搜索 (autoglm-websearch)
- **功能**: 使用 AutoGLM Web Search API 进行网络搜索
- **能力**: 联网搜索、查询最新资讯、检索网页内容
- **Token获取**: 自动从 http://127.0.0.1:53699/get_token 获取
- **状态**: ✅ 已了解技能详情

### 💰 东方财富金融数据 (eastmoney-financial-data)
- **功能**: 查询股票、板块、指数、基金、债券的实时行情、财务数据等
- **API**: https://mkapi2.dfcfs.com/finskillshub/api/claw/query
- **需要**: EASTMONEY_APIKEY 环境变量
- **获取API Key**: https://marketing.dfcfs.com/views/finskillshub/indexuNdYscEA
- **状态**: ✅ 已安装到 workspace/.opencode/skills/eastmoney-financial-data/

## 已验证的爬虫能力

### ✅ 成功抓取的网站
- 新浪财经 (finance.sina.com.cn)
- 东方财富 (eastmoney.com)
- 同花顺 (10jqka.com.cn)
- 澎湃新闻 (thepaper.cn)
- 百度搜索
- 抖音热榜

## 技能依赖安装

需要安装的Python依赖：
```bash
pip install yt-dlp edge-tts moviepy requests beautifulsoup4 selenium webdriver-manager
```

## 使用场景

1. **视频制作**: video-creator + news-video-resources
2. **浏览器自动化**: autoglm-browser-agent - 已验证可用！
3. **网络搜索**: autoglm-websearch
4. **金融数据查询**: eastmoney-financial-data - 需要API Key
