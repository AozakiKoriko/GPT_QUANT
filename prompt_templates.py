def build_prompt(data):
    return f"""
你是一位AI量化分析师。以下是关于某只美股标的的盘前与开盘5分钟数据，请判断走势方向，并给出是否建议入场与挂单区间。

【标的】：{data['symbol']}  
【日期】：{data['date']}  
【时间】：{data['time']} EST  
【前日收盘】：${data['prev_close']}  
【盘前涨幅】：{data['premarket_change']}  
【开盘5分钟K线】：开：${data['open_5min']['open']} 高：${data['open_5min']['high']} 低：${data['open_5min']['low']} 收：${data['open_5min']['close']}  
【成交量】：{data['open_5min']['volume']} 股  
【相关新闻】：
1. {data['news'][0]}
2. {data['news'][1]}

请使用以下格式输出你的分析结论：

方向：看多 / 看空 / 震荡  
入场建议：是 / 否  
挂单区间：$xxx ~ $xxx  
理由：  
1. （结构性依据）  
2. （新闻面依据）
""".strip()