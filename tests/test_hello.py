import hello
import pytest


@pytest.mark.parametrize("language, message", [["English", "Hello World"], ["日本語", "ハローワールド"]])
def test_message(language, message):
    assert hello.get_message(language) == message