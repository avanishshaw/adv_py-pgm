# flask - python web fw - web apps, rest apis microservices

from flask import Flask, jsonify

#create a flask object
app = Flask(__name__)

@app.route("/users", methods=['GET'])
def home():
    return jsonify({"Users": ["Avanish", "Bob", "Cristian"]})

# run the below code only if this file is executed directly

@app.route("/users/<int:id>", methods=['POST'])
def users(id):
    return jsonify({"Users": [str(id)]})


@app.route("/users/<int:id>", methods=['PATCH'])
def update(id):
    return jsonify({"Updated User": str(id)})


if __name__ == "__main__":
    app.run(debug=True)