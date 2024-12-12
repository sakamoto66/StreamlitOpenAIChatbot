import streamlit as st
from chat_handler import ChatHandler
from styles import get_css
import streamlit.components.v1 as components

def main():
    st.set_page_config(
        page_title="AI Chat Assistant",
        page_icon="💬",
        layout="wide"
    )
    
    # Initialize chat handler
    try:
        chat_handler = ChatHandler()
        chat_handler.initialize_session_state()
    except ValueError as e:
        st.error(str(e))
        st.stop()
    
    # Inject custom CSS
    components.html(get_css(), height=0)
    
    # Header
    st.title("💬 AI Chat Assistant")
    st.markdown("""
    Welcome to the AI Chat Assistant! Ask me anything, and I'll do my best to help you.
    """)
    
    # Display error message if exists
    if st.session_state.error:
        st.markdown(f"""
        <div class="error-message">
            {st.session_state.error}
        </div>
        """, unsafe_allow_html=True)
        st.session_state.error = None
    
    # Display chat messages
    for message in st.session_state.messages[1:]:  # Skip the system message
        role = message["role"]
        content = message["content"]
        
        st.markdown(f"""
        <div class="{role}-message">
            <div class="message-header">
                {'You' if role == 'user' else 'AI Assistant'}
            </div>
            <div class="message-content">
                {content}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Chat input
    user_input = st.text_area("Type your message here...", key="user_input", height=100)
    
    # Send button
    if st.button("Send", key="send_button") and user_input:
        chat_handler.process_user_input(user_input)
        # Reset the text input widget using session state
        st.session_state["user_input"] = ""
        # Rerun to update the chat display
        st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        Powered by OpenAI GPT-4o
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
