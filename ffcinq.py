# Pour future référence
# En utilisant powershell, lance ./venv/Scripts/activate, si ça se fait pas tout seul
# et écrit juste "deactivate" quand t'en as marre.
# tellement évident 4head
import pyautogui
from time import sleep
from twitchio.ext import commands
import Twitchkeys


class Base:
    def __init__(self):
        # dicePos = Liste de tuples pour chaque dé.
        self.dicePos = {}
        self.atkPos = {}

    def generateDicePos(self, nbDices=12):
        # Générer les positions de 12 dés
        self.dicePos.clear()
        for x in range(nbDices):
            self.dicePos["d{}".format(
                x+1)] = ((895+((x % 6)*145), 955-(145*(x//6))))

    def generateAtkPos(self, nbAtk):
        # A moins de trouver une solution universelle,
        # faut hardcoder tout ça. ah well.
        pass

    def debugPosDes(self):
        for x in range(len(self.dicePos)):
            print("Dé {} = {}".format(x, self.dicePos[x]))
            pyautogui.moveTo(self.dicePos[x], duration=1)
            sleep(1)


class Warrior(Base):
    def __init__(self):
        # Le guerrier commence avec 2 dés
        super().__init__()
        self.generateDicePos()
        self.generateAtkPos(1)
        self.keys = {"up": "z", "down": "s", "left": "q", "right": "d",
                     "a": "j", "b": "k", "l": "u", "r": "i", "start": "b", "select": "n"}

    def parseCommande(self, command):
        print("parsing {}".format(command))
        arg = command.lower().split()
        if arg[0] == ("up"):
            # Je re je vais chercher ma souris
            pyautogui.keyDown("z")
            pyautogui.keyUp("z")
            return
        if arg[0] == ("down"):
            pyautogui.keyDown("s")
            pyautogui.keyUp("s")
            return
        if arg[0] == ("left"):
            pyautogui.keyDown("q")
            pyautogui.keyUp("q")
            return
        if arg[0] == ("right"):
            pyautogui.keyDown("d")
            pyautogui.keyUp("d")
            return
        if arg[0] == ("a"):
            pyautogui.keyDown("j")
            pyautogui.keyUp("j")
            return
        if arg[0] == ("b"):
            pyautogui.keyDown("k")
            pyautogui.keyUp("k")
            return
        if arg[0] == ("l"):
            pyautogui.keyDown("u")
            pyautogui.keyUp("u")
            return
        if arg[0] == ("r"):
            pyautogui.keyDown("i")
            pyautogui.keyUp("i")
            return
        if arg[0] == ("select"):
            pyautogui.keyDown("b")
            pyautogui.keyUp("b")
            return
        if arg[0] == ("start"):
            pyautogui.keyDown("n")
            pyautogui.keyUp("n")
            return


testRun = Warrior()

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
