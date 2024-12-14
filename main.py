import streamlit as st
from chat_handler import ChatHandler
from styles import get_css
import streamlit.components.v1 as components
import html


def show_user_message(st, content):
    st.html('<div class="message-wrapper user-message-wrapper">')
    st.html('  <div class="message-icon">👤</div>')
    st.html('  <div class="user-message">')
    st.html('    <div class="message-content">')
    st.html(html.escape(content))
    st.html('    </div>')
    st.html('  </div>')
    st.html('</div>')


def show_assistant_message(st):
    st.html('<div class="message-wrapper">')
    st.html('  <div class="message-icon">🤖</div>')
    st.html('  <div class="assistant-message">')
    st.html('    <div class="message-content">')
    message_placeholder = st.empty()
    st.html('    </div>')
    st.html('  </div>')
    st.html('</div>')
    return message_placeholder


def show_footer(chat_handler, counter):
    # Chat input with dynamic key
    user_input = st.text_area("Type your message here...",
                              key=f"user_input_{counter}",
                              height=100)

    # Send button
    if st.button("Send", key=f"send_button_{counter}"):
        if user_input and user_input.strip():
            #chat_handler.process_user_input(user_input)
            chat_handler.add_message("user", user_input)
            # Increment counter to generate new key for next input
            st.session_state.message_counter = counter + 1
            # Rerun to update the chat display
            st.rerun()


def main():
    st.set_page_config(page_title="AI Chat Assistant",
                       page_icon="💬",
                       layout="wide")

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

    st.html("""
    <div class="chat-container">
        AIアシスタントと自由に会話ができます。どんな質問でもお気軽にどうぞ！
    </div>
    """)

    # Display error message if exists
    if st.session_state.error:
        st.markdown(f"""
        <div class="error-message">
            {st.session_state.error}
        </div>
        """,
                    unsafe_allow_html=True)
        st.session_state.error = None

    # Initialize message counter in session state if it doesn't exist
    if "message_counter" not in st.session_state:
        st.session_state.message_counter = 0

    # Display chat messages
    st.html('<div class="chat-messages">')
    for message in st.session_state.messages[1:]:  # Skip the system message
        role = message["role"]
        content = message["content"]
        if role == "user":
            show_user_message(st, content)
        else:
            message_placeholder = show_assistant_message(st)
            message_placeholder.markdown(content)

    # Create a placeholder for the assistant's message
    if st.session_state.message_counter > 0 and st.session_state.messages[-1][
            "role"] == "user":
        message_placeholder = show_assistant_message(st)
        st.html('</div>')
        show_footer(chat_handler, st.session_state.message_counter + 1)
        full_response = ""

        # Get streaming response
        response, error = chat_handler.get_ai_response(
            st.session_state.messages)

        if error:
            st.session_state.error = error
        else:
            # Display streaming response
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response)

            # Save the complete response
            chat_handler.add_message("assistant", full_response)
            # Increment counter to generate new key for next input
            st.session_state.message_counter += 1
    else:
        st.html('</div>')
        show_footer(chat_handler, st.session_state.message_counter)
    # Footer
    st.markdown("---")
    st.html("""
    <div style="text-align: center; color: #666;">
        Powered by OpenAI GPT-4o
    </div>
    """)


if __name__ == "__main__":
    main()
