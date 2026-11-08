from pathlib import Path
import matplotlib.pyplot as plt


def plot_nav(returns, output_path):
    """
    绘制累计净值曲线，并保存为图片。
    """

    # cumprod()：根据收益率计算累计净值
    nav = (1 + returns).cumprod()

    # mkdir()：创建输出目录
    # parents=True 允许同时创建上级目录
    # exist_ok=True 表示目录已经存在时不报错
    output_path = Path(output_path)
    output_path.parent.mkdir(
        parents=True, exist_ok=True
    )

    # plot()：绘制每只股票的累计净值
    ax = nav.plot(
        figsize=(12, 6),
        title="Cumulative NAV"
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("NAV")

    # legend()：显示图例
    ax.legend()

    # tight_layout()：调整图表布局
    plt.tight_layout()

    # savefig()：将图表保存为图片文件
    plt.savefig(output_path, dpi=150)

    # close()：关闭图表，避免重复运行时累积大量图形对象
    plt.close()


def plot_drawdown(returns, output_path):
    """
    绘制并保存各股票的回撤曲线。
    """

    # cumprod()：计算累计净值
    nav = (1 + returns).cumprod()

    # cummax()：计算历史峰值
    peak = nav.cummax()

    # 计算回撤
    drawdown = nav / peak - 1

    output_path = Path(output_path)
    output_path.parent.mkdir(
        parents=True, exist_ok=True
    )

    # plot()：绘制回撤曲线
    ax = drawdown.plot(
        figsize=(12, 5),
        title="Drawdown"
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Drawdown")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()