from gibberish_text.validator import CleanLabel

validator = CleanLabel()
X = {1,2,3}
y = {1,2,3}  # Your labels (list or numpy array)

result, info = validator.validate({"features": X, "labels": y})
if not result:
    print("WARNING: Possible data poisoning detected!")
    print("Details:", info)
else:
    print("Dataset appears clean.") 