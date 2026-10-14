from flask import Flask, jsonify

app = Flask(__name__)

# Inventario inicial con al menos 5 equipos
inventario = [
    {"id": 1, "nombre": "Switch Core", "tipo": "switch", "marca": "Cisco", "cantidad": 3, "estado": "disponible"},
    {"id": 2, "nombre": "Router Borde", "tipo": "router", "marca": "Huawei", "cantidad": 1, "estado": "en uso"},
    {"id": 3, "nombre": "AP Oficina", "tipo": "access point", "marca": "TP-Link", "cantidad": 5, "estado": "disponible"},
    {"id": 4, "nombre": "Switch Acceso", "tipo": "switch", "marca": "Cisco", "cantidad": 2, "estado": "mantenimiento"},
    {"id": 5, "nombre": "Router Principal", "tipo": "router", "marca": "MikroTik", "cantidad": 2, "estado": "disponible"}
]

@app.route('/')
def home():
    return jsonify({"mensaje": "Bienvenido a NetStock API", "estado": "activo"})

@app.route('/equipos', methods=['GET'])
def get_equipos():
    return jsonify(inventario)

@app.route('/equipos/<int:id_equipo>', methods=['GET'])
def get_equipo_by_id(id_equipo):
    equipo = next((item for item in inventario if item["id"] == id_equipo), None)
    if equipo:
        return jsonify(equipo)
    return jsonify({"error": "Equipo no encontrado"}), 404

@app.route('/equipos/tipo/<string:tipo_equipo>', methods=['GET'])
def get_equipos_by_tipo(tipo_equipo):
    filtrados = [item for item in inventario if item["tipo"].lower() == tipo_equipo.lower()]
    return jsonify(filtrados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)