from flask import Flask, jsonify, request
from queue_service import QueueService

app = Flask(__name__)
queue_service = QueueService()

# Obtener estado de la cola
@app.route('/queue', methods=['GET'])
def get_queue():
    return jsonify(queue_service.get_queue()), 200

# Agregar un elemento a la cola
@app.route('/queue', methods=['POST'])
def add_to_queue():
    data = request.json 
    if not data or 'data' not in data: 
        return jsonify({"error": "Debe enviar un campo 'data' en el cuerpo de la solicitud"}), 400

    # Añadir el dato a la cola y devolver la respuesta al frontend
    result = queue_service.add_to_queue(data['data'])
    return jsonify(result), 201

# Run
if __name__ == '__main__':
    app.run(debug=True, port=5000)
