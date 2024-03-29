import pytest
from model_mixer.message_facade import MessageFacade


@pytest.fixture
def message_facade():
    # Setup code before each test method
    facade = MessageFacade(None, "gpt-3")
    yield facade
    # Teardown code after each test method (if necessary)


def test_send_message(message_facade):
    message_facade.provider = 'openai'
    # Assuming there's a way to verify the message was sent or received,
    # which might involve mocking the OpenAIClient.
    message_facade.send_message('test message')


def test_send_message_without_message(message_facade):
    message_facade.provider = 'openai'
    with pytest.raises(ValueError):
        message_facade.send_message(None)


def test_send_empty_message(message_facade):
    message_facade.provider = 'openai'
    with pytest.raises(ValueError):
        message_facade.send_message('')


def test_send_message_with_openai_provider(message_facade):
    message_facade.provider = 'openai'
    # As above, assuming verification of message sending/receiving.
    message_facade.send_message('test message')
