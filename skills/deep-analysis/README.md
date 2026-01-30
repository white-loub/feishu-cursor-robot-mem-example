---
name: deep-analysis
description: "Master-level skill for deep analysis and research. Combines systematic reading frameworks (SCQA, 5W2H, Six Hats, etc.) with advanced research methodologies (Graph of Thoughts, Multi-agent execution, Citation validation). Use for deep-diving into articles, academic papers, technical topics, or complex problem-solving. Activates for tasks like 'analyze this paper', 'deep research on X', 'extract insights from Y', or 'systematic evaluation of Z'."
---

# 🧠 Deep Analysis & Research (深度分析与研究)

> 从碎片化信息到系统化洞见：融合思维模型与多维研究的顶尖专家框架

本技能将**深度阅读分析**（10+ 思维模型）与**学术/技术深度调研**（7阶段 GoT 流程）完美结合，旨在为复杂任务提供具备深度、广度和可验证性的分析结果。

## 🎯 何时使用 (When to Use)

- **学术/技术研判**: 需要对论文、技术文档或前沿领域进行全方位拆解时。
- **深度内容消化**: 阅读长难文章、研报，需要提取核心洞见并形成行动方案。
- **复杂问题分析**: 需要运用多种思维模型（第一性原理、逆向思维等）进行决策或方案评估。
- **多源信息核实**: 需要跨平台验证信息真伪，提供引文支撑。

---

## 🛠️ 核心方法论 (Methodology)

### 1. 深度调研流 (7-Phase Research Workflow)
针对高复杂度课题，采用分阶段研究流：

1. **需求对齐 (Refinement)**: 明确目标、范围及产出格式。
2. **研究规划 (Planning)**: 初始化 **GoT (Graph of Thoughts)**，拆解子任务。
3. **多源采集 (Gathering)**: 检索 arXiv, Hugging Face, GitHub, 及全球网页。
4. **并行执行 (Execution)**: 多 Agent 协作，分别负责架构、指标、社区反馈等。
5. **交叉验证 (CoV)**: 通过 Chain-of-Verification 消除信息冲突。
6. **引文分级 (Validation)**: 确保每一项核心主张都有 A 级（同行评审）或 B 级（官方）信源支撑。
7. **综合报告 (Synthesis)**: 产出结构化深度报告。

### 2. 思维模型武器库 (Mental Model Arsenal)
在分析过程中，灵活调用以下模型：

- **基础分析 (Level 1-2)**:
  - 📋 **SCQA**: 背景 (S)、冲突 (C)、问题 (Q)、答案 (A)。
  - 🔍 **5W2H**: 全面性检查。
  - 🎯 **批判性思维**: 评估论据质量与逻辑漏洞。
  - 🔄 **逆向思维**: 识别风险与失败模式。

- **深度洞察 (Level 3-4)**:
  - 🧠 **思维模型集**: 跨学科应用物理、生物、心理、经济模型。
  - ⚡ **第一性原理**: 剥离表象，回归本质真相。
  - 🔗 **系统思考**: 映射复杂变量间的反馈回路。
  - 🎨 **六顶思考帽**: 结构化多角度评估（事实、情感、风险、收益、创意、流程）。

---

## 📋 执行路径 (Execution Path)

### 第一步：初始化分析 (Initialize)
根据任务深度选择路径：
- **快速 (15min)**: SCQA + 5W2H。
- **标准 (30min)**: + 批判性思维 + 逆向思维。
- **深度 (60min)**: + 思维模型集 + 第一性原理 + 系统思考。
- **研究 (120min+)**: 启动 7 阶段深度调研流 + 网页检索。

### 第二步：结构化产出 (Output)

所有分析结果通过飞书 API 完整推送：

1.  **🚀 飞书实时同步 (Primary)**:
    -   所有进度和报告优先通过飞书 API 推送。
    -   内容必须完整且结构化（推荐使用飞书卡片格式）。
    -   飞书消息应包含完整分析内容，而非简化摘要。

2.  **📂 GitHub 长文档托管 (仅超长内容)**:
    -   只有当报告**特别长**（如完整论文拆解、多篇文献综述等）时，才创建临时分支上传。
    -   分支命名：`temp/analysis-[topic]`
    -   保存目录：`RESEARCH/[topic_name]/`
    -   飞书消息中包含完整关键点 + GitHub 文档链接。

---

## 💡 专家意见 (Expert Advice)

1. **不要为了框架而框架**: 框架是工具，不是目的。如果 SCQA 已经足够清晰，就不必强行应用六顶思考帽。
2. **关注"缺失"的信息**: 5W2H 最大的价值在于发现原文中"没说"的部分。
3. **分级信源**: 在学术研究中，GitHub Stars 反映人气，arXiv 论文反映前沿，两者结合才是完整的技术图景。

## 📂 参考资源 (References)
- [思维模型详解](./references/)
- [引文分级标准](./references/evaluation.md) (待补充)
- [输出模板](./references/output_templates.md)

---

**Version**: 2.1
**Last Updated**: 2026-01-21
