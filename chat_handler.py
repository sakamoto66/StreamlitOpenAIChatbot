import os
from openai import OpenAI
import streamlit as st

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
MODEL_NAME = "gpt-4o"

class ChatHandler:
    def __init__(self):
        api_key = os.environ.get("OPENAI_API_KEY")
        base_url = os.environ.get("OPENAI_API_BASE_URL", "https://api.openai.com/v1")
        
        if not api_key:
            raise ValueError("OpenAI APIキーが設定されていません。APIキーを設定してください。")
        
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
    def get_ai_response(self, messages):
        try:
            return self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=0.7,
                max_tokens=1000,
                stream=True,
            ), None
        except Exception as e:
            return None, f"Error: {str(e)}"
    
    @staticmethod
    def initialize_session_state():
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system",
                    "content": "You are a helpful and friendly AI assistant. Respond in a concise and engaging manner."
                }
            ]
        if "error" not in st.session_state:
            st.session_state.error = None
    
    @staticmethod
    def add_message(role, content):
        st.session_state.messages.append({"role": role, "content": content})
    
    def process_user_input(self, user_input):
        if not user_input.strip():
            return
        
        # Add user message to chat history
        self.add_message("user", user_input)
        
        # Create empty placeholder for assistant's message
        self.add_message("assistant", "")
        current_message_idx = len(st.session_state.messages) - 1
        
        # Get AI response stream
        stream, error = self.get_ai_response(st.session_state.messages)
        
        if error:
            st.session_state.error = error
            return
        
        # Process streaming response
        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_response += content
                # Update the current message
                st.session_state.messages[current_message_idx]["content"] = full_response
                # Force streamlit to update the display
                st.rerun()
