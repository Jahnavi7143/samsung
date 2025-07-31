from gibberish_text.validator import GradientAnomaly

validator = GradientAnomaly()
X = [[0.1, 0.2], [0.2, 0.1], [5, 5]]  # Last one is an anomalous gradient
y = [0, 0, 0]

result, info = validator.validate({"features": X, "labels": y})
print("Passed:", result)
print("Details:", info) 
