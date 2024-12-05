import os
from flask import Flask, request, jsonify
import joblib
import numpy as np

# aplicación Flask
app = Flask(__name__)

# cargo el modelo guardado
model = joblib.load('random_forest_model.joblib')

# endpoint para realizar predicciones
@app.route('/predict', methods=['POST'])
def predict():
    # obtengo los datos de la solicitud
    data = request.get_json()  # JSON con los datos de entrada
    features = np.array(data['features']).reshape(1, -1)
    
    # prediccion
    prediction = model.predict(features)
    
    # prediccin como respuesta
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
