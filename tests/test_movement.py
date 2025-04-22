from vrchatosc import VRChatOSC

def test_move_forward():
    client = VRChatOSC()
    try:
        client.move_forward(True)
        client.move_forward(False)
        client.move_forward(1)
        assert True
    except Exception as e:
        assert False

def test_move_backward():
    client = VRChatOSC()
    try:
        client.move_backward(True)
        client.move_backward(False)
        client.move_backward(1)
        assert True
    except Exception as e:
        assert False

def test_move_left():
    client = VRChatOSC()
    try:
        client.move_left(True)
        client.move_left(False)
        client.move_left(1)
        assert True
    except Exception as e:
        assert False

def test_move_right():
    client = VRChatOSC()
    try:
        client.move_right(True)
        client.move_right(False)
        client.move_right(1)
        assert True
    except Exception as e:
        assert False

def test_jump():
    client = VRChatOSC()
    try:
        client.jump()
        assert True
    except Exception as e:
        assert False
