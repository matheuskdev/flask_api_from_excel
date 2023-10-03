from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok
import pandas as pd

app = Flask(__name__)
run_with_ngrok(app) 

@app.route('/index', methods=['GET'])
def home():
    try:
        df = pd.read_excel('peoples.xlsx', engine='openpyxl')
        data = df.to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
