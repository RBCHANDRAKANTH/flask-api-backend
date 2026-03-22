from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = [{"name": "chandra", "role": "admin"}]

@app.route("/")
def home():
    return "Flask API Running"

# CREATE
@app.route("/data", methods=["POST"])
def create_data():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    data_store.append(data)
    return jsonify({"message": "Data added"}), 201

# READ
@app.route("/data", methods=["GET"])
def read_data():
    return jsonify(data_store)

# UPDATE
@app.route("/data/<int:index>", methods=["PUT"])
def update_data(index):
    if index < len(data_store):
        new_data = request.get_json()
        data_store[index] = new_data
        return jsonify({"message": "Updated"})
    return jsonify({"error": "Not found"}), 404

# DELETE
@app.route("/data/<int:index>", methods=["DELETE"])
def delete_data(index):
    if index < len(data_store):
        data_store.pop(index)
        return jsonify({"message": "Deleted"})
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)