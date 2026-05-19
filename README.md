# Code Archaeologist - AI屎山代码考古学家

> 让AI帮你读懂遗留代码，自动生成文档，安全重构。

## 解决的痛点
接手无文档的遗留项目时，调用链混乱，改一行崩全身。传统IDE只能静态跳转，无法理解业务逻辑。

## 核心架构
[代码仓库] → [全量索引/调用图谱] → [多Agent分析]
                                    ├── Archaeologist: 追踪调用链
                                    ├── Documentarian: 生成文档
                                    └── Refactor: 提出重构方案

## 技术栈
- Python 3.11+
- LangChain / AutoGen（多Agent协作）
- ChromaDB（代码向量索引）
- Tree-sitter（AST解析）
- MiMo API（长链推理）

## 开发计划
- [x] 项目初始化
- [ ] AST解析模块：提取函数定义和调用关系
- [ ] 向量索引模块：将代码片段存入ChromaDB
- [ ] Archaeologist Agent：追踪跨文件调用链
- [ ] Documentarian Agent：自动生成注释
- [ ] Refactor Agent：重构建议与风险评估
- [ ] 接入MiMo API，验证长链推理效果

## 为什么需要大量Token
中型项目（10万+行）单次索引需将全量代码作为上下文，多Agent多轮推理和文档生成，单次消耗数百万Token。计划批量分析开源项目来测试极限场景。