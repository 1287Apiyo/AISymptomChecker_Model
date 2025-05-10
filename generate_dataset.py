import pandas as pd

data = [
    {
        "symptoms": "fever,cough,sore throat",
        "condition": "Common Cold",
        "urgency": "Low"
    },
    {
        "symptoms": "fever,headache,stiff neck",
        "condition": "Meningitis",
        "urgency": "High"
    },
    {
        "symptoms": "chest pain,shortness of breath",
        "condition": "Heart Attack",
        "urgency": "High"
    },
    {
        "symptoms": "nausea,vomiting,diarrhea",
        "condition": "Food Poisoning",
        "urgency": "Medium"
    },
    {
        "symptoms": "fatigue,weight loss,night sweats",
        "condition": "Tuberculosis",
        "urgency": "High"
    },
    {
        "symptoms": "sneezing,itchy eyes,runny nose",
        "condition": "Allergic Rhinitis",
        "urgency": "Low"
    },
    {
        "symptoms": "abdominal pain,bloating,constipation",
        "condition": "Irritable Bowel Syndrome",
        "urgency": "Medium"
    },
    {
        "symptoms": "dizziness,blurred vision,slurred speech",
        "condition": "Stroke",
        "urgency": "High"
    },
    {
        "symptoms": "fever,headache,loss of appetite",
        "condition": "Malaria",
        "urgency": "High"
    },
    {
        "symptoms": "joint pain,rash,fever",
        "condition": "Dengue",
        "urgency": "High"
    },
]

df = pd.DataFrame(data)
df.to_csv("data/symptoms_conditions.csv", index=False)
print("✅ Dataset saved to data/symptoms_conditions.csv")
