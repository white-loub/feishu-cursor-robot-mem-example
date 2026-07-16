# 第三方内容声明（Third-Party Notices）

本仓库包含由 Cursor Agent 整理、改编或重新组织的第三方材料。

本文件用于记录目前可以核实的来源、许可证和粗粒度变更情况。它本身不是许可证，也不会改变任何第三方内容原有的许可条款。

本仓库没有提供覆盖全部内容的统一许可证：

- 已识别的第三方内容继续适用其各自的原许可证。
- 对于经确认属于 `white-loub` 的原创内容，未另行授予使用许可，保留所有权利。
- 尚未确认来源的内容，不因此自动被认定为 `white-loub` 的原创作品。

如本文件与上游许可证存在冲突，以对应上游许可证原文为准。

## 已识别的第三方内容

| 本仓库路径 | 可核实来源 | 许可证 | 比对及本地变更概况 |
| --- | --- | --- | --- |
| `skills/meta-skill-creator/` | [YYH211/Claude-meta-skill — create-skill-file](https://github.com/YYH211/Claude-meta-skill/tree/main/create-skill-file) | [MIT](./LICENSES/YYH211-Claude-meta-skill-MIT.txt) | `README.md` 对应上游 `SKILL.md`；主体和示例基本一致，两个模板文件存在本地调整。 |
| `skills/daily-ai-news/` | [YYH211/Claude-meta-skill — daily-ai-news](https://github.com/YYH211/Claude-meta-skill/tree/main/daily-ai-news) | [MIT](./LICENSES/YYH211-Claude-meta-skill-MIT.txt) | 基于上游内容整理，主文件名称、格式及部分内容存在少量本地调整。 |
| `skills/prompt-optimize/` | [YYH211/Claude-meta-skill — prompt-optimize](https://github.com/YYH211/Claude-meta-skill/tree/main/prompt-optimize) | [MIT](./LICENSES/YYH211-Claude-meta-skill-MIT.txt) | 基于上游内容整理，主文件名称、格式及部分内容存在少量本地调整。 |
| `skills/deep-analysis/` | [ginobefun/deep-reading-analyst-skill](https://github.com/ginobefun/deep-reading-analyst-skill/tree/main/src/deep-reading-analyst)，相关整理版本见 [YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill/tree/main/deep-reading-analyst) | [MIT](./LICENSES/ginobefun-deep-reading-analyst-skill-MIT.txt) | 10 个 `references/` 文件与可核实上游一致；主 `README.md` 经过重新组织和本地适配。 |
| `skills/planning-with-files/` | [OthmanAdi/planning-with-files 历史版本](https://github.com/OthmanAdi/planning-with-files/tree/1f54991325a245a73a0be80bce22a32602967e9d/planning-with-files)，相关整理版本见 [YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill/tree/main/planning-with-files) | [MIT](./LICENSES/OthmanAdi-planning-with-files-MIT.txt) | 三个文件内容与该上游版本一致；其中上游 `SKILL.md` 在本仓库中命名为 `README.md`。 |
| `skills/mcp-builder/` | [anthropics/skills — mcp-builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | [Apache-2.0](./skills/mcp-builder/LICENSE.txt) | 目录内容与上游基本一致；上游 `SKILL.md` 在本仓库中命名为 `README.md`。现有 Apache-2.0 许可证文件予以保留。 |

## 当前尚未确认明确上游的内容

目前没有为以下目录确认到足够可靠的直接上游：

- `skills/feishu-bot/`
- `skills/info-gathering/`
- `skills/skill-loader/`

这不表示它们一定完全原创，也不表示它们一定来自第三方；仅表示现有仓库历史不足以作出可靠归属判断。

如果后续找到可信来源，应补充到本文件，并按对应许可证要求保留许可和署名信息。

## 许可证文件

相关许可证原文保存在以下位置：

- [`LICENSES/YYH211-Claude-meta-skill-MIT.txt`](./LICENSES/YYH211-Claude-meta-skill-MIT.txt)
- [`LICENSES/ginobefun-deep-reading-analyst-skill-MIT.txt`](./LICENSES/ginobefun-deep-reading-analyst-skill-MIT.txt)
- [`LICENSES/OthmanAdi-planning-with-files-MIT.txt`](./LICENSES/OthmanAdi-planning-with-files-MIT.txt)
- [`skills/mcp-builder/LICENSE.txt`](./skills/mcp-builder/LICENSE.txt)

许可证文件按当前可核实的上游原文保留，不应删除原有版权声明，也不应将第三方内容改称为 `white-loub` 的原创作品。

## 版本与比对说明

本清单依据当前能够访问的仓库历史、文件内容和逐文件比对整理。

上游仓库可能在本示例创建后发生过更新；由于本仓库没有保存每项内容导入时的完整来源记录，本清单不声称重建了所有文件的精确导入时间和提交链，只记录当前可以合理核实的来源及差异。

YYH211/Claude-meta-skill 的 MIT `LICENSE` 晚于本示例仓库的初始提交，因此此处记录的是目前可以核实的上游许可证，不将其描述为导入当时已经存在的许可记录。

## 纠错与补充

本清单可能存在遗漏。

如果您认为仓库中的内容缺少来源、署名或许可证声明，请提供：

- 涉及的文件或目录路径；
- 可能的原始来源链接；
- 可以帮助核实归属的比较或历史证据。

可以通过 [GitHub Issue](https://github.com/white-loub/feishu-cursor-robot-mem-example/issues/new) 提交说明。仓库虽已停止维护，但保留 Issues 作为讨论和来源纠错渠道；不承诺回复时效、修复或后续更新。

核实后，我们将视情况补充来源与许可证、修正归属说明，或移除相关内容。

# 第三方内容声明（Third-Party Notices）

本仓库包含由 Cursor Agent 整理、改编或重新组织的第三方材料。

本文件用于记录目前可以核实的来源、许可证和粗粒度变更情况。它本身不是许可证，也不会改变任何第三方内容原有的许可条款。

本仓库没有提供覆盖全部内容的统一许可证：

- 已识别的第三方内容继续适用其各自的原许可证。
- 对于经确认属于 `white-loub` 的原创内容，未另行授予使用许可，保留所有权利。
- 尚未确认来源的内容，不因此自动被认定为 `white-loub` 的原创作品。

如本文件与上游许可证存在冲突，以对应上游许可证原文为准。

## 已识别的第三方内容

| 本仓库路径 | 可核实来源 | 许可证 | 比对及本地变更概况 |
| --- | --- | --- | --- |
| `skills/meta-skill-creator/` | [YYH211/Claude-meta-skill — create-skill-file](https://github.com/YYH211/Claude-meta-skill/tree/main/create-skill-file) | [MIT](./LICENSES/YYH211-Claude-meta-skill-MIT.txt) | `README.md` 对应上游 `SKILL.md`；主体和示例基本一致，两个模板文件存在本地调整。 |
| `skills/daily-ai-news/` | [YYH211/Claude-meta-skill — daily-ai-news](https://github.com/YYH211/Claude-meta-skill/tree/main/daily-ai-news) | [MIT](./LICENSES/YYH211-Claude-meta-skill-MIT.txt) | 基于上游内容整理，主文件名称、格式及部分内容存在少量本地调整。 |
| `skills/prompt-optimize/` | [YYH211/Claude-meta-skill — prompt-optimize](https://github.com/YYH211/Claude-meta-skill/tree/main/prompt-optimize) | [MIT](./LICENSES/YYH211-Claude-meta-skill-MIT.txt) | 基于上游内容整理，主文件名称、格式及部分内容存在少量本地调整。 |
| `skills/deep-analysis/` | [ginobefun/deep-reading-analyst-skill](https://github.com/ginobefun/deep-reading-analyst-skill/tree/main/src/deep-reading-analyst)，相关整理版本见 [YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill/tree/main/deep-reading-analyst) | [MIT](./LICENSES/ginobefun-deep-reading-analyst-skill-MIT.txt) | 10 个 `references/` 文件与可核实上游一致；主 `README.md` 经过重新组织和本地适配。 |
| `skills/planning-with-files/` | [OthmanAdi/planning-with-files 历史版本](https://github.com/OthmanAdi/planning-with-files/tree/1f54991325a245a73a0be80bce22a32602967e9d/planning-with-files)，相关整理版本见 [YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill/tree/main/planning-with-files) | [MIT](./LICENSES/OthmanAdi-planning-with-files-MIT.txt) | 三个文件内容与该上游版本一致；其中上游 `SKILL.md` 在本仓库中命名为 `README.md`。 |
| `skills/mcp-builder/` | [anthropics/skills — mcp-builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | [Apache-2.0](./skills/mcp-builder/LICENSE.txt) | 目录内容与上游基本一致；上游 `SKILL.md` 在本仓库中命名为 `README.md`。现有 Apache-2.0 许可证文件予以保留。 |

## 当前尚未确认明确上游的内容

目前没有为以下目录确认到足够可靠的直接上游：

- `skills/feishu-bot/`
- `skills/info-gathering/`
- `skills/skill-loader/`

这不表示它们一定完全原创，也不表示它们一定来自第三方；仅表示现有仓库历史不足以作出可靠归属判断。

如果后续找到可信来源，应补充到本文件，并按对应许可证要求保留许可和署名信息。

## 许可证文件

相关许可证原文保存在以下位置：

- [`LICENSES/YYH211-Claude-meta-skill-MIT.txt`](./LICENSES/YYH211-Claude-meta-skill-MIT.txt)
- [`LICENSES/ginobefun-deep-reading-analyst-skill-MIT.txt`](./LICENSES/ginobefun-deep-reading-analyst-skill-MIT.txt)
- [`LICENSES/OthmanAdi-planning-with-files-MIT.txt`](./LICENSES/OthmanAdi-planning-with-files-MIT.txt)
- [`skills/mcp-builder/LICENSE.txt`](./skills/mcp-builder/LICENSE.txt)

许可证文件按当前可核实的上游原文保留，不应删除原有版权声明，也不应将第三方内容改称为 `white-loub` 的原创作品。

## 版本与比对说明

本清单依据当前能够访问的仓库历史、文件内容和逐文件比对整理。

上游仓库可能在本示例创建后发生过更新；由于本仓库没有保存每项内容导入时的完整来源记录，本清单不声称重建了所有文件的精确导入时间和提交链，只记录当前可以合理核实的来源及差异。

YYH211/Claude-meta-skill 的 MIT `LICENSE` 晚于本示例仓库的初始提交，因此此处记录的是目前可以核实的上游许可证，不将其描述为导入当时已经存在的许可记录。

## 纠错与补充

本清单可能存在遗漏。

如果您认为仓库中的内容缺少来源、署名或许可证声明，请提供：

- 涉及的文件或目录路径；
- 可能的原始来源链接；
- 可以帮助核实归属的比较或历史证据。

在仓库归档前，可以通过 [GitHub Issue](https://github.com/white-loub/feishu-cursor-robot-mem-example/issues/new) 提交说明。仓库归档后，如维护者 GitHub 主页提供了公开联系方式，可以通过该方式联系。

核实后，我们将视情况补充来源与许可证、修正归属说明，或移除相关内容。

