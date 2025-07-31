from gibberish_text.validator import LabelFlip


validator = LabelFlip()

X = [[1, 2], [2, 3], [3, 4], [100, 200]]   
y = [0, 0, 0, 0]                 

result, info = validator.validate({"features": X, "labels": y})

print("Passed:", result)
print("Details:", info) 