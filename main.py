from flask import Flask, jsonify, request
from flask_cors import CORS
from src.data_collection import get_stock_data
from src.Deepseek import deepseek_prediction

app = Flask(__name__)
CORS(app)  

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Get parameters from query string
        stock_name = request.args.get('stock_name')
        ticker_symbol = request.args.get('ticker_symbol')
        
        # Validate parameters
        if not stock_name or not ticker_symbol:
            return jsonify({'error': 'Both stock_name and ticker_symbol are required'}), 400
        
        # Get stock data
        stock_data = get_stock_data(stock_name=stock_name, ticker_symbol=ticker_symbol)
        
        # Make prediction
        prediction = deepseek_prediction(stock_data)
        
        return prediction
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/')
def home():
    return 'Hello World'

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)