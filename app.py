# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load model
model = joblib.load('iris_model.pkl')

# Create API
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = int(model.predict(features)[0])
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)








