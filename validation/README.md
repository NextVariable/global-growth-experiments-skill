# 验证记录

2026-10-23 UTC，一个不继承开发历史的新模型上下文实际执行了三个合成业务任务，按需加载运行资料并使用计算工具。三个任务在同一上下文顺序完成，未提供评审答案；这不是三个独立样本或竞品对照。

| 任务 | 实际观察 | 本轮判断 |
|---|---|---|
| [低流量选择](forward-tests/low-traffic.input.md) | [原稿](forward-tests/low-traffic.output.md)选择修复导入障碍，识别付费队列不成熟，不承诺两周测出 15% 付费提升 | 提供能在资源内推进的任务验证，同时保留付费结论 |
| [渠道重叠](forward-tests/attribution.input.md) | [原稿](forward-tests/attribution.output.md)正确去重为 280 注册、33 付费；保留价格与版本混杂，不把 UTM 触点当因果贡献 | 不支持无依据三倍加预算，给出有限试投和补测安排 |
| [护栏与成熟窗口](forward-tests/guardrail.input.md) | [原稿](forward-tests/guardrail.output.md)区分 +8 个百分点与相对 +20%；识别重复扣款已触发停止、14 天不可能有成熟 D30 | 拒绝全量，给出有权限负责人应执行的止损，未假称自己停用 |

逐份判断由维护者完成，不是独立盲评。输入、原始输出、运行方式和方法哈希见 [manifest.json](forward-tests/manifest.json)。未测量成本、自动触发准确率、模型间稳定性或真实增长收益。

转化率脚本另有 7 项自动检查：Wilson 固定例、百分点与相对变化、零基线、全成功、非法计数、命令行拒绝、有限 JSON 输出。安装单元通过结构、内部链接、客户端元数据和 skill-creator `quick_validate.py` 检查。

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

自动检查只验证格式、记录完整性和算数，不会给业务答案评分。计算器不产生因果结论或“赢者”；现实的分流、事件采集、支付、广告配置、成熟留存和收益仍需真实实施验证。记录里的样例客户、费用和计数均为合成资料。
