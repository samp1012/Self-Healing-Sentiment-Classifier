from dag_nodes import InferenceNode, ConfidenceCheckNode, FallbackNode
from logger import logger

def main():
    inference = InferenceNode()
    confidence = ConfidenceCheckNode()
    fallback = FallbackNode()

    print("Self-Healing Classifier\nType 'exit' to quit.")
    while True:
        text = input("\nInput Text: ")
        if text.lower() == "exit":
            break
        label, conf = inference.run(text)
        if confidence.run(label, conf):
            print(f"Final Label: {label} (Confidence: {conf:.2f})")
        else:
            corrected = fallback.ask_user(text, label)
            print(f"Final Label: {corrected} (Corrected)")

if __name__ == "__main__":
    main()
