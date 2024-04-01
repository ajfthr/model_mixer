import os
from openai import OpenAI


class OpenAIClient:

    def __init__(self, api_key):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)

    def set_api_key(self, api_key):
        self.api_key = api_key

    def send_message(self, message, model="gpt-3.5-turbo") -> str:
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model=model,
        )

        return chat_completion.choices[0].message.content
