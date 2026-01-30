---
name: your-skill-name
description: Brief description of what this skill does and when to activate it. Include trigger keywords and scenarios where this skill should be used.
---

# Your Skill Title

> Brief one-line summary of what this skill accomplishes

## When to Use This Skill

- User asks to [specific action or task]
- User mentions keywords like "[keyword1]", "[keyword2]", or "[keyword3]"
- User is working with [specific technology/framework/tool]
- User needs to [specific outcome or goal]

## Quick Start

```bash
# Basic usage example
command-to-run --option value
```

## How It Works

1. **Step 1**: Brief description of first step
   - Detail about what happens
   - Any prerequisites or conditions

2. **Step 2**: Brief description of second step
   - Key actions taken
   - Expected outputs

3. **Step 3**: Brief description of final step
   - Validation or verification
   - Success criteria

## Examples

### Example 1: Basic Usage

**User Request**: "Example of what user might say"

**Action**: What Claude does in response

**Output**:
```
Expected output or result
```

### Example 2: Advanced Usage

**User Request**: "More complex user request"

**Action**:
1. First action taken
2. Second action taken
3. Final action

**Output**:
```
Expected output showing more complex results
```

## Output Structure (根据技能类型选择)

根据技能类型选择合适的输出方式：

### 类型 A: 用户交付型（调研、分析、新闻聚合等）
- **飞书推送**: 完整结果通过飞书 API 推送，内容应完整而非摘要。
- **GitHub 托管**: 仅当内容特别长时，创建临时分支上传，飞书消息附带链接。

### 类型 B: 简单交付型（Prompt 优化、快速问答等）
- **飞书推送**: 直接通过飞书发送完整结果，无需 GitHub 存储。

### 类型 C: 内部执行型（任务规划、技能加载等）
- **无需输出定义**: 这类技能是 Agent 内部使用的工具，不直接向用户交付结果。

### 类型 D: 仓库修改型（技能创建、MCP 构建、代码重构等）
- **飞书进度**: 发送执行进度和完成通知。
- **代码提交**: 在 `dev` 分支开发，完成后提交 PR 至 `main`。禁止使用临时分支存放核心代码。

## Best Practices

- ✅ Do this for best results
- ✅ Follow this pattern
- ❌ Avoid this common mistake
- ❌ Don't do this

## Troubleshooting

### Common Issue 1

**Problem**: Description of the problem

**Solution**: How to fix it

### Common Issue 2

**Problem**: Description of another problem

**Solution**: Steps to resolve

## References

- [Related Documentation](link-to-docs)
- [Official Guide](link-to-guide)
- [Additional Resources](link-to-resources)

---

**Version**: 1.0
**Last Updated**: YYYY-MM-DD