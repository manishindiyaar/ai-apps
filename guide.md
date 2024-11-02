# ChatGPT-like App Documentation

## Overview

This application is a simple chat interface built using Streamlit and OpenAI's API. It allows users to interact with a language model, customize the system prompt, and adjust model parameters for a personalized experience.

## Features

- **Interactive Chat Interface**: Users can input messages and receive responses from the AI model.
- **System Prompt Customization**: Users can set a system prompt to guide the AI's behavior.
- **Adjustable Model Parameters**: Users can modify the `temperature` and `max_tokens` to influence the model's response style and length.
- **Chat History Management**: Users can clear the chat history or download it as a text file.

## Setup Instructions

1. **Environment Setup**:
   - Ensure you have Python installed on your system.
   - Install the required packages using pip:
     ```bash
     pip install streamlit openai python-dotenv
     ```

2. **Environment Variables**:
   - Create a `.env` file in the project directory with the following content:
     ```
     NVIDIA_BASE_URL=<your_base_url>
     NVIDIA_API_KEY=<your_api_key>
     ```

3. **Running the Application**:
   - Save the application code in a file named `chat.py`.
   - Run the application using Streamlit:
     ```bash
     streamlit run chat.py
     ```

4. **Using the Application**:
   - Open the application in your web browser.
   - Use the sidebar to set the system prompt and adjust model parameters.
   - Enter your message in the chat input box and press Enter to receive a response.
   - Use the "Clear Chat History" button to reset the conversation.
   - Use the "Download Chat History" button to save the conversation as a text file.

## Customization

- **System Prompt**: Modify the default system prompt in the sidebar to change how the AI responds.
- **Model Parameters**: Adjust the `temperature` for creativity and `max_tokens` for response length.

## Troubleshooting

- **API Key Issues**: Ensure your API key is correctly set in the `.env` file.
- **Model Response**: If the model's responses are not as expected, try adjusting the system prompt or model parameters.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.