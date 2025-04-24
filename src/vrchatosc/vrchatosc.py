from pythonosc.udp_client import SimpleUDPClient
from typing import Union
import time

class VRChatOSC:
    def __init__(self, ip:str="127.0.0.1", port:int=9000) -> None:
        """
        Initialize a connection to VRChat's OSC server.

        Establishes a UDP client to send OSC messages to a running VRChat instance.

        Args:
            ip (str, optional): IP address where VRChat is listening for OSC. Defaults to "127.0.0.1".
            port (int, optional): Port number for VRChat's OSC server. Defaults to 9000.
        """
        self.client = SimpleUDPClient(ip, port)

    def chatbox_input(self, text:str, immediate:bool=True, sound:bool=False) -> None:
        """
        Send text to VRChat's chatbox input field.

        This populates the chatbox with the given message, optionally opening the keyboard UI or playing the notification sound.

        Args:
            text (str): Message to display (max 144 characters).
            immediate (bool, optional): If True, updates the chatbox instantly; if False, opens the keyboard. Defaults to True.
            sound (bool, optional): If True, plays the notification SFX. Defaults to False.
        """
        self.client.send_message("/chatbox/input", [text, immediate, sound])

    def chatbox_typing(self, typing:bool) -> None:
        """
        Turn VRChat's chatbox typing indicator on or off.

        Args:
            typing (bool): True to show the typing indicator; False to hide it.
        """
        self.client.send_message("/chatbox/typing", typing)

    def toggle_left_quickmenu(self) -> None:
        """
        Toggle the left-side quick menu in VRChat.

        Simulates a quick press to open or close the left Quick Menu.
        """
        self.client.send_message("input/QuickMenuToggleLeft", True)
        time.sleep(0.01)
        self.client.send_message("input/QuickMenuToggleLeft", False)

    def toggle_right_quickmenu(self) -> None:
        """
        Toggle the right-side quick menu in VRChat.

        Simulates a quick press to open or close the right Quick Menu.
        """
        self.client.send_message("input/QuickMenuToggleRight", True)
        time.sleep(0.01)
        self.client.send_message("input/QuickMenuToggleRight", False)

    def move_forward(self, value:Union[bool,float]) -> None:
        """
        Move the local player forward.

        Can either press/release the forward input or move for a specified duration.

        Args:
            value (bool | float): If bool, True to start moving forward, False to stop. If float, moves forward for the given number of seconds.
        """
        if isinstance(value, bool):
            self.client.send_message("/input/MoveForward", value)
        elif isinstance(value, float):
            self.client.send_message("/input/MoveForward", True)
            time.sleep(value)
            self.client.send_message("/input/MoveForward", False)

    def move_backward(self, value:Union[bool,float]) -> None:
        """
        Move the local player backward.

        Can either press/release the backward input or move for a specified duration.

        Args:
            value (bool | float): If bool, True to start moving backward, False to stop. If float, moves backward for the given number of seconds.
        """
        if isinstance(value, bool):
            self.client.send_message("/input/MoveBackward", value)
        elif isinstance(value, float):
            self.client.send_message("/input/MoveBackward", True)
            time.sleep(value)
            self.client.send_message("/input/MoveBackward", False)

    def move_left(self, value:Union[bool,float]) -> None:
        """
        Strafe the local avatar to the left.

        Can either press/release the left input or move for a specified duration.

        Args:
            value (bool | float): If bool, True to start strafing left, False to stop. If float, strafes left for the given number of seconds.
        """
        if isinstance(value, bool):
            self.client.send_message("/input/MoveLeft", value)
        elif isinstance(value, float):
            self.client.send_message("/input/MoveLeft", True)
            time.sleep(value)
            self.client.send_message("/input/MoveLeft", False)

    def move_right(self, value:Union[bool,float]) -> None:
        """
        Strafe the local avatar to the right.

        Can either press/release the right input or move for a specified duration.

        Args:
            value (bool | float): If bool, True to start strafing right, False to stop. If float, strafes right for the given number of seconds.
        """
        if isinstance(value, bool):
            self.client.send_message("/input/MoveRight", value)
        elif isinstance(value, float):
            self.client.send_message("/input/MoveRight", True)
            time.sleep(value)
            self.client.send_message("/input/MoveRight", False)

    def jump(self) -> None:
        """
        Make the local player jump.

        Sends a quick press to the jump input; effective only if the world supports jumping.
        """
        self.client.send_message("/input/Jump", True)
        time.sleep(0.01)
        self.client.send_message("/input/Jump", False)

    def look_left(self, value:Union[bool,float]) -> None:
        """
        Rotate the local player to the left (counter-clockwise).

        Can either press/release the look-left input or turn over a specified duration.

        Args:
            value (bool | float): If bool, True to start turning left, False to stop. If float, turns left for the given number of seconds.
        """
        if isinstance(value, bool):
            self.client.send_message("/input/LookLeft", value)
        elif isinstance(value, float):
            self.client.send_message("/input/LookLeft", True)
            time.sleep(value)
            self.client.send_message("/input/LookLeft", False)

    def look_right(self, value:Union[bool,float]) -> None:
        """
        Rotate the local player to the right (clockwise).

        Can either press/release the look-right input or turn over a specified duration.

        Args:
            value (bool | float): If bool, True to start turning right, False to stop. If float, turns right for the given number of seconds.
        """
        if isinstance(value, bool):
            self.client.send_message("/input/LookRight", value)
        elif isinstance(value, float):
            self.client.send_message("/input/LookRight", True)
            time.sleep(value)
            self.client.send_message("/input/LookRight", False)

    def run(self, state:bool) -> None:
        """
        Toggle running mode for the local player.

        Args:
            state (bool): True to enable running, False to disable.
        """
        self.client.send_message("/input/Run", state)
