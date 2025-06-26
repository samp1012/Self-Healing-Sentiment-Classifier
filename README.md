# 🧠 Self-Healing Sentiment Classifier

An adaptive command-line sentiment classifier powered by a local LLM (via Ollama) with confidence checks and fallback correction through human feedback. Designed to improve predictions over time with minimal supervision.

---

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [System Architecture](#system-architecture)
- [Logs](#logs)
- [Technologies Used](#technologies-used)
- [Contact](#contact)

---

## ✅ Features

- 🔍 **Sentiment Classification**: Classifies text as *Positive* or *Negative* using an LLM.
- 📉 **Confidence Thresholding**: Falls back to user verification if the model confidence is too low.
- 🔁 **Self-Healing**: System corrects its prediction based on user feedback.
- 📂 **Structured Logging**: All events logged in `logs.txt` for review and analysis.
- 🧪 **Modular Nodes**: Clean DAG-based node system (Inference, Confidence, Fallback).
- 🖥️ **Simple CLI Interface**: Minimal, interactive, and user-driven.

---

## 📁 Project Structure

```
Self-Healing-Sentiment-Classifier/
├── main_cli.py           # Entry point for running the CLI classifier
├── dag_nodes.py          # Contains node logic (inference, confidence check, fallback)
├── logger.py             # Logger configuration for logs.txt
├── logs.txt              # System-generated logs
├── requirements.txt      # Python dependencies
├── .gitignore            # Files and folders to ignore in git
└── README.md             # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/samp1012/Self-Healing-Sentiment-Classifier.git
cd Self-Healing-Sentiment-Classifier
```

2. **(Optional) Create a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install the dependencies**:
```bash
pip install -r requirements.txt
```

4. **Ensure Ollama is running locally**:
- Install and run Ollama: https://ollama.com/
- Pull model used (e.g., llama3): `ollama pull llama3`

---

## 🚀 Usage

Run the classifier from the terminal:
```bash
python main_cli.py
```

Then follow the prompts:
- Enter any sentence to classify.
- If the confidence is high, the label is printed.
- If not, you’re asked to confirm or correct it.

Example:
```
Input Text: I hate waiting for hours.
System predicted: Negative (Confidence: 72%)
[FallbackNode] Was that correct? (yes/no)
```

---

## 🧠 System Architecture

```
User Input
    │
    ▼
[InferenceNode] ──► Classifies using LLM (Ollama)
    │
    ▼
[ConfidenceCheckNode] ──► Accept or reject based on threshold (default: 85%)
    │
    ▼
[FallbackNode] ──► If rejected, ask user for correction
```

Each interaction is logged in `logs.txt` with timestamp and decision flow.

---

## 🪵 Logs

All interactions and decision points are saved to `logs.txt` using Python’s logging module:
```
2025-06-26 06:58:11,814 - [InferenceNode] Label: Negative | Confidence: 0.75
2025-06-26 06:58:11,814 - [ConfidenceCheckNode] Confidence too low. Triggering fallback...
2025-06-26 06:58:17,258 - [FallbackNode] Final label after user correction: Negative
```

---

## 🧰 Technologies Used

- **Python 3**
- **Ollama** (Local LLM inference)
- **Requests** (HTTP calls to local LLM API)
- **Logging** (for tracking decisions and corrections)

---

## 📬 Contact

For feedback, suggestions, or contributions:

- GitHub: [samp1012](https://github.com/samp1012)
- Email: [samparkadas@gmail.com](mailto:samparkadas@gmail.com)
- LinkedIn: [Samparka Das](https://www.linkedin.com/in/samparka-das-b4317726b/)

---
