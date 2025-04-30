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

def test_look_left():
    client = VRChatOSC()
    try:
        client.look_left(True)
        client.look_left(False)
        client.look_left(1)
        assert True
    except Exception as e:
        assert False

def test_look_right():
    client = VRChatOSC()
    try:
        client.look_right(True)
        client.look_right(False)
        client.look_right(1)
        assert True
    except Exception as e:
        assert False

def test_run():
    client = VRChatOSC()
    try:
        client.run(True)
        client.run(False)
        assert True
    except Exception as e:
        assert False

def test_comfort_turn_left():
    client = VRChatOSC()
    try:
        client.comfort_turn_left()
        assert True
    except Exception as e:
        assert False

def test_comfort_turn_right():
    client = VRChatOSC()
    try:
        client.comfort_turn_right()
        assert True
    except Exception as e:
        assert False
