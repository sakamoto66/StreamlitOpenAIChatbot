# CSS styles for the chat interface
def get_css():
    return """
    <style>
        /* Reset and base styles */
        .main-chat-container {
            display: flex;
            flex-direction: column;
            height: 100vh;
            max-width: 800px;
            margin: 0 auto;
            padding: 1rem;
            box-sizing: border-box;
            position: relative;
        }

        /* Messages area */
        .messages-area {
            flex-grow: 1;
            overflow-y: auto;
            margin-bottom: 120px;  /* Space for input area */
            padding: 1rem;
        }

        /* Fixed input area */
        .fixed-input-area {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            padding: 1rem;
            border-top: 1px solid #e2e8f0;
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
            z-index: 1000;
        }

        .input-container {
            max-width: 800px;
            margin: 0 auto;
            display: flex;
            gap: 1rem;
        }

        /* Message styles */
        .message {
            margin-bottom: 1rem;
            padding: 1rem;
            border-radius: 0.5rem;
            animation: slideIn 0.3s ease-out;
        }

        .user-message {
            background-color: #e6f3ff;
            margin-left: 2rem;
        }

        .assistant-message {
            background-color: #f0f2f6;
            margin-right: 2rem;
        }

        .message-header {
            font-size: 0.8rem;
            color: #666;
            margin-bottom: 0.5rem;
        }

        .message-content {
            font-size: 1rem;
            line-height: 1.6;
            color: #2d3748;
        }

        /* Animations */
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

        /* Error message */
        .error-message {
            color: #ff4b4b;
            padding: 1rem;
            border: 1px solid #ff4b4b;
            border-radius: 0.5rem;
            margin: 1rem 0;
            background-color: #fff5f5;
        }

        /* Custom Streamlit elements */
        .stTextArea textarea {
            border-radius: 10px;
            border: 2px solid #e2e8f0;
            padding: 10px;
            font-size: 1rem;
            resize: none;
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
            width: 100%;
        }

        .stButton button:hover {
            background-color: #3182ce;
        }

        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display: none;}
    </style>
    """