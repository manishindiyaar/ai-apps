import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up the OpenAI client
client = OpenAI(
    base_url=os.getenv('NVIDIA_BASE_URL'),
    api_key=os.getenv('NVIDIA_API_KEY')
)

# Set the title of the app
st.title("ChatGPT-like App")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for additional functionalities
st.sidebar.title("Settings")

# System prompt input
system_prompt = st.sidebar.text_area("System Prompt", "You are a helpful assistant.")

# Clear chat history
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []

# Adjustable model parameters
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2)
max_tokens = st.sidebar.slider("Max Tokens", 50, 1024, 102)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from OpenAI
    with st.chat_message("assistant"):
        # Include the system prompt in the messages
        messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages

        response = client.chat.completions.create(
            model="nvidia/nemotron-4-340b-instruct",
            messages=messages,
            temperature=temperature,
            top_p=0.7,
            max_tokens=max_tokens,
            stream=False,
            
        )
        response_text = response.choices[0].message.content.strip()

        # Display assistant response in chat message container
        st.markdown(response_text)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_text})

# Save chat history
if st.sidebar.button("Download Chat History"):
    chat_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
    st.sidebar.download_button("Download", chat_history, "chat_history.txt")