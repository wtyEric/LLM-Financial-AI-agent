# LLM-Financial-AI-agent

A powerful stock price analysis API powered by Deepseek AI, providing intelligent insights and predictions for stock market data.

## Overview

This project leverages the Deepseek AI model to analyze stock prices and provide detailed insights. The API returns structured data including stock information and analysis results in a clean JSON format.

## Features

- Real-time stock price analysis
- Intelligent market insights
- Structured JSON response format
- Support for multiple stock symbols
- Historical data analysis capabilities

## API Response Format

```json
{
   "stock_name":"騰訊控股",
   "stock_ID":"0700.HK",
   "Notice":"技術面顯示MACD柱狀圖負值收窄但仍在零軸下方，EMA5下穿EMA10形成死叉，短期 趨勢偏空。RSI_9(48.41)接近超賣區，隨機指標%K(20.31)與%D(18.99)超賣，暗示反彈機會。聰明錢關注503.5關鍵支撐（近期低點），若跌破可能加 速下跌。建議在503.5附近輕倉試多，突破516.5阻力加倉，停損設在500.0整數關口下方。基本面市盈率23.17合理但市淨率4.79偏高，短期以技術反彈 為主邏輯。",
   "result":"Long"
}
```

## Prerequisites

- Python 3.10+
- Deepseek API access
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/LLM-Financial-AI-agent.git
cd LLM-Financial-AI-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
cp .env.example .env
# Edit .env with your Deepseek API key and other configurations
```

## Usage

1. Start the API server:
```bash
python app.py
```

2. Make API requests:
```bash
curl -X POST http://localhost:8000/analyze \
     -H "Content-Type: application/json" \
     -d '{"stock_id": "AAPL"}'
```

## Configuration

The API can be configured through environment variables:
- `DEEPSEEK_API_KEY`: Your Deepseek API key
- `PORT`: Server port (default: 8000)



## Disclaimer

This tool is for educational and research purposes only. Always verify the analysis results and make your own investment decisions. The predictions and analysis provided by this API should not be considered as financial advice.
