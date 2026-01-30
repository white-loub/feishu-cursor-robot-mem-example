---
name: info-gathering
description: "Aggregates information from multiple sources including search engines, social media (X/Twitter), developer platforms (GitHub), and academic databases. Focuses on data cleaning, deduplication, and signal-to-noise ratio optimization."
---

# Multi-Source Information Gathering Skill

> High-efficiency information aggregation and noise reduction framework for comprehensive research.

## When to Use This Skill

Activate this skill when the user:
- Asks to "collect information about [topic]"
- Needs a "comprehensive overview" of a new technology or trend
- Wants to "monitor" a specific field across different platforms
- Requests to "find all relevant links/resources" for a project

## Workflow: The 4C Model

### 1. Collection (多源采集)
- **Web Search**: Google/Bing via `WebSearch` tool for general context.
- **Social Media**: Search X/Twitter for real-time sentiment and developer buzz.
- **Code/Dev**: GitHub API/Search for implementations, libraries, and stars.
- **Academic**: arXiv/Hugging Face for theoretical foundations.
- **Direct Fetch**: `webReader` for deep content extraction from key URLs.

### 2. Cleaning (信息清洗)
- **Deduplication**: Remove identical stories from different sources.
- **Noise Filtering**: Strip marketing fluff, ads, and irrelevant side-topics.
- **Entity Extraction**: Identify key companies, people, and technologies mentioned.

### 3. Categorization (多维分类)
- Group information by **source type**, **relevance**, or **chronology**.
- Tag items as "Must Read", "Technical Implementations", or "Industry News".

### 4. Condensing (智能浓缩)
- Provide a "Bottom Line Up Front" (BLUF) summary.
- Map out the relationships between different pieces of information.

## Best Practices

- **Signal-to-Noise**: Prioritize quality over quantity. Limit results to top 15-20 high-signal items.
- **Cross-Verification**: If a claim appears in multiple independent sources, increase its "Trust Score".
- **Source Transparency**: Always include the original source link and date.
- **Latent Linkage**: Look for hidden connections (e.g., a paper and its unofficial GitHub implementation).

## 📊 输出标准 (Output Structure)

收集到的信息通过飞书 API 完整推送：

1. **🚀 飞书推送 (Primary)**:
    - 发送整理后的信息简报（卡片格式）。
    - 包含核心发现、Top 资源列表及直接访问链接。
    - 飞书消息应包含完整内容，而非简化摘要。

2. **📂 GitHub 长文档托管 (仅超长内容)**:
    - 只有当资源清单**特别长**（如 50+ 条目的完整数据集）时，才创建临时分支上传。
    - 路径：`GATHERED/[topic]/resources.md`
    - 飞书消息中包含完整关键发现 + GitHub 文档链接。

## Example Commands

- `Find all recent discussions and implementations of 'Mamba-2' architecture.`
- `Gather information on the 'Humans&' $480M funding round, including investor sentiment and competitor reactions.`
- `Comprehensive search for 'AutoGLM' performance benchmarks across GitHub and academic papers.`
