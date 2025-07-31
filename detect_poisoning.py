from gibberish_text.validator import CleanLabel, Backdoor, LabelFlip, GradientAnomaly
import numpy as np
class DummyModel:
    def predict(self, X, verbose=0):
        return np.array(X)
dummy_model = DummyModel()
X = [[1, 1], [1, 1], [1.1, 1.0], [0.9, 1.2], [1.3, 1.1], [100,100]]
y = [0, 1, 0, 1, 1, 0]
validators = [
    ("CleanLabel", CleanLabel()),
    ("Backdoor", Backdoor()),
    ("LabelFlip", LabelFlip()),
    ("GradientAnomaly", GradientAnomaly())
]
for name, validator in validators:
    if name == "Backdoor":
        result, info = validator.validate({"features": X, "labels": y}, metadata={"model": dummy_model})
    else:
        result, info = validator.validate({"features": X, "labels": y})
    print(f"{name} details: {info}")
    if not result:
        print(f"WARNING: {name} attack detected!")
    else:
        print(f"{name}: No attack detected.")