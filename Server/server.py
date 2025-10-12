from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import util
import os

app = Flask(__name__, static_folder='../Client', template_folder='../Client')
CORS(app)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.form
    total_sqft = float(data['total_sqft'])
    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("🏠 Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()

    # Use the PORT Render provides or default to 5000 for local
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
