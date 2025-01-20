from pythonosc.udp_client import SimpleUDPClient

class VrcOscClient:
    def __init__(self, ip:str="127.0.0.1", port:int=9000) -> None:
        self.client = SimpleUDPClient(ip, port)

    def set_chatbox(self, message:str, immidiate:bool=True, sfxsound:bool=False) -> None:
        self.client.send_message("/chatbox/input", [message, immidiate, sfxsound])

    def set_typing_indicator(self, state:bool) -> None:
        if state:
            self.client.send_message("/chatbox/typing", 1)
        else:
            self.client.send_message("/chatbox/typing", 0)

    def set_avatar_parameter(self, parameter:str, value:any) -> None:
        if isinstance(value, bool):
            self.client.send_message(f"/avatar/parameters/{parameter}", int(value))
        elif isinstance(value, (int, float)):
            self.client.send_message(f"/avatar/parameters/{parameter}", value)
        else:
            raise ValueError("Unsupported value type. Must be bool, int or float.")
