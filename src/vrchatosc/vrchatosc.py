from pythonosc.udp_client import SimpleUDPClient

class VRChatOSC:
    def __init__(self, ip:str="127.0.0.1", port:int=9000) -> None:
        """Connect to VRChat's OSC server.

        Args:
            ip (str, optional): Local IP address of the computer vrchat is running on. Defaults to "127.0.0.1".
            port (int, optional): VRChat's open OSC port. Defaults to 9000.
        """
        self.client = SimpleUDPClient(ip, port)

    def chatbox_input(self, text:str, immediate:bool=True, sound:bool=False) -> None:
        """Set the text displayed in VRChat's chatbox.

        Args:
            text (str): The text to be displayed, wich is limited to 144 characters.
            immediate (bool, optional): Wether the chatbox is immediately updated or the keyboard opens. Defaults to True.
            sound (bool, optional): Wether or not the notification SFX sound will be played. Defaults to False.
        """
        self.client.send_message("/chatbox/input", [text, immediate, sound])

    def chatbox_typing(self, typing:bool) -> None:
        """Set the state of the VRChat chatbox typing indicator.

        Args:
            typing (bool): Wether the typing indicator is on or off.
        """
        self.client.send_message("/chatbox/typing", typing)
