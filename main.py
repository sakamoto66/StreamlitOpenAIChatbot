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
    st.title("💬 AIチャットアシスタント")
    
    # サイドバーに説明を追加
    with st.sidebar:
        st.markdown("""
        ### 使い方
        1. メッセージを入力欄に書き込む
        2. Sendボタンをクリックするか、Enterキーを押す
        3. AIアシスタントからの返答を待つ
        
        ### 特徴
        - 自然な会話が可能
        - 日本語で対話可能
        - 文脈を理解して返答
        
        ### 注意事項
        - APIキーが必要です
        - 個人情報は送信しないでください
        """)
    
    st.markdown("""
    <div class="chat-container">
        AIアシスタントと自由に会話ができます。どんな質問でもお気軽にどうぞ！
    </div>
    """, unsafe_allow_html=True)
    
    # Display error message if exists
    if st.session_state.error:
        st.markdown(f"""
        <div class="error-message">
            {st.session_state.error}
        </div>
        """, unsafe_allow_html=True)
        st.session_state.error = None
    
    # Initialize message counter in session state if it doesn't exist
    if "message_counter" not in st.session_state:
        st.session_state.message_counter = 0
    
    # Container for all chat content
    main_container = st.container()
    
    # Chat input and send button at the bottom
    input_container = st.container()
    with input_container:
        user_input = st.text_area(
            "Type your message here...",
            key=f"user_input_{st.session_state.message_counter}",
            height=100
        )
        
        # Send button
        if st.button("Send", key=f"send_button_{st.session_state.message_counter}"):
            if user_input and user_input.strip():
                chat_handler.process_user_input(user_input)
                st.session_state.message_counter += 1
                st.rerun()
    
    # Display chat messages above the input
    with main_container:
        # Create a placeholder for streaming messages at the top
        message_placeholder = st.empty()
        
        # Display existing messages
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
    with input_container:
        user_input = st.text_area(
            "Type your message here...",
            key=f"user_input_{st.session_state.message_counter}",
            height=100
        )
        
        # Send button
        if st.button("Send", key=f"send_button_{st.session_state.message_counter}"):
            if user_input and user_input.strip():
                chat_handler.process_user_input(user_input)
                # Increment counter to generate new key for next input
                st.session_state.message_counter += 1
                # Reset message counter to create a new input widget
                st.session_state.message_counter += 1
                # Rerun to refresh the page with new input widget
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
