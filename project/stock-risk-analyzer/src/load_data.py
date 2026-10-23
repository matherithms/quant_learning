
'''from pathlib import Path

import numpy as np
import pandas as pd


def load_prices(path):
    """
    读取并检查股票行情。

    参数
    ----
    path : str 或 Path
        CSV 文件路径。

    返回
    ----
    pd.DataFrame
        包含 date、asset、close 三列的行情数据。
    """

    # 1. 检查文件是否存在
    path = Path(path)

    if not path.is_file():
        raise FileNotFoundError(f"找不到数据文件：{path}")

    # 2. 读取 CSV
    df = pd.read_csv(path)

    required_columns = {"date", "asset", "close"}

    if not required_columns.issubset(df.columns):
        raise ValueError(
            f"数据必须包含以下列：{required_columns}"
        )

    # 3. 先检查原始缺失值
    if df[["date", "asset", "close"]].isna().any().any():
        raise ValueError("行情数据中存在缺失值")

    # 4. 转换数据类型
    df["date"] = pd.to_datetime(
        df["date"], errors="raise"
    )

    df["asset"] = df["asset"].astype(str).str.strip()


    df["close"] = pd.to_numeric(
        df["close"], errors="raise"
    )

    # 5. 检查空股票代码
    if df["asset"].eq("").any():
        raise ValueError("发现空股票代码")

    # 6. 检查价格是否为有限正数
    if not np.isfinite(df["close"]).all():
        raise ValueError("发现非有限价格")

    if (df["close"] <= 0).any():
        raise ValueError("发现非正价格")

    # 7. 检查重复记录
    duplicate_mask = df.duplicated(
        subset=["date", "asset"],
        keep=False
    )

    if duplicate_mask.any():
        raise ValueError(
            "发现重复的日期—股票记录"
        )

    # 8. 按股票代码和日期排序
    df = df.sort_values(["asset", "date"])

    # 9. 重建行索引
    df = df.reset_index(drop=True)

    return df'''

import pandas as pd
import numpy as np
from pathlib import Path

def load_prices(path):
    
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"找不到数据文件：{path}")
    df = pd.read_csv(path)

    required_columns = {"date", "asset", "close"}
    if not requierd_columns.issubset(df.columns):
        raise ValueError(f"数据必须包含以下列：{required_columns}")

    if df[["date", "asset", "close"]].isna().any().any():
        raise ValueError("行情数据中存在缺失值")

    df["date"] = pd.to_datetime(df["date"], errors="raise")
    df["asset"] = df["asset"].astype(str).str.strip()
    df["close"] = pd.to_numeric(df["close"], errors="raise" )

    

