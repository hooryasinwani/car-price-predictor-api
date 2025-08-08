import pandas as pd
import pickle as pk
from flask import Flask, request, jsonify

app = Flask(__name__)

model = pk.load(open('model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    print("[DEBUG] --- Request received ---", flush=True)
    json_data = request.get_json()
    print(f"[DEBUG] --- JSON data parsed: {json_data} ---", flush=True)

    df = pd.DataFrame(json_data, index=[0])
    print("[DEBUG] --- DataFrame created ---", flush=True)

    df['Fuel_Type'].replace(['Diesel' ,'Hybrid' ,'Electric', 'Petrol'], [1, 2, 3, 4], inplace=True)
    df['Model'].replace(['Rio', 'Malibu', 'GLA', 'Q5', 'Golf' ,'Camry', 'Civic' ,'Sportage' ,'RAV4',
    '5 Series', 'CR-V', 'Elantra', 'Tiguan', 'Equinox', 'Explorer' ,'A3' ,'3 Series',
    'Tucson', 'Passat' ,'Impala', 'Corolla' ,'Optima' ,'Fiesta', 'A4' ,'Focus',
    'E-Class' ,'Sonata', 'C-Class' ,'X5', 'Accord'], [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], inplace=True)
    df['Transmission'].replace(['Manual', 'Automatic', 'Semi-Automatic'], [1, 2, 3], inplace=True)
    df['Brand'].replace(
    ['Kia', 'Chevrolet', 'Mercedes', 'Audi', 'Volkswagen', 'Toyota', 'Honda', 'BMW', 'Hyundai', 'Ford'],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], inplace=True)
    print("[DEBUG] --- Preprocessing complete ---", flush=True)

    print("[DEBUG] --- Calling model.predict() ---", flush=True)
    prediction = model.predict(df)
    print("[DEBUG] --- Prediction successful ---", flush=True)

    return jsonify({'predicted_price': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)