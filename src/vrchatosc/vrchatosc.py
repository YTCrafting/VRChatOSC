from pythonosc.udp_client import SimpleUDPClient
from typing import Union
import time

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

    def toggle_left_quickmenu(self) -> None:
        """Toggle the left VRChat quickmenu."""
        self.client.send_message("input/QuickMenuToggleLeft", 0)
        self.client.send_message("input/QuickMenuToggleLeft", 1)
        self.client.send_message("input/QuickMenuToggleLeft", 0)

    def toggle_right_quickmenu(self) -> None:
        """Toggle the right VRChat quickmenu."""
        self.client.send_message("input/QuickMenuToggleRight", 0)
        self.client.send_message("input/QuickMenuToggleRight", 1)
        self.client.send_message("input/QuickMenuToggleRight", 0)

    def move_forward(self, value:Union[bool,int]) -> None:
        """Moves the local VRChat player forwards.

        Args:
            value (bool or int, optional): Amount of seconds as integer or change forward walking state with bool.
        """
        if isinstance(value, bool):
            self.client.send_message("/input/MoveForward", value)
        elif isinstance(value, int):
            self.client.send_message("/input/MoveForward", True)
            time.sleep(value)
            self.client.send_message("/input/MoveForward", False)

    def move_backward(self, value:Union[bool,int]) -> None:
        """Moves the local VRChat player backwards.

        Args:
            value (bool or int, optional): Amount of seconds as integer or change backward walking state with bool.
        """
        if isinstance(value, bool):
            self.client.send_message("/input/MoveBackward", value)
        elif isinstance(value, int):
            self.client.send_message("/input/MoveBackward", True)
            time.sleep(value)
            self.client.send_message("/input/MoveBackward", False)

    def move_left(self, value:Union[bool,int]) -> None:
        """Moves the local VRChat player left.

        Args:
            value (bool or int): Amount of seconds as integer or change left walking state with bool.
        """
        if isinstance(value, bool):
            self.client.send_message("/input/MoveLeft", value)
        elif isinstance(value, int):
            self.client.send_message("/input/MoveLeft", True)
            time.sleep(value)
            self.client.send_message("/input/MoveLeft", False)

    def move_right(self, value:Union[bool,int]) -> None:
        """Moves the local VRChat player right.

        Args:
            value (bool or int): Amount of seconds as integer or change right walking state with bool.
        """
        if isinstance(value, bool):
            self.client.send_message("/input/MoveRight", value)
        elif isinstance(value, int):
            self.client.send_message("/input/MoveRight", True)
            time.sleep(value)
            self.client.send_message("/input/MoveRight", False)
