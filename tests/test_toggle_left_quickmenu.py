from vrchatosc import VRChatOSC

def test_chatbox_typing():
    client = VRChatOSC()
    try:
        client.toggle_left_quickmenu()
        assert True
    except Exception as e:
        assert False, f"toggle_left_quickmenu -> {e}"
