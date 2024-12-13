# CSS styles for the chat interface
def get_css():
    return """
    <style>
        /* Reset default margins and padding */
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        
        /* メインコンテナのスタイル */
        .main-container {
            position: relative;
            height: 100vh;
            max-width: 800px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
        }
        
        /* チャットメッセージエリアのスタイル */
        .chat-container {
            flex: 1;
            overflow-y: auto;
            padding: 1rem;
            padding-bottom: 200px; /* フッターの高さ分の余白 */
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
        }
        
        /* フッター固定入力エリアのスタイル */
        .input-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            padding: 1rem;
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
            z-index: 1000;
            border-top: 1px solid #e2e8f0;
        }
        
        .input-container-inner {
            max-width: 800px;
            margin: 0 auto;
            padding: 0 1rem;
        }
        
        .user-message {
            background-color: #e6f3ff;
            padding: 1rem;
            border-radius: 15px;
            margin: 1rem 0;
            border-bottom-right-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            animation: slideIn 0.3s ease-out;
        }
        
        .assistant-message {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 15px;
            margin: 1rem 0;
            border-bottom-left-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            animation: slideIn 0.3s ease-out;
        }
        
        .message-header {
            font-size: 0.8rem;
            color: #666;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }
        
        .message-content {
            font-size: 1rem;
            line-height: 1.6;
            color: #2d3748;
        }
        
        .error-message {
            color: #ff4b4b;
            padding: 1rem;
            border: 1px solid #ff4b4b;
            border-radius: 0.5rem;
            margin: 1rem 0;
            background-color: #fff5f5;
            animation: fadeIn 0.3s ease-out;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        /* Streamlitのデフォルトスタイルのカスタマイズ */
        .stTextArea textarea {
            border-radius: 10px;
            border: 2px solid #e2e8f0;
            padding: 10px;
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }

        .stTextArea textarea:focus {
            border-color: #4299e1;
            box-shadow: 0 0 0 1px #4299e1;
        }

        .stButton button {
            border-radius: 8px;
            padding: 0.5rem 2rem;
            background-color: #4299e1;
            color: white;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .stButton button:hover {
            background-color: #3182ce;
            transform: translateY(-1px);
        }
    </style>
    """
