# CSS styles for the chat interface
def get_css():
    return """
    <style>
        .chat-container {
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
        
        .user-message {
            background-color: #e6f3ff;
            padding: 1rem;
            border-radius: 15px;
            margin: 1rem 0;
            border-bottom-right-radius: 5px;
        }
        
        .assistant-message {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 15px;
            margin: 1rem 0;
            border-bottom-left-radius: 5px;
        }
        
        .message-header {
            font-size: 0.8rem;
            color: #666;
            margin-bottom: 0.5rem;
        }
        
        .message-content {
            font-size: 1rem;
            line-height: 1.5;
        }
        
        .error-message {
            color: #ff4b4b;
            padding: 1rem;
            border: 1px solid #ff4b4b;
            border-radius: 0.5rem;
            margin: 1rem 0;
        }
    </style>
    """
