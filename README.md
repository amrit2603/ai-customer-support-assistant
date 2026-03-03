# AI Customer Support Assistant

An AI-powered Customer Support Assistant built using Streamlit and Large Language Models (LLMs).  
The system performs real-time query classification, sentiment analysis, intelligent response generation, and smart human escalation when necessary.

Unlike a basic chatbot, this project implements a structured decision pipeline that determines whether to respond automatically, redirect, or escalate to human support.

---

## Overview

The system processes each customer query through a multi-step AI workflow:

1. Query Classification  
2. Sentiment Analysis (Positive / Neutral / Negative)  
3. Decision Engine  
4. Response Generation or Human Escalation  

If the detected sentiment is strongly negative or critical, the system flags the case for human intervention instead of responding blindly.

---

## Features

- Automated Query Classification  
- Sentiment Detection (Positive / Neutral / Negative)  
- Color-coded Sentiment Output  
  - 🟢 Positive  
  - 🔴 Negative  
  - ⚪ Neutral  
- Real-time AI Response Generation  
- Smart Escalation Logic  
- Clean and Interactive Streamlit UI  

---

## Demo Video

Watch the project demo here:

[▶ Watch Demo Video]([streamlit-app-2026-03-03-20-32-23.webm](https://github.com/user-attachments/assets/86dba25c-c910-403e-9954-68bf5a23242a))

---

## Screenshots

(<img width="1912" height="1741" alt="screencapture-localhost-8501-2026-03-03-20_48_22" src="https://github.com/user-attachments/assets/8a3476db-3b52-4262-8c7a-ebbf3d35b412" />[streamlit-app-2026-03-03-20-32-23.webm](https://github.com/user-attachments/assets/d9c63809-bfde-4d98-8b76-454fa56d36fc)
<img width="1912" height="2147" alt="screencapture-localhost-8501-2026-03-03-20_43_49" src="https://github.com/user-attachments/assets/aab6fcb6-a636-4ecb-9440-3bb5e9d951d2" />
<img width="1912" height="1741" alt="screencapture-localhost-8501-2026-03-03-20_48_22" src="https://github.com/user-attachments/assets/3b38e8ca-3487-4d69-b3c6-647ce180eccb" />
<img width="1912" height="2410" alt="screencapture-localhost-8501-2026-03-03-20_49_20" src="https://github.com/user-attachments/assets/5b248964-5653-4f0b-8a9a-418c414f3ef2" />
<img width="1912" height="1624" alt="screencapture-localhost-8501-2026-03-03-20_49_54" src="https://github.com/user-attachments/assets/5688417f-e0be-43dc-8566-30bc04fb5a4a" />
)


---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-customer-support-assistant.git
cd ai-customer-support-assistant

### Run the Application
```bash
streamlit run app.py
