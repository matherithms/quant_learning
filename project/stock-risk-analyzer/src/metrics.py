import numpy as np
import pandas as pd


TRADING_DAYS = 252


def make_price_matrix(df):
    """
    将长表行情转换为宽表价格矩阵。

    行：日期
    列：股票代码
    值：收盘价
    """

    # pivot()：按日期和股票代码重塑数据
    prices = df.pivot(
        index="date",
        columns="asset",
        values="close"
    )

    # sort_index()：保证日期按升序排列
    prices = prices.sort_index()

    return prices


def calculate_returns(prices):
    """
    根据价格矩阵计算简单收益率。
    """

    # pct_change()：计算相邻观测值之间的简单收益率
    returns = prices.pct_change(fill_method=None)

    return returns


def calculate_metrics(returns):
    """
    对每只股票计算收益与风险指标。

    本函数中的年化收益率采用算术年化近似。
    年化波动率使用样本标准差和 252 交易日假设。
    """

    results = []

    for asset in returns.columns:
        # dropna()：去掉该股票缺失的收益率观测
        r = returns[asset].dropna()

        # 避免有效样本太少时输出缺乏意义的指标
        if len(r) < 2:
            continue

        # mean()：计算日均收益率
        mean_daily = r.mean()

        # std()：计算样本标准差
        vol_daily = r.std()

        # cumprod()：将收益率转换为累计净值
        nav = (1 + r).cumprod()

        # cummax()：计算历史最高净值
        peak = nav.cummax()

        # 计算回撤序列
        drawdown = nav / peak - 1

        # 年化波动率
        annualized_vol = vol_daily * np.sqrt(TRADING_DAYS)

        # 算术年化收益率近似
        annualized_return = mean_daily * TRADING_DAYS

        # 最大回撤
        max_drawdown = -drawdown.min()

        # 简化的年化夏普比率，暂不扣除无风险利率
        if vol_daily > 0:
            sharpe = (
                mean_daily / vol_daily
            ) * np.sqrt(TRADING_DAYS)
        else:
            sharpe = np.nan

        results.append({
            "asset": asset,
            "observations": len(r),
            "mean_daily_return": mean_daily,
            "annualized_return_approx": annualized_return,
            "annualized_volatility": annualized_vol,
            "max_drawdown": max_drawdown,
            "sharpe_no_rf": sharpe
        })

    # pd.DataFrame()：将结果字典列表转换为汇总表
    metrics = pd.DataFrame(results)

    # set_index()：把股票代码设为汇总表的索引
    if not metrics.empty:
        metrics = metrics.set_index("asset")

    return metrics