import pytest
from unittest.mock import MagicMock
from openai.types import CompletionUsage
from openai.types.chat import ChatCompletion, ChatCompletionMessage
from openai.types.chat.chat_completion import Choice
from model_mixer.llm_clients.openai_client import OpenAIClient


@pytest.fixture
def openai_client():
    client = OpenAIClient(api_key='dummy_api_key')
    client.client = MagicMock()  # Mock the OpenAI client
    return client


def test_set_api_key(openai_client):
    new_api_key = 'new_api_key'
    openai_client.set_api_key(new_api_key)
    assert openai_client.api_key == new_api_key


def test_send_message(openai_client):
    message = "What can you do for me?"
    expected_response = ChatCompletion(id='chatcmpl-99AZORjRZ4Gqp5NEVQouTu5t7gVVT', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='As a language model AI, I can assist you with a wide range of tasks including answering questions, providing information, generating content, offering suggestions, and engaging in conversation on a variety of topics. If you have a specific request or need help with something, feel free to ask and I will do my best to assist you.', role='assistant', function_call=None, tool_calls=None))], created=1711972610, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3bc1b5746c', usage=CompletionUsage(completion_tokens=65, prompt_tokens=14, total_tokens=79))

    # Mock the chat completion response
    openai_client.client.chat.completions.create.return_value.choices = [
        MagicMock(message=MagicMock(content=expected_response))
    ]

    response = openai_client.send_message(message)
    assert response == expected_response
    openai_client.client.chat.completions.create.assert_called_once_with(
        messages=[{'role': 'user', 'content': message}],
        model="gpt-3.5-turbo"
    )
