from pathlib import Path

from src.load_data import load_prices
from src.metrics import (
    make_price_matrix,
    calculate_returns,
    calculate_metrics
)
from src.plotting import plot_nav, plot_drawdown


def main():
    # __file__：当前 Python 文件的路径
    # resolve()：获取规范化后的绝对路径
    project_root = Path(__file__).resolve().parent

    data_path = project_root / "data" / "prices.csv"
    output_dir = project_root / "outputs"

    # 读取并检查行情数据
    df = load_prices(data_path)

    # 转换为价格宽表
    prices = make_price_matrix(df)

    # 计算收益率
    returns = calculate_returns(prices)

    # 计算收益和风险指标
    metrics = calculate_metrics(returns)

    # mkdir()：创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)

    # to_csv()：将指标汇总表保存为 CSV
    metrics.to_csv(output_dir / "stock_metrics.csv")

    # corr()：计算股票收益率的相关矩阵
    correlation = returns.corr()

    # to_csv()：保存相关矩阵
    correlation.to_csv(output_dir / "correlation.csv")

    # 输出累计净值曲线
    plot_nav(
        returns,
        output_dir / "nav.png"
    )

    # 输出回撤曲线
    plot_drawdown(
        returns,
        output_dir / "drawdown.png"
    )

    print("分析完成。")
    print("有效股票数量：", len(prices.columns))
    print("价格数据行数：", len(prices))
    print("结果保存目录：", output_dir)
    print(metrics)


# 只有直接运行 main.py 时，才调用 main()
if __name__ == "__main__":
    main()
