
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

# -----------------------------
# 1. Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI-Powered Smart Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 AI-Powered Smart Chatbot")
st.write(
    "Ask questions and receive AI-generated answers "
    "using a locally running language model."
)

# -----------------------------
# 2. Sidebar Settings
# -----------------------------
with st.sidebar:
    st.header("Chatbot Settings")

    model_name = st.selectbox(
        "Choose Model",
        ["llama3.2:3b"],
    )

    st.caption("Powered by Ollama and LangChain.")

    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.write("Built with Python, Streamlit, LangChain and Ollama.")

# -----------------------------
# 3. Initialize Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# 4. Configure Language Model
# -----------------------------
llm = ChatOllama(
    model=model_name,
    temperature=0.3,
)

system_prompt = (
    "You are a helpful AI assistant. "
    "Answer questions clearly and accurately using simple language. "
    "If you do not know an answer, say so honestly."
)

# -----------------------------
# 5. Display Previous Messages
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# 6. Receive User Input
# -----------------------------
user_question = st.chat_input("Type your question here...")

if user_question:
    # Save and display the user's message
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    # Build conversation history for the model
    chat_history = [SystemMessage(content=system_prompt)]

    # Use recent messages to limit context size
    for message in st.session_state.messages[-12:]:
        if message["role"] == "user":
            chat_history.append(
                HumanMessage(content=message["content"])
            )
        else:
            chat_history.append(
                AIMessage(content=message["content"])
            )

    # Generate and display the AI response
    with st.chat_message("assistant"):
        try:
            with st.spinner("AI is thinking..."):
                response = llm.invoke(chat_history)

            answer = response.content

            if not isinstance(answer, str):
                answer = str(answer)

            st.markdown(answer)

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        except Exception as error:
            st.error(
                "Unable to connect to the AI model. "
                "Make sure Ollama is running and the model is installed."
            )
            st.caption(f"Technical details: {error}")
