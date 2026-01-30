---
name: skill-loader
description: Repository-wide skill discovery and loader. Before starting a new task, use this to scan the repository for available skills. Loads skill IDs and descriptions into the context, providing a "map" of available capabilities.
---

# 📥 Skill Loader

> 一键扫描全库技能，为 AI 提供能力地图

Skill Loader 是本仓库的核心基石技能。它具有两个核心功能：
1. **全局概览**：扫描整个 `skills/` 目录，将所有可用技能的 ID 和简介加载到上下文中，让 AI 知道自己拥有哪些“超能力”。
2. **精准加载**：根据需要，将特定技能的完整文档加载到上下文中，以执行复杂的工作流。

## When to Use This Skill

- **新任务开始前**：运行不带参数的脚本，获取技能全景图。
- **需要特定能力时**：通过 ID 加载具体技能（如：开始调研前加载 `paper-analysis`）。
- **遵循 [README.md](../../README.md) 中的“先加载，后工作”原则。**

## Usage

### 1. 全局概览 (推荐在每个新任务开始前执行)
```bash
python skills/skill-loader/scripts/load_skill.py
```

### 2. 加载具体技能
```bash
python skills/skill-loader/scripts/load_skill.py <skill_id>
```

## How It Works

1. **扫描全库**：脚本遍历 `skills/` 目录，解析每个技能的 `README.md`。
2. **提取元数据**：提取 YAML frontmatter 中的 `name` 和 `description`。
3. **注入能力地图**：在对话流中生成一张技能对比表。
4. **按需深读**：提示 AI 如果需要更详细的操作指引，请进一步读取具体文件。

## Best Practices

- ✅ **先扫描，后深入**：先执行全局加载了解可用工具，再根据需要加载具体文档。
- ✅ **保持 Frontmatter 更新**：每个技能的 `README.md` 必须包含准确的 `name` 和 `description`。
- ❌ **避免过载**：不要一次性读取所有技能的全文，这会消耗过多的 Token。

---

**Version**: 1.1
**Last Updated**: 2026-01-21
