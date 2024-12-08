from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

# Cargar el modelo guardado
model = joblib.load(r'C:\Users\DELL\Documents\GitHub\proyectofinalLaboDatos\random_forest_model2.joblib')

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para la predicción, que acepta solicitudes POST
@app.route("/predict", methods = ['POST'])
def predict():
    # Obtener los datos del JSON enviado en la solicitud
    data = request.get_json(force=True)

    # Convertir los datos en un array numpy
    features = np.array(data['features']).reshape(1, -1)

    # Realizar la predicción
    prediction = model.predict(features)

    # Devolver la predicción como JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == "__main__":
    # Iniciar la aplicación Flask en el puerto correcto
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))




