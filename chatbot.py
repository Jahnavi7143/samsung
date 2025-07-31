import subprocess
from attack_detection import detect_backdoor, detect_clean_label, detect_grad_anomaly, detect_label_flip
import joblib

# Load the trained ML model
try:
    ml_model = joblib.load("attack_classifier.joblib")
except Exception as e:
    ml_model = None
    print("Warning: Could not load ML model. Reason:", e)

def main():
    print("Welcome to the Chatbot! Describe your data or scenario, or type 'help' for options, or 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'help':
            print("Describe your data or scenario in plain text. The chatbot will try to detect if it matches any known attack types (backdoor, clean label, gradient anomaly, label flip) using both pattern matching and a machine learning model. Type 'exit' to quit.")
        else:
            # ML-based detection
            if ml_model:
                ml_pred = ml_model.predict([user_input])[0]
                if ml_pred != "none":
                    print(f"[ML] Predicted attack type: {ml_pred.replace('_', ' ').title()}")
                else:
                    print("[ML] No known attack detected.")
            else:
                print("[ML] Model not available.")

            # Regex-based detection
            results = []
            for func, name in [
                (detect_backdoor, "Backdoor"),
                (detect_clean_label, "Clean Label"),
                (detect_grad_anomaly, "Gradient Anomaly"),
                (detect_label_flip, "Label Flip")
            ]:
                detected, message = func(user_input)
                if detected:
                    results.append(f"{name} Attack: {message}")
            if results:
                print("[Pattern] Attack(s) detected:")
                for r in results:
                    print("-", r)
            else:
                print("[Pattern] No known attack detected.")

if __name__ == "__main__":
    main()