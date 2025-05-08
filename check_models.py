from openai import OpenAI
from gpt_analyzer import load_keys

keys = load_keys()
client = OpenAI(api_key=keys["OPENAI_API_KEY"])

models = client.models.list()

print("你有权限使用的模型包括：")
for model in models.data:
    print(model.id)