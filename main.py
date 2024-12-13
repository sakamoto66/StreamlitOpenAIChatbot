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
    
    # チャットコンテナ
    chat_container = st.container()
    
    # 入力エリア
    input_container = st.container()
    
    with input_container:
        # フォームを使用してユーザー入力を管理
        with st.form(key="chat_form", clear_on_submit=True):
            user_input = st.text_area(
                "メッセージを入力してください...",
                key="user_input_area",
                height=100
            )
            
            # Submit button
            submit_button = st.form_submit_button("送信")
            
            if submit_button and user_input and user_input.strip():
                # Add user message to chat history
                chat_handler.add_message("user", user_input)
                # Rerun to update UI immediately
                st.rerun()
    
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
        
        # Handle streaming response if there's a new user message
        if st.session_state.messages[-1]["role"] == "user":
            response, error = chat_handler.get_ai_response(st.session_state.messages)
            
            if error:
                st.error(error)
            else:
                # Create placeholder for streaming response
                message_placeholder = st.empty()
                full_response = ""
                
                # Display streaming response
                for chunk in response:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
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
                
                # Remove the typing indicator
                message_placeholder.empty()
                
                # Rerun to update UI with the new message
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