def print_analysis_result(analysis):
    print(f"\n🧠 GPT分析结果 [{analysis['symbol']} - {analysis['date']} {analysis['time']} EST]")
    print("-" * 50)
    print(analysis["raw_response"])
    print("-" * 50)