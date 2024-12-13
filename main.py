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
    
    # チャットメッセージ表示用のコンテナ
    with st.container():
        # ストリーミングメッセージ用のプレースホルダー
        stream_placeholder = st.empty()
        
        # 既存のメッセージを表示
        for msg in st.session_state.messages[1:]:  # システムメッセージをスキップ
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
    
    # 入力フォーム
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_area(
            "メッセージを入力してください...",
            key="user_input",
            height=100
        )
        
        submit_button = st.form_submit_button("送信")
        
        if submit_button and user_input and user_input.strip():
            # ユーザーメッセージをチャット履歴に追加
            chat_handler.add_message("user", user_input)
            
            # AI応答を取得
            response = chat_handler.process_user_input(user_input)
            
            if isinstance(response, str):
                st.error(response)
            else:
                full_response = ""
                try:
                    # レスポンスをストリーミング
                    for chunk in response:
                        if chunk.choices[0].delta.content is not None:
                            full_response += chunk.choices[0].delta.content
                            stream_placeholder.markdown(f"""
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
                    
                    # 完全な応答をチャット履歴に追加
                    chat_handler.add_message("assistant", full_response)
                    
                    # プレースホルダーをクリア
                    stream_placeholder.empty()
                    
                    # メッセージを表示するために新しいメッセージを追加
                    st.session_state.messages = st.session_state.messages
                    
                except Exception as e:
                    st.error(f"Error during streaming: {str(e)}")
                    stream_placeholder.empty()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        Powered by OpenAI GPT-4o
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()