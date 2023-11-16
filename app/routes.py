from flask import Blueprint, request, jsonify
import joblib

predicciones_bp = Blueprint('predicciones', __name__)

# Cargar el modelo entrenado
modelo_rf = joblib.load('modelo_random_forest.joblib')

#class_mapping = {'High': 0, 'Normal': 1, 'Low': 2}

# Endpoint para realizar predicciones
@predicciones_bp.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener datos del cuerpo de la solicitud
        datos = request.json['datos']
        
        # Realizar predicción con el modelo
        predicciones = modelo_rf.predict([datos])
        
        #numeric_prediction = class_mapping.get(predicciones, -1)

        # Devolver la predicción como JSON
        return jsonify({'prediccion': str(predicciones[0])})
    except Exception as e:
        return jsonify({'error': str(e)})