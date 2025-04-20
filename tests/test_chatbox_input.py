from vrchatosc import VRChatOSC

def test_chatbox_input():
    client = VRChatOSC()
    try:
        client.chatbox_input("Hello, World!")
        assert True
    except Exception as e:
        assert False, f"chatbox_input -> {e}"
