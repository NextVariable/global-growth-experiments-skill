# 增长实验执行与复盘 · Growth Experiments

把“接下来怎么增长”变成一项值得做的验证：选假设、定方案、协调执行、检查数据，最后决定继续、扩大、修改还是停止。

适合海外产品的渠道验证、内容测试、激活优化、购买与留存实验。既能处理有足够流量的对照试验，也能在只有少量客户时设计有价值的验证。支持单独使用，或承接市场研究、内容、获客和客户增长的结果。

## 安装和第一次使用

将 [完整技能目录](skills/global-growth-experiments/)复制到支持 Agent Skills 的客户端。以 Codex 为例，在终端逐行运行：

```bash
git clone https://github.com/NextVariable/global-growth-experiments-skill.git
cd global-growth-experiments-skill
mkdir -p ~/.agents/skills
cp -R skills/global-growth-experiments ~/.agents/skills/
```

已有同名目录时先核对版本，避免混入旧文件。重新加载客户端，输入：

```text
使用 $global-growth-experiments。我们给小团队做对账工具，每周约有
30 个新注册团队，只有 8 个完成首次核对。团队怀疑首用步骤太多，
也有人建议先加广告。我们只有一名开发者和两周时间。
请先判断值得验证什么，给具体执行方案、需要记录的行为，以及
什么结果会让我们保留、修改或放弃这个方案。不要替我们投放。
```

最少提供产品和当前决定、已有事实/数据、资源限制。没有基线也可开始，Skill 会设计补充测量或小规模验证，不用虚构数字补齐。

## 会交付什么

按任务交出一份可执行的验证方案、真实操作状态或复盘决定。方案写清对象、改动、比较方式、指标、观察窗口、资源上限及停止条件；复盘检查数据质量、实际收益与风险，再给下一动作。没有外部工具或授权时，交出待执行包，不宣称已上线。

方法按需加载：[实验设计](skills/global-growth-experiments/references/experiment-design.md)、[测量与数据](skills/global-growth-experiments/references/measurement.md)、[执行与恢复](skills/global-growth-experiments/references/execution.md)、[复盘与回流](skills/global-growth-experiments/references/learning.md)。一次简短问题无需建立完整实验档案。

可选的转化率计算器使用 Python 3.10+ 标准库，不需要密钥或服务：

```bash
python3 skills/global-growth-experiments/scripts/conversion_summary.py --control 20 100 --variant 30 100
```

它给出比例、百分点差、相对变化及各组 Wilson 区间，不自动判断实验胜负。分析收入、聚类、序贯或复杂归因时需要相应数据与方法。

## 在五个 Skill 中的位置

本 Skill 负责验证与学习：把市场、内容、渠道和客户动作中的未知变成可检验的问题，把结果交回对应部分。它不重新做市场选择、不批量生成营销内容，也不代替日常运营或销售。可通过普通文字和文件交接，其他四个不是安装依赖。

客户和业务数据存放在用户指定的项目目录，安装单元只包含方法、模板及计算工具。关于职责和取舍见 [设计说明](docs/design.md)。

## 验证

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

结构、内部链接与计算检查，以及模型试用的范围和限制分别记录在 [验证说明](validation/README.md)。测试通过不代表真实增长效果；需要真实曝光、成交与成熟留存数据才能判断业务收益。

Growth experiment design, execution coordination and review for international products. Turn a business uncertainty into an actionable test and a defensible next decision. Skill instructions are in Chinese; outputs follow the user's audience and language.

项目及随包代码采用 [MIT License](LICENSE)。
