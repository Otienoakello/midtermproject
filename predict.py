import pickle
from flask import Flask, jsonify, request

model_file = 'model=.bin'

with open(model_file, 'rb') as f_in:
    dv, dt = pickle.load(f_in)

app = Flask(__name__)  #  creating the Flask app

@app.route('/predict', methods=['POST']) 
def predict():
    client = request.get_json()
    x = dv.transform([client])  
    y_pred = dt.predict_proba(x)[0, 1]  
    exit_flag = y_pred >= 0.7  
    
    result = {
        'exit_probability': float(y_pred),
        'will_exit': bool(exit_flag)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)    