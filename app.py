import streamlit as st
import os
from dotenv import load_dotenv
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

st.markdown("""
<style>
    .stTextArea textarea {
        font-size: 16px;
    }
    .stButton button {
        font-size: 16px;
        height: 3em;
    }
</style>
""", unsafe_allow_html=True)

# Load environment
load_dotenv()

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
)

# -------------------------
# State Definition
# -------------------------
class State(TypedDict):
    query: str
    category: str
    sentiment: str
    response: str


# -------------------------
# Functions (OUTSIDE class)
# -------------------------
def categorize(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Categorize the following query into one of: Technical, Billing, General. "
        "Respond with only one word. Query: {query}"
    )
    chain = prompt | llm
    category = chain.invoke({"query": state["query"]}).content.strip()
    return {"category": category}


def analyze_sentiment(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Analyze the sentiment of the following query. "
        "Respond with only one word: Positive, Neutral, or Negative. "
        "Query: {query}"
    )
    chain = prompt | llm
    sentiment = chain.invoke({"query": state["query"]}).content.strip()
    return {"sentiment": sentiment}


def handle_technical(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Provide a technical support response to the following query: {query}"
    )
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]}).content.strip()
    return {"response": response}


def handle_billing(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Provide a billing support response to the following query: {query}"
    )
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]}).content.strip()
    return {"response": response}


def handle_general(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Provide a general support response to the following query: {query}"
    )
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]}).content.strip()
    return {"response": response}


def escalate(state: State) -> State:
    return {
        "response": "This query has been escalated to a human agent due to negative sentiment."
    }


def route_query(state: State) -> str:
    if state["sentiment"] == "Negative":
        return "escalate"
    elif state["category"] == "Technical":
        return "handle_technical"
    elif state["category"] == "Billing":
        return "handle_billing"
    else:
        return "handle_general"


# -------------------------
# Build Workflow
# -------------------------
workflow = StateGraph(State)

workflow.add_node("categorize", categorize)
workflow.add_node("analyze_sentiment", analyze_sentiment)
workflow.add_node("handle_technical", handle_technical)
workflow.add_node("handle_billing", handle_billing)
workflow.add_node("handle_general", handle_general)
workflow.add_node("escalate", escalate)

workflow.set_entry_point("categorize")
workflow.add_edge("categorize", "analyze_sentiment")

workflow.add_conditional_edges(
    "analyze_sentiment",
    route_query,
    ["escalate", "handle_technical", "handle_billing", "handle_general"]
)

workflow.add_edge("handle_technical", END)
workflow.add_edge("handle_billing", END)
workflow.add_edge("handle_general", END)
workflow.add_edge("escalate", END)

app_graph = workflow.compile()


# -------------------------
# -------------------------
# Streamlit UI
# -------------------------

st.set_page_config(page_title="AI Customer Support", page_icon="🤖", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center;'>🤖 AI Customer Support Assistant</h1>
    <p style='text-align: center; color: gray;'>
        Automated query classification and response system
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

query = st.text_area("Enter your customer query below:", height=100)

if st.button("Submit Query", use_container_width=True) and query:

    with st.spinner("Processing your request..."):
        results = app_graph.invoke({"query": query})

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📂 Category")
        st.success(results["category"])

    with col2:
        st.markdown("### 💬 Sentiment")
        sentiment = results["sentiment"]

        if "Negative" in sentiment:
            st.error(sentiment)
        elif "Positive" in sentiment:
            st.success(sentiment)
        else:
            st.info(sentiment)

    st.markdown("### 📝 Response")
    st.write(results["response"])