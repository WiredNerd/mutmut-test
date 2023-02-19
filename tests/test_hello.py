import hello


def test_message_english():
    assert hello.get_message("English") == "Hello World"