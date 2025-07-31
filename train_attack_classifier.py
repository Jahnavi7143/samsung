import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# Synthetic dataset: (description, label)
data = [
    ("This contains a backdoor trigger in the data.", "backdoor"),
    ("Poisoned data with a specific image patch is present.", "backdoor"),
    ("Clean label attack with subtle manipulation.", "clean_label"),
    ("Innocent looking data but labels are poisoned.", "clean_label"),
    ("There is a gradient anomaly during training.", "grad_anomaly"),
    ("Unexpected gradient explosion detected.", "grad_anomaly"),
    ("Label flip attack: wrong label assigned.", "label_flip"),
    ("Some samples have mislabeling issues.", "label_flip"),
    ("Normal data with no attack.", "none"),
    ("Standard training, no anomalies detected.", "none"),
]

texts, labels = zip(*data)

# Create a pipeline: TF-IDF + Logistic Regression
pipeline = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression(max_iter=200)
)

# Train the model
pipeline.fit(texts, labels)

# Save the model
joblib.dump(pipeline, "attack_classifier.joblib")
print("Model trained and saved as attack_classifier.joblib") 