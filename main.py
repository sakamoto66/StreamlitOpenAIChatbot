import streamlit as st
from chat_handler import ChatHandler
from styles import get_css
import streamlit.components.v1 as components

def main():
    st.set_page_config(
        page_title="AI Chat Assistant",
        page_icon="💬",
        layout="wide",
        initial_sidebar_state="collapsed"
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
    
    # Header and sidebar
    st.title("💬 AIチャットアシスタント")
    
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
    
    # Main chat container
    st.markdown("""
        <div class="main-chat-container">
            <div class="messages-area">
                <!-- Error message -->
                {}
                
                <!-- Chat messages -->
                {}
            </div>
        </div>
    """.format(
        f'<div class="error-message">{st.session_state.error}</div>' if st.session_state.error else '',
        ''.join([
            f'''
            <div class="message {'user-message' if message['role'] == 'user' else 'assistant-message'}">
                <div class="message-header">
                    {'あなた' if message['role'] == 'user' else 'AI アシスタント'}
                </div>
                <div class="message-content">
                    {message['content']}
                </div>
            </div>
            ''' for message in st.session_state.messages[1:]  # Skip system message
        ])
    ), unsafe_allow_html=True)
    
    # Fixed input area container
    st.markdown('<div class="fixed-input-area">', unsafe_allow_html=True)
    
    # Input container
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    # Message counter for unique keys
    if "message_counter" not in st.session_state:
        st.session_state.message_counter = 0
    
    # Input columns
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_area(
            "メッセージを入力してください...",
            key=f"user_input_{st.session_state.message_counter}",
            height=100,
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.button(
            "送信",
            key=f"send_button_{st.session_state.message_counter}",
            use_container_width=True
        )
    
    # Close containers
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    # Handle user input
    if send_button and user_input and user_input.strip():
        chat_handler.process_user_input(user_input)
        st.session_state.message_counter += 1
        st.rerun()

if __name__ == "__main__":
    main()