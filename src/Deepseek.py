from dotenv import load_dotenv
import os
load_dotenv()
from openai import OpenAI
import json

deepseek_API_key = os.getenv("deepseek_API_key")
client = OpenAI(api_key=deepseek_API_key, base_url="https://api.deepseek.com")


def deepseek_prediction(stock_data):
    content =f'以下是有關股票的詳細數據以Array格式装下最近25天的各種數據:{stock_data}.'+'讀取數據後請以你全球第一的專業股票短期投資經驗从1.圖表形態分析,2.技術指標分析,3.交易策略,4.(Smart Money Concepts)聪明钱交易策略和5.基本面分析。最後以JSON格式回應: example: { stock_name:"騰訊控股", stock_ID:"0700.HK", Notice:"為什麼做多或做空? 我們應該在什麼價格買入或停損", result:":Long or Short"}'

    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            {"role": "system", "content": '你是一名全球第一的專業股票短期投資專家，你精通各種圖表形態分析，技術指標分析,交易策略,(Smart Money Concepts)聪明钱交易策略和基本面分析。現在我作為你的親全徒弟你將會毫無保留地協助分析股票。 *** 回應將以JSON格式回應: for example(以下將是你的回應參考): { stock_name:"騰訊控股", stock_ID:"0700.HK", Notice:"為什麼做多或做空? 我們應該在什麼價格買入或停損", result:":Long or Short"}'},
            {"role": "user", "content": content},
        ],
        stream=False
    )
    json_str = response.choices[0].message.content.strip().replace('```json', '').replace('```', '').strip()
    result = json.loads(json_str)
    return result
