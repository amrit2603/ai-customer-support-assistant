# AI Customer Support Assistant

An AI-powered Customer Support Assistant built using Streamlit and Large Language Models (LLMs) that performs real-time query classification, sentiment analysis, intelligent response generation, and smart human escalation when necessary.

This project simulates a structured customer support workflow rather than just a chatbot by incorporating decision logic and escalation handling.

---

## Overview

The system processes customer queries through a multi-step AI pipeline:

1. Query Classification  
2. Sentiment Analysis (Positive / Neutral / Negative)  
3. Decision Engine  
4. Response Generation or Human Escalation  

If the sentiment is strongly negative or indicates critical concern, the system flags the case for human intervention instead of responding automatically.

---

## Features

- Automated Query Classification  
- Sentiment Detection (Positive / Neutral / Negative)  
- Color-coded Sentiment Output  
  - 🟢 Positive  
  - 🔴 Negative  
  - ⚪ Neutral  
- Real-time AI Response Generation  
- Smart Escalation Logic for Human Support  
- Clean and Interactive Streamlit UI  

---

## Demo Video

Watch the project demo here:

[Watch the Demo Video](ADD_YOUR_VIDEO_LINK_HERE)

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-customer-support-assistant.git
cd ai-customer-support-assistant

## 4. Configure Environment Variables

Create a `.env` file in the root directory of the project:

```env
API_KEY=your_api_key_here
MODEL_NAME=your_model_name_here

API_KEY=your_api_key_here
MODEL_NAME=your_model_name_here

streamlit run app.py

Project Structure
AI-Customer-Support-Assistant/
│
├── app.py
├── notebook.ipynb
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

System Architecture
User
  ↓
Streamlit UI
  ↓
LLM Processing
  ↓
Classification + Sentiment Analysis
  ↓
Decision Engine
  ↓
Response Generation
        OR
Human Escalation
