# Pour future référence
# En utilisant powershell, lance ./venv/Scripts/activate, si ça se fait pas tout seul
# et écrit juste "deactivate" quand t'en as marre.
# tellement évident 4head
import pyautogui
from time import sleep
from twitchio.ext import commands
import Twitchkeys


class Manette():
    def __init__(self):
        self.keys = {"up": "z", "down": "s", "left": "q", "right": "d",
                     "a": "j", "b": "k", "l": "u", "r": "i", "start": "b", "select": "n"}

    def parseCommande(self, command):
        command = command.lower()
        print("parsing {}".format(command))
        if " " in command:
            return
        # No numbers
        if command in self.keys:
            pyautogui.keyDown(self.keys[command])
            pyautogui.keyUp(self.keys[command])
        # Number
        if command[:-1] in self.keys and command[-1:] in "123456789":
            for _ in range(int(command[-1:])):
                pyautogui.keyDown(self.keys[command])
                pyautogui.keyUp(self.keys[command])
                sleep(0.2)


testRun = Manette()

# Partie Twitch
bot = commands.Bot(
    irc_token=Twitchkeys.IRC_TOKEN,
    client_id=Twitchkeys.CLIENT_ID,
    nick=Twitchkeys.NICK,
    prefix=Twitchkeys.PREFIX,
    initial_channels=Twitchkeys.INITIAL_CHANNELS
)


@bot.event
async def event_ready():
    print("Bot OK")


@bot.event
async def event_message(ctx):
    print(ctx.content)
    testRun.parseCommande(ctx.content)
bot.run()

# while 1:
#    cmd = input(">>> ")
#    try:
#        testRun.parseCommande(cmd)
#    except:
#        print("Commande invalide.")
