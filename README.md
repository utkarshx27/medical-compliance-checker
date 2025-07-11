# Medical Claim Compliance Checker

A web-based tool to evaluate the **FDA compliance** of medical product claims using a powerful LLM (LLaMA 3.1 8B Instant via Groq) integrated with LangChain and Streamlit. Designed for **regulatory professionals**, **medical marketers**, and **health tech reviewers**, this tool helps classify whether a medical claim aligns with U.S. FDA promotional regulations.

---
## Features

- **Compliant / Non-compliant Classification**
- **Brief Explanation** for Non-compliant outputs
- **LLM-Driven Evaluation** powered by Groq + LangChain
- **Regulation-Aware Prompting** following key FDA advertising standards

---

## FDA Rules Implemented

The LLM checks against key FDA regulatory criteria such as:

- Off-label promotion
- Superiority claims without evidence
- Risk omission or unbalanced benefits
- Exaggerated, unverifiable, or misleading claims
- Inappropriate social media marketing
- Lack of clinical substantiation
- Misleading endorsements or testimonials
---
## Demo

![App Screenshot](https://github.com/utkarshx27/medical-compliance-checker/blob/84be165c4b4613f68dc86cfa3eafc81a0b9f3ac8/demo_ss/Screenshot%202025-07-10%20231204.png)

## Evaluation:

```
Accuracy: 0.96
Precision (Compliant): 0.92
Recall (Compliant): 1.00
F1 Score (Compliant): 0.96

Classification Report:
               precision    recall  f1-score   support

    Compliant       0.92      1.00      0.96        11
Non-Compliant       1.00      0.93      0.96        14

     accuracy                           0.96        25
    macro avg       0.96      0.96      0.96        25
 weighted avg       0.96      0.96      0.96        25
```
![eval_CM](https://github.com/utkarshx27/medical-compliance-checker/blob/4618f4c0c43723019f7deb6b74bb94f5c68c6f50/demo_ss/output.png)
---



---

## Tech Stack

- [Streamlit](https://streamlit.io/) – UI
- [LangChain](https://www.langchain.com/) – LLM orchestration
- [Groq API](https://console.groq.com/) – LLaMA 3.1-8B model backend
- [Pydantic](https://docs.pydantic.dev/) – Data validation

---

## Installation

### 1. Clone the repository

### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3. Set your API key
Create a .env file in the root directory or just update **groq api** key in app.py
```
GROQ_API_KEY=your_groq_api_key
```
### 4. Run the app
```
streamlit run app.py
```
