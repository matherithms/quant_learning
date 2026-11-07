Project 01 · Stock Risk Analyzer
股票收益与风险分析器 · 本月最终验收项目

输入

一份包含日期、股票代码、收盘价的行情 CSV 文件。优先选取至少 5 只股票、约 2 年以上的历史数据。


处理

数据检查、清洗、价格宽表转换、收益率计算、风险指标计算、相关性分析。


输出

股票指标汇总 CSV、收益与风险图表、数据质量检查结果、研究报告。


质量要求

能重复运行；关键计算有测试；异常数据会被发现；指标口径清楚；不把缺失行情随意填为零。



本项目使用历史行情数据来练习数据工程与统计计算。它不是交易策略，也不以证明某只股票值得买入为目标。


stock-risk-analyzer/
│
├── data/
│   └── prices.csv
│
├── outputs/
│   ├── stock_metrics.csv
│   ├── correlation.csv
│   ├── nav.png
│   └── drawdown.png
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── metrics.py
│   └── plotting.py
│
├── tests/
│   └── test_metrics.py
│
├── main.py
└── README.md
