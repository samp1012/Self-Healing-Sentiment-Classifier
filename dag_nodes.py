import requests
import json
from logger import logger

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"  

def query_ollama(prompt: str) -> str:
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]

class InferenceNode:
    def run(self, text):
        prompt = f"Classify the sentiment of this sentence as Positive or Negative. Just return the label and confidence in %.\n\nSentence: \"{text}\"\n"
        response = query_ollama(prompt)
        logger.info(f"[InferenceNode] Raw response: {response}")

        # Expecting output like: "Negative (confidence: 64%)"
        import re
        match = re.search(r"(Positive|Negative).*?(\d{1,3})%", response, re.IGNORECASE)
        if match:
            label = match.group(1).capitalize()
            confidence = int(match.group(2)) / 100
        else:
            label = "Unknown"
            confidence = 0.0
        logger.info(f"[InferenceNode] Label: {label} | Confidence: {confidence}")
        return label, confidence

class ConfidenceCheckNode:
    def __init__(self, threshold=0.85):
        self.threshold = threshold

    def run(self, label, confidence):
        if confidence < self.threshold:
            logger.info("[ConfidenceCheckNode] Confidence too low. Triggering fallback...")
            return False
        return True

class FallbackNode:
    def ask_user(self, text, label):
        print(f"[FallbackNode] The system predicted: {label}. Was that correct for: \"{text}\"? (yes/no)")
        user = input("User: ").strip().lower()
        if user == "yes":
            final = label
        else:
            final = "Negative" if label == "Positive" else "Positive"
        logger.info(f"[FallbackNode] Final label after user correction: {final}")
        return final
