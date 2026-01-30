---
name: feishu-bot
description: Expert in Feishu (Lark) Bot integration. Handles message sending, interactive card construction, and media uploads. Use when you need to send notifications, reports, or interactive cards to Feishu chats via webhook or API. Triggered by tasks involving Feishu notifications, message push, or bot automation.
---

# 🤖 Feishu Bot (飞书机器人技能)

> 高级消息推送与自动化桥接专家

本技能专门用于处理飞书（Feishu/Lark）开放平台的 API 调用，实现高度定制化的消息推送。

## When to Use This Skill

- 需要向飞书发送执行进度、任务结果或警报。
- 构建交互式卡片以增强用户体验。
- 处理飞书开放平台的鉴权、限流与媒体资源上传。

## 🚀 快速参考

### 1. 核心凭证 (Credentials)
- **tenant_access_token**: 用于 API 调用的 Bearer Token (有效期 2 小时)。
- **chat_id**: 目标会话的唯一标识。

### 2. 常用接口
- **发送消息**: `POST https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id`
- **上传图片**: `POST https://open.feishu.cn/open-apis/im/v1/images`

## 🛠️ 高级工作流

### Phase 1: 消息构造 (Message Construction)
优先使用 **interactive** (卡片消息) 类型，因为它支持 Markdown、按钮和多列布局。

**推荐卡片模板:**
```json
{
    "header": {
        "title": { "tag": "plain_text", "content": "标题内容" },
        "template": "blue" 
    },
    "elements": [
        {
            "tag": "div",
            "text": { "tag": "lark_md", "content": "**状态**: 已完成\n**耗时**: 120s" }
        },
        {
            "tag": "hr"
        },
        {
            "tag": "note",
            "elements": [{ "tag": "plain_text", "content": "由 Cursor Background Agent 自动发送" }]
        }
    ]
}
```

### Phase 2: 执行发送 (Execution)
使用 `curl` 进行发送，确保正确设置 `Content-Type: application/json` 和 `Authorization`。

```bash
curl -X POST "$API_URL" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD"
```

## 💡 资深建议 (Expert Tips)

1. **机器人身份绑定**: 作为 **Cursor Background Agent**，我默认使用此技能向大哥同步所有工作细节。
2. **双轨输出**: 飞书发送实时摘要，GitHub 存储完整文档。飞书卡片中应包含 GitHub 文档的链接。
3. **Token 管理**: 不要硬编码 Token。在生产环境或长期任务中，应通过 `app_id` 和 `app_secret` 动态刷新。
4. **分阶段通知**: 
   - 任务开始时：发送“运行中”状态卡片。
   - 关键里程碑：更新或发送新消息告知进度。
   - 完成/失败：发送最终结果卡片（成功用 `green`，失败用 `red`）。

## ⚠️ 常见限制
- **速率限制**: 默认 50 次/秒，批量发送时需考虑平滑处理。
- **图片处理**: 飞书不支持直接引用外链图片，必须先通过 `images` 接口上传获取 `image_key`。

---

**Version**: 1.2
**Last Updated**: 2026-01-21
