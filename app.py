from flask import Flask, request, jsonify
from threading import Thread
import joblib
import numpy as np
import sklearn

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
    # Aquí 'features' debe ser una lista con todas las características de entrada
    features = np.array(data['features']).reshape(1, -1)

    # Realizar la predicción
    prediction = model.predict(features)

    # Devolver la predicción como JSON
    return jsonify({'prediction': prediction.tolist()})

# Función para ejecutar la app de Flask
def run_app():
    app.run(host='0.0.0.0', port=5000)

# Ejecutar la aplicación Flask en un hilo
thread = Thread(target=run_app)
thread.start()



