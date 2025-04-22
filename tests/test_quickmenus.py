from vrchatosc import VRChatOSC

def test_left_quickmenu():
    client = VRChatOSC()
    try:
        client.toggle_left_quickmenu()
        client.toggle_left_quickmenu()
        assert True
    except Exception as e:
        assert False

def test_right_quickmenu():
    client = VRChatOSC()
    try:
        client.toggle_right_quickmenu()
        client.toggle_right_quickmenu()
        assert True
    except Exception as e:
        assert False
