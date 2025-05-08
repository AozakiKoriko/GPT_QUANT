def build_prompt(data):
    return f"""
你是一位AI量化分析师。以下是关于某ETF的盘前与开盘5分钟数据，请判断方向及入场建议。

【标的】：{data['symbol']}  
【日期】：{data['date']}  
【时间】：{data['time']} EST  
【前日收盘】：${data['prev_close']}  
【盘前涨幅】：{data['premarket_change']}  
【开盘5分钟K线】：开：${data['open_5min']['open']} 高：${data['open_5min']['high']} 低：${data['open_5min']['low']} 收：${data['open_5min']['close']}  
【成交量】：{data['open_5min']['volume']}股  
【相关新闻】：
1. {data['news'][0]}
2. {data['news'][1]}

请输出：
- 今日方向偏好（看多 / 看空 / 震荡）
- 是否建议入场（是 / 否）
- 推荐挂单区间（如 $355.30 ~ $355.50）
- 简要理由（结构 + 新闻）
""".strip()