class ModelOverloadedError(BaseException):
    """
    HF Model Overloaded Error

    Raised when hf return response `{"error":"Model is overloaded", "error_type":"overloaded"}`
    """
    pass


class ChatBotInitError(BaseException):
    """
    ChatBot Init Error

    Raised when chatbot init failed
    """
    pass


class CreateConversationError(BaseException):
    """
    Create Conversation Error

    Raised when create conversation failed
    """
    pass


class InvalidConversationIDError(BaseException):
    """
    Invalid Conversation ID Error

    Raised when using a invalid conversation id
    """
    pass


class DeleteConversationError(BaseException):
    """
    Delete Conversation Error

    Raised when delete conversation failed
    """
    pass


class ChatError(BaseException):
    """
    Chat Error

    Raised when chat failed
    """
    pass