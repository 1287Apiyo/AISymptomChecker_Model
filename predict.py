import joblib

# Load the trained modell
model = joblib.load("model/symptom_checker_model.pkl")

print("AI Symptom Checker")
print("Type your symptoms separated by commas (e.g. fever, cough, sore throat)")
user_input = input("Your symptoms: ")

# Make prediction
prediction = model.predict([user_input])[0]

print(f"\nLikely condition: {prediction}")
