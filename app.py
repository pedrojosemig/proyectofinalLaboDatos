from flask import Flask, jsonify, request

app = Flask(__name__)

# Ejemplo de una ruta
@app.route('/')
def hello_world():
    return "¡Hola desde la API Flask en Heroku!"

# Aquí puedes agregar otras rutas que tengas en tu Jupyter Notebook
# Por ejemplo:
# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     # Aquí va tu código para hacer predicciones con el modelo
#     return jsonify(result="Aquí va el resultado de tu predicción")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Heroku asigna un puerto dinámico
    app.run(host='0.0.0.0', port=port)