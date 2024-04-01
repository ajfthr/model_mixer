import os

from model_mixer.llm_clients.openai_client import OpenAIClient

openai_api_key = os.environ.get('OPENAI_API_KEY', 'test-key')


class MessageFacade:
    def __init__(self, provider, model, functions=None):
        self.provider = provider
        self.model = model
        self.functions = functions if functions is not None else []

    def send_message(self, message) -> str:
        if not isinstance(message, str) or not message:
            raise ValueError("Message must be a non-empty string")

        if self.provider == "openai":
            openai = OpenAIClient(openai_api_key)
            return openai.send_message(message, self.model)
        else:
            print(f"Sending message: {message}")
