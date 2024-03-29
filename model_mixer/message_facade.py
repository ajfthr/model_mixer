import os

from model_mixer.llm_clients.openai_client import OpenAIClient

openai_api_key = os.environ.get('OPENAI_API_KEY', 'test-key')


class MessageFacade:
    def __init__(self, provider, model, functions=None):
        self.provider = provider
        self.model = model
        self.functions = functions if functions is not None else []

    def send_message(self, message):
        if not isinstance(message, str) or not message:
            raise ValueError("Message must be a non-empty string")

        if self.provider == "openai":
            openai = OpenAIClient(openai_api_key)
            # Assume send_message is a method within OpenAIClient that accepts model and message
            openai.send_message(self.model, message)
        else:
            print(f"Sending message: {message}")
