from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Cargar el modelo entrenado
modelo_rf = joblib.load('modelo_random_forest.joblib')

# Endpoint para realizar predicciones
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener datos del cuerpo de la solicitud
        datos = request.json['datos']
        
        # Realizar predicción con el modelo
        predicciones = modelo_rf.predict([datos])

        # Devolver la predicción como JSON
        return jsonify({'prediccion': int(predicciones[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)
