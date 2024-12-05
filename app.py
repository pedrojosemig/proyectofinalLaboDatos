import os  # Importar os para acceder a variables de entorno
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
    
    # predicción
    prediction = model.predict(features)
    
    # predicción como respuesta
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Heroku asigna un puerto dinámico
    app.run(host='0.0.0.0', port=port, debug=True)  # Asegúrate de pasar el puerto a app.run()
