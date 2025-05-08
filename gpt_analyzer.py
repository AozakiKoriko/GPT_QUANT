from openai import OpenAI
from prompt_templates import build_prompt

def load_keys(path="apikey.txt"):
    keys = {}
    with open(path, "r") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                keys[key] = value
    return keys

keys = load_keys()

client = OpenAI(api_key=keys["OPENAI_API_KEY"])

def analyze_market(market_data):
    prompt = build_prompt(market_data)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return {
        "symbol": market_data["symbol"],
        "date": market_data["date"],
        "time": market_data["time"],
        "raw_response": response.choices[0].message.content
    }