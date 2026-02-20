from flask import Flask, render_template, request
import pickle
import numpy as np

import os

app = Flask(__name__)

# Load the model and scaler
model = None
scaler = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'floods.save')
SCALER_PATH = os.path.join(BASE_DIR, 'transform.save')

try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")

try:
    with open(SCALER_PATH, 'rb') as f:
        scaler = pickle.load(f)
    print("Scaler loaded successfully.")
except Exception as e:
    print(f"Error loading scaler: {e}")


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_ui')
def predict_ui():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return render_template('index.html', prediction_text="Error: Model or Scaler not loaded.")

    try:
        # Get data from form
        # Features: Temp, Humidity, Cloud Cover, ANNUAL, Jan-Feb, Mar-May, Jun-Sep, Oct-Dec, avgjune, sub
        
        features = [
            float(request.form['Temp']),
            float(request.form['Humidity']),
            float(request.form['Cloud_Cover']),
            float(request.form['ANNUAL']),
            float(request.form['Jan_Feb']),
            float(request.form['Mar_May']),
            float(request.form['Jun_Sep']),
            float(request.form['Oct_Dec']),
            float(request.form['avgjune']),
            float(request.form['sub'])
        ]
        
        # Scale the features
        final_features = scaler.transform([np.array(features)])
        
        # Predict
        prediction = model.predict(final_features)
        output = prediction[0]
        
        if output == 1:
            return render_template('chance.html')
        else:
            return render_template('no chance.html')

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error in prediction: {e}")

if __name__ == "__main__":
    app.run(debug=True)
