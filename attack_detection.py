# attack_detection.py

import re

# Advanced detection with regex and detailed explanations

def detect_backdoor(text):
    patterns = [
        r"backdoor",
        r"trigger( pattern)?",
        r"hidden pattern",
        r"poisoned data",
        r"specific (image|text) (patch|sequence)",
        r"target label"
    ]
    matches = [p for p in patterns if re.search(p, text, re.IGNORECASE)]
    if matches:
        return True, f"Backdoor attack detected. Matched: {', '.join(matches)}."
    return False, "No backdoor attack detected."

def detect_clean_label(text):
    patterns = [
        r"clean label",
        r"poison(ed)? data",
        r"innocent",
        r"label-preserving",
        r"subtle manipulation"
    ]
    matches = [p for p in patterns if re.search(p, text, re.IGNORECASE)]
    if matches:
        return True, f"Clean label attack detected. Matched: {', '.join(matches)}."
    return False, "No clean label attack detected."

def detect_grad_anomaly(text):
    patterns = [
        r"gradient anomaly",
        r"strange gradient",
        r"weird training",
        r"unexpected gradient",
        r"gradient (explosion|vanishing)"
    ]
    matches = [p for p in patterns if re.search(p, text, re.IGNORECASE)]
    if matches:
        return True, f"Gradient anomaly attack detected. Matched: {', '.join(matches)}."
    return False, "No gradient anomaly attack detected."

def detect_label_flip(text):
    patterns = [
        r"label flip",
        r"wrong label",
        r"mislabel",
        r"label switching",
        r"label manipulation"
    ]
    matches = [p for p in patterns if re.search(p, text, re.IGNORECASE)]
    if matches:
        return True, f"Label flip attack detected. Matched: {', '.join(matches)}."
    return False, "No label flip attack detected." 