 import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load the dataset
df = pd.read_csv("data/symptoms_conditions.csv")

# Split into input and output
X = df["symptoms"]
y = df["condition"]

# Create a pipeline for vectorization and classification
model = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the model
model.fit(X, y)

# Save the model
joblib.dump(model, "model/symptom_checker_model.pkl")
print("✅ Model trained and saved as model/symptom_checker_model.pkl")
