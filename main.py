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
    <div class="main-container">
        <div class="chat-container">
            AIアシスタントと自由に会話ができます。どんな質問でもお気軽にどうぞ！
        
            <!-- エラーメッセージ表示エリア -->
            {error_message}
            
            <!-- チャットメッセージ表示エリア -->
            <div id="chat-messages">
                {chat_messages}
            </div>
        </div>
    </div>
    """.format(
        error_message=f"""
        <div class="error-message">
            {st.session_state.error}
        </div>
        """ if st.session_state.error else "",
        chat_messages="".join([
            f"""
            <div class="{message['role']}-message">
                <div class="message-header">
                    {'You' if message['role'] == 'user' else 'AI Assistant'}
                </div>
                <div class="message-content">
                    {message['content']}
                </div>
            </div>
            """ for message in st.session_state.messages[1:]  # システムメッセージをスキップ
        ])
    ), unsafe_allow_html=True)
    
    # メッセージカウンターの初期化
    if "message_counter" not in st.session_state:
        st.session_state.message_counter = 0
    
    # ストリーミングメッセージ用のプレースホルダー
    message_placeholder = st.empty()
    
    # フッター固定の入力エリア
    with st.container():
        st.markdown("""
        <div class="input-container">
            <div class="input-container-inner">
        """, unsafe_allow_html=True)
        
        user_input = st.text_area(
            "メッセージを入力してください...",
            key=f"user_input_{st.session_state.message_counter}",
            height=100
        )
        
        if st.button("送信", key=f"send_button_{st.session_state.message_counter}"):
            if user_input and user_input.strip():
                chat_handler.process_user_input(user_input)
                st.session_state.message_counter += 1
                st.rerun()
        
        st.markdown("""
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        Powered by OpenAI GPT-4o
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
