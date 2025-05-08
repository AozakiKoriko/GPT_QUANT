from data_fetcher import get_real_market_data
from gpt_analyzer import analyze_market
from output import print_analysis_result
from datetime import datetime
import pytz

def main():
    print("📈 GPT+量化交易助手 (历史分析模式)")

    symbol = input("请输入标的代码（如 QQQ）：").strip().upper()
    date_str = input("请输入分析日期（格式 YYYY-MM-DD，如 2024-05-01）：").strip()

    try:
        est_datetime = datetime.strptime(date_str, "%Y-%m-%d")
        est_datetime = pytz.timezone("US/Eastern").localize(est_datetime)
    except Exception as e:
        print(f"❌ 日期格式错误，请使用 YYYY-MM-DD（例如 2024-05-01）。")
        return

    print(f"\n⏳ 正在准备数据：{symbol} @ {date_str}（历史模式）")
    market_data = get_real_market_data(symbol, est_datetime)

    if not market_data:
        print("🚫 获取数据失败，终止分析。")
        return

    analysis = analyze_market(market_data)
    print_analysis_result(analysis)

if __name__ == "__main__":
    main()