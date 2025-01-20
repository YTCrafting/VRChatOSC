import vrcosc
import time

# create a vrchat osc client
client = vrcosc.VrcOscClient("192.168.178.178", 9000)
# the ip address and port are optional because they default to 127.0.0.1:9000
# however its recommended to enter your pc's local ip address to prevent other bugs that may occurr.
# to get your pc's local ip address in your network you'll need to go into command prompt.
# in there type "ipconfig" and it should list you your network adapters.
# then look for the IPv4 address under the correct adapter that has a readable dns suffix such as fritz.box

# show "Hello, World!" in the vrchat chatbox
client.set_chatbox("Hello, World!")
# optionally you can add immidiate wich is default true and/or sfxsound wich is false by default.
# immidiate sends the message immidiantly without opening the keyboard input in vrchat.
# sfxsound specifies wether or not a sound should be played once the chatbox is updated.
# its recommended to keep sfxsound on false if youre updating your chatbox frequently.

# enable the chatbox typing indicator
client.set_typing_indicator(True)
# i hope this is self explainatory but if you dont know,
# the typing indicator are the 3 dots that appear when you write a chatbox message.
# this sets the typing indicator to either on or off.
