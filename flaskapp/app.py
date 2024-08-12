from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Gemini AI API details
GEMINI_API_KEY = 'AIzaSyB9-9vqc7axPxc0YefWB_jFoNHuI8FQrgM'
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

@app.route('/query', methods=['POST'])
def query_gemini():
    data = request.json
    query = data.get("query")
    
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    payload = {
        "contents": [{"parts": [{"text": query}]}]
    }
    
    # Make the request to Gemini API
    response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", json=payload)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
