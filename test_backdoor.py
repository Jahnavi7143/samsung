from gibberish_text.validator import Backdoor

class DummyModel:
    def predict(self, X, verbose=0):
        return X  

v = Backdoor()

X = [
    [0.1, 0.2], 
    [0.2, 0.1],
    [999, 999], 
    [0.3, 0.4]
]
y = [0, 0, 0, 0]

result, info = v.validate({"features": X, "labels": y}, metadata={"model": DummyModel()})

print("Passed:", result)
print("Details:", info) 

