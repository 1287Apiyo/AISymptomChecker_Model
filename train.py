import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib


df = pd.read_csv("data/symptoms_conditions.csv")


X = df["symptoms"]
y = df["condition"]

# Create a pipeline for vectorization 
model = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])


model.fit(X, y)


joblib.dump(model, "model/symptom_checker_model.pkl")
print("✅ Model trained and saved as model/symptom_checker_model.pkl")
