import streamlit as st
from chat_handler import ChatHandler
from styles import get_css
import streamlit.components.v1 as components
import html

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
    
    # Create main containers
    chat_container = st.container()
    form_container = st.container()
    
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
    
    # Display chat messages
    with chat_container:
        for msg in st.session_state.messages[1:]:  # Skip system message
            role = msg["role"]
            content = msg["content"]
            icon = "👤" if role == "user" else "🤖"
            
            st.markdown(f"""
            <div class="message-wrapper {'user-message-wrapper' if role == 'user' else ''}">
                <div class="message-icon">
                    {icon}
                </div>
                <div class="{role}-message">
                    <div class="message-content">
                        {html.escape(content)}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Input form
    with form_container:
        with st.form(key="chat_form", clear_on_submit=True):
            user_input = st.text_area(
                "メッセージを入力してください...",
                key="user_input_area",
                height=100
            )
            
            submit_button = st.form_submit_button("送信")
            
            if submit_button and user_input and user_input.strip():
                # Add user message to chat history first
                chat_handler.add_message("user", user_input)

                # Get AI response
                response = chat_handler.process_user_input(user_input)
                
                if isinstance(response, str):
                    st.error(response)
                else:
                    # Create placeholder for streaming
                    message_placeholder = st.empty()
                    full_response = ""
                    
                    # Stream the response
                    try:
                        for chunk in response:
                            if chunk.choices[0].delta.content is not None:
                                full_response += chunk.choices[0].delta.content
                                # Display streaming response
                                message_placeholder.markdown(f"""
                                <div class="message-wrapper">
                                    <div class="message-icon">
                                        🤖
                                    </div>
                                    <div class="assistant-message">
                                        <div class="message-content">
                                            {html.escape(full_response)}▌
                                        </div>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                        
                        # Add the complete response to chat history
                        chat_handler.add_message("assistant", full_response)
                        
                        # Clear the placeholder
                        message_placeholder.empty()
                        
                        # Force a rerun without the placeholder
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error during streaming: {str(e)}")
                        message_placeholder.empty()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        Powered by OpenAI GPT-4o
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()