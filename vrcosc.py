from pythonosc.udp_client import SimpleUDPClient

class VrcOscClient:
    def __init__(self, ip:str="127.0.0.1", port:int=9000) -> None:
        self.client = SimpleUDPClient(ip, port)

    def chatbox_input(self, message:str, immidiate:bool=True, sfxsound:bool=False) -> None:
        self.client.send_message("/chatbox/input", [message, immidiate, sfxsound])

    def chatbox_typing(self, state:bool) -> None:
        if state:
            self.client.send_message("/chatbox/typing", 1)
        else:
            self.client.send_message("/chatbox/typing", 0)

    def avatar_parameter(self, parameter:str, value:any) -> None:
        if isinstance(value, bool):
            self.client.send_message(f"/avatar/parameters/{parameter}", int(value))
        elif isinstance(value, (int, float)):
            self.client.send_message(f"/avatar/parameters/{parameter}", value)
        else:
            raise ValueError("Unsupported value type. Must be bool, int or float.")

    def input_moveForward(self, state:bool) -> None:
        if state:
            self.client.send_message("/input/MoveForward", 1)
        else:
            self.client.send_message("/input/MoveForward", 0)

    def input_moveBackward(self, state:bool) -> None:
        if state:
            self.client.send_message("/input/MoveBackward", 1)
        else:
            self.client.send_message("/input/MoveBackward", 0)

    def input_moveLeft(self, state:bool) -> None:
        if state:
            self.client.send_message("/input/MoveLeft", 1)
        else:
            self.client.send_message("/input/MoveLeft", 0)

    def input_moveRight(self, state:bool) -> None:
        if state:
            self.client.send_message("/input/MoveRight", 1)
        else:
            self.client.send_message("/input/MoveRight", 0)

    def input_lookLeft(self, state:bool) -> None:
        if state:
            self.client.send_message("/input/LookLeft", 1)
        else:
            self.client.send_message("/input/LookLeft", 0)

    def input_lookRight(self, state:bool) -> None:
        if state:
            self.client.send_message("/input/LookRight", 1)
        else:
            self.client.send_message("/input/LookRight", 0)

    def input_jump(self, state:bool) -> None:
        if state:
            self.client.send_message("/input/Jump", 1)
        else:
            self.client.send_message("/input/Jump", 0)

    def input_run(self, state:bool) -> None:
        if state:
            self.client.send_message("/input/Run", 1)
        else:
            self.client.send_message("/input/Run", 0)
