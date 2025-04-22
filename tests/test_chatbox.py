from vrchatosc import VRChatOSC

def test_chatbox_input():
    client = VRChatOSC()
    try:
        client.chatbox_input("Hello, World!")
        client.chatbox_input("")
        assert True
    except Exception as e:
        assert False

def test_chatbox_typing():
    client = VRChatOSC()
    try:
        client.chatbox_typing(True)
        client.chatbox_typing(False)
        assert True
    except Exception as e:
        assert False
