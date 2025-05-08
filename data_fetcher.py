import requests
from datetime import datetime, timedelta
from gpt_analyzer import load_keys
import pytz

def get_real_market_data(symbol: str, est_datetime: datetime):
    keys = load_keys()
    api_key = keys["POLYGON_API_KEY"]
    eastern = pytz.timezone("US/Eastern")

    try:
        # 获取前一日收盘价（注意：prev 只能拿最新一日，这里用不了，只能省略或模拟）
        prev_close = 0.0  # ⚠️ 暂时无法准确获取前一日，仅用于测试。你可指定默认或写死

        # 获取指定日期的 9:30–9:35 的分钟K线
        date_str = est_datetime.strftime("%Y-%m-%d")
        url = (
            f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/minute/"
            f"{date_str}/{date_str}?adjusted=true&sort=asc&limit=300&apiKey={api_key}"
        )

        res = requests.get(url).json()
        results = res.get("results", [])
        if not results:
            print("⚠️ 无法获取该日期的分钟数据")
            return None

        # 筛选出 9:30–9:34 分钟数据
        start = est_datetime.replace(hour=9, minute=30, second=0)
        end = start + timedelta(minutes=5)

        filtered = []
        for r in results:
            ts = datetime.fromtimestamp(r["t"] / 1000, tz=eastern)
            if start <= ts < end:
                filtered.append(r)

        if len(filtered) < 5:
            print(f"⚠️ 该日期分钟数据不足5条（实际仅 {len(filtered)} 条）")
            return None

        open_price = round(filtered[0]["o"], 2)
        high_price = round(max(r["h"] for r in filtered), 2)
        low_price = round(min(r["l"] for r in filtered), 2)
        close_price = round(filtered[-1]["c"], 2)
        volume = int(sum(r["v"] for r in filtered))

        return {
            "symbol": symbol.upper(),
            "date": date_str,
            "time": "09:30–09:35",
            "prev_close": prev_close,  # 暂用模拟值
            "premarket_change": "N/A",
            "open_5min": {
                "open": open_price,
                "high": high_price,
                "low": low_price,
                "close": close_price,
                "volume": volume
            },
            "news": [
                "CNBC：FOMC维持利率不变，鲍威尔称通胀仍未达目标。",
                "Yahoo Finance：NVDA盘前上涨3%，GPU订单强劲。"
            ]
        }

    except Exception as e:
        print(f"❌ 获取 {symbol} 数据失败：{e}")
        return None