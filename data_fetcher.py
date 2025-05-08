import requests
from datetime import datetime, timedelta
from gpt_analyzer import load_keys
import pytz

def get_real_market_data(symbol: str, est_datetime: datetime):
    keys = load_keys()
    api_key = keys["POLYGON_API_KEY"]
    eastern = pytz.timezone("US/Eastern")

    try:
        # 获取前一日收盘价
        prev_url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/prev?adjusted=true&apiKey={api_key}"
        try:
            prev_data = requests.get(prev_url).json()
            prev_close = round(prev_data["results"][0]["c"], 2)
        except Exception as e:
            print(f"⚠️ 无法获取 {symbol} 的前一日收盘价：{e}")
            prev_close = 0.0  # 保底值

        # 计算9:30和9:35 EST对应的UTC时间戳（毫秒）
        date_str = est_datetime.strftime("%Y-%m-%d")
        dt_start_est = eastern.localize(datetime.strptime(f"{date_str} 09:30:00", "%Y-%m-%d %H:%M:%S"))
        dt_end_est = eastern.localize(datetime.strptime(f"{date_str} 09:35:00", "%Y-%m-%d %H:%M:%S"))
        dt_start_utc = dt_start_est.astimezone(pytz.utc)
        dt_end_utc = dt_end_est.astimezone(pytz.utc)
        ts_start = int(dt_start_utc.timestamp() * 1000)
        ts_end = int(dt_end_utc.timestamp() * 1000)

        url = (
            f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/minute/"
            f"{date_str}/{date_str}?adjusted=true&sort=asc&limit=300&apiKey={api_key}"
        )

        res = requests.get(url).json()
        results = res.get("results", [])
        if not results:
            print("⚠️ 无法获取该日期的分钟数据")
            return None

        # 按时间升序排序
        results.sort(key=lambda r: r["t"])

        # 筛选出 9:30–9:34 分钟数据（ts_start ≤ t < ts_end）
        filtered = [r for r in results if ts_start <= r["t"] < ts_end]

        # 若不足5条，fallback取最后连续5条数据
        if len(filtered) < 5:
            if len(results) < 5:
                print(f"⚠️ 该日期分钟数据不足5条（实际仅 {len(results)} 条）")
                return None
            filtered = results[-5:]

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
                "no",
                "no"
            ]
        }

    except Exception as e:
        print(f"❌ 获取 {symbol} 数据失败：{e}")
        return None