from flask import Flask, request, jsonify
import joblib

# Load the trained model
model = joblib.load("model/symptom_checker_model.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    symptoms = data.get("symptoms", "")
    
    if not symptoms:
        return jsonify({"error": "No symptoms provided!"}), 400
    
    # Predict condition
    prediction = model.predict([symptoms])[0]
    
    return jsonify({"condition": prediction})

if __name__ == "__main__":
    app.run(debug=True)
