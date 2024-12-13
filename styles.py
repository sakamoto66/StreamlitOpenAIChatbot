# CSS styles for the chat interface
def get_css():
    return """
    <style>
        .chat-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 1rem;
            display: flex;
            flex-direction: column;
            height: calc(100vh - 200px);
            position: relative;
        }
        
        .chat-messages {
            flex-grow: 1;
            overflow-y: auto;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        .message-wrapper {
            display: flex;
            align-items: flex-start;
            margin: 1rem 0;
            gap: 8px;
        }
        
        .user-message-wrapper {
            flex-direction: row-reverse;
        }
        
        .message-icon {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        
        .user-message {
            background-color: #f1f1f1;
            padding: 1rem;
            border-radius: 20px;
            border-bottom-right-radius: 5px;
            margin-right: 12px;
            position: relative;
            max-width: 80%;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
            animation: slideIn 0.3s ease-out;
        }
        
        .assistant-message {
            background-color: white;
            padding: 1rem;
            border-radius: 20px;
            border-bottom-left-radius: 5px;
            margin-left: 12px;
            position: relative;
            max-width: 80%;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
            animation: slideIn 0.3s ease-out;
        }
        
        .message-content {
            font-size: 1rem;
            line-height: 1.6;
            color: #333;
            word-wrap: break-word;
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
