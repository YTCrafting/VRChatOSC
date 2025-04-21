from vrchatosc import VRChatOSC

def test_chatbox_typing():
    client = VRChatOSC()
    try:
        client.chatbox_typing(True)
        assert True
    except Exception as e:
        assert False, f"chatbox_typing -> {e}"
