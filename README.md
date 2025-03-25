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
    "stock_name": "Company Name",
    "stock_id": "TICKER_SYMBOL",
    "result": "xxxxxxx"
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
