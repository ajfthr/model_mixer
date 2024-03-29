class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def set_api_key(self, api_key):
        self.api_key = api_key

    def send_message(self, model, message):
        print(f"Sending message to model {model}: {message}")