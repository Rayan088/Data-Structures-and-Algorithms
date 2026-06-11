from flask import Flask, request, jsonify
from flask_cors import CORS

from pipeline import run_pipeline

app = Flask(__name__) # Create flask app
CORS(app) # Enables cross-origin requests from frontend and backend

@app.route('/compare', methods=['POST', 'OPTIONS'])
def compare():

    # Gets uploaded docs
    file1 = request.files['file1']
    file2 = request.files['file2']

    # Converts bytes to string
    text1 = file1.read().decode('utf-8', errors='ignore')
    text2 = file2.read().decode('utf-8', errors='ignore')

    result = run_pipeline(text1, text2)

    # Converts python dict to JSON object
    return jsonify(result) 

if __name__ == "__main__":
    app.run(debug=True) #  Execute app and auto reload on changes