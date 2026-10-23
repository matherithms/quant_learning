'''from pathlib import Path
import os

import pandas as pd
import tushare as ts


# 五只A股
TICKERS = [
    "600519.SH",
    "300750.SZ",
    "600036.SH",
    "601318.SH",
    "000333.SZ",
]

START_DATE = "20240101"
END_DATE = "20261019"

# __file__ 指向 src/download_data.py
# parent.parent 指向 stock-risk-analyzer 项目根目录
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = PROJECT_ROOT / "data" / "prices.csv"


def download_prices():
    # 1. 从环境变量读取 Token
    token = os.getenv("TUSHARE_TOKEN")

    if not token:
        raise ValueError("请先设置 TUSHARE_TOKEN 环境变量")

    # 2. 初始化 Tushare Pro
    pro = ts.pro_api(token)

    all_prices = []

    # 3. 下载各只股票
    for ticker in TICKERS:
        print(f"正在下载：{ticker}")

        df = pro.daily(
            ts_code=ticker,
            start_date=START_DATE,
            end_date=END_DATE,
            fields="ts_code,trade_date,close",
        )

        if df is None or df.empty:
            raise ValueError(f"{ticker} 没有获取到行情数据")

        # 4. 统一列名
        df = df.rename(
            columns={
                "trade_date": "date",
                "ts_code": "asset",
            }
        )

        df = df[["date", "asset", "close"]].copy()

        # 5. 将日期转换为标准格式
        df["date"] = pd.to_datetime(
            df["date"], format="%Y%m%d"
        ).dt.strftime("%Y-%m-%d")

        all_prices.append(df)

    # 6. 合并五只股票的数据
    prices = pd.concat(all_prices, ignore_index=True)

    # 7. 排序
    prices = prices.sort_values(
        ["date", "asset"]
    ).reset_index(drop=True)

    # 8. 保存 CSV
    OUTPUT_PATH.parent.mkdir(
        parents=True, exist_ok=True
    )

    prices.to_csv(
        OUTPUT_PATH,
        index=False,
        encoding="utf-8",
    )

    print(f"\n下载完成：{OUTPUT_PATH}")
    print(prices.groupby("asset").size())
    print(prices.head())


if __name__ == "__main__":
    download_prices()'''

from pathlib import Path
import os
import pandas as pd
import tushare as ts

TICKERS = [
    "600519.SH",
    "300750.SZ",
    "600036.SH",
    "601318.SH",
    "000333.SZ",
]

START_DATE = "20240101"
END_DATE = "20261022"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = PROJECT_ROOT / "data" / "prices.csv"

def download_prices():
    token = os.getenv("TUSHARE_TOKEN")
    if not token:
        raise ValueError("请先设置 TUSHARE_TOKEN 环境变量")
    pro = ts.pro_api(token)

    all_prices = []

    for ticker in TICKERS:
        print(f"正在下载：{ticker}")
        df = pro.daily(ts_code=ticker,start_date=START_DATE,end_date=END_DATE,fields="ts_code,trade_date,close")
        if df is None or df.empty:
            raise ValueError(f"{ticker} 没有获取到行情数据")

        df = df.rename(columns={"trade_date":"date", "ts_code":"asset"})
        df = df[["date", "asset", "close"]].copy()
        df["date"] = pd.to_datetime(df["date"], format="%Y%m%d").dt.strftime("%Y-%m-%d")
        all_prices.append(df)

    prices = pd.concat(all_prices, ignore_index=True)
    prices = prices.sort_values(["date", "asset"]).reset_index(drop=True)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    prices.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
    print(f"\n下载完成：{OUTPUT_PATH}")
    print(prices.groupby("asset").size())
    print(prices.head())

if __name__ == "__main__":
    download_prices()
