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
    
    def generateDicePos(self, nbDices = 12):
        # Générer les positions de 12 dés
        self.dicePos.clear()
        for x in range(nbDices):
            self.dicePos["d{}".format(x+1)] = ((895+((x%6)*145), 955-(145*(x//6))))
    
    def generateAtkPos(self, nbAtk):
        # A moins de trouver une solution universelle,
        # faut hardcoder tout ça. ah well.
        # self.atkPos.append((290+(()),685)
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
        self.generateAtkPos(1) # Par défaut
    
    def generateAtkPos(self, nbCols):
        # Le warrior a le reroll.
        # Ecran: 1920x1080, avec la barre des tâches à gauche
        self.atkPos.clear()
        if(nbCols == 1):
            self.atkPos["atk1"] = (750, 385) # Col 1
            self.atkPos["atk2"] = (750, 670)
            self.atkPos["reroll"] = (1220, 550) # Reroll
        if(nbCols == 2):
            self.atkPos["atk1"] = (520, 385) # Col 1
            self.atkPos["atk2"] = (520, 670) 
            self.atkPos["atk3"] = (990, 385) # Col 2
            self.atkPos["atk4"] = (990, 670) 
            self.atkPos["reroll"] = (1450, 550) # Reroll
        if(nbCols == 3):
            self.atkPos["atk1"] = (290, 385) # Col 1
            self.atkPos["atk2"] = (290, 670)  
            self.atkPos["atk3"] = (750, 385) # Col 2
            self.atkPos["atk4"] = (750, 670)  
            self.atkPos["atk5"] = (1210, 385) # Col 3
            self.atkPos["atk6"] = (1210, 670) 
            self.atkPos["reroll"] = (1680, 550) # Reroll 
        self.atkPos["limitbreak"] = (565, 980) # Limitbreak
        self.atkPos["endturn"] = (1800, 950) # End turn
    
    def parseCommande(self, command):
        print("parsing {}".format(command))
        # Commande de la forme:
        # d[x] atk[y]   |   ex: d4 atk1
        arg = command.lower().split()
        if arg[0].startswith("setcol"):
            self.generateAtkPos(int(arg[1]))
            return
        if arg[0].startswith("setcol"):
            self.generateAtkPos(int(arg[1]))
            return
        if arg[0] == "limitbreak":
            pyautogui.moveTo(self.atkPos["limitbreak"], duration=0.2)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            return
        if arg[0] == "endturn":
            pyautogui.moveTo(self.atkPos["endturn"], duration=0.2)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            return
        pyautogui.moveTo(self.dicePos[arg[0]])
        pyautogui.dragTo(self.atkPos[arg[1]], duration=0.2)

testRun = Warrior()

# Partie Twitch
bot = commands.Bot(
    irc_token = Twitchkeys.IRC_TOKEN,
    client_id = Twitchkeys.CLIENT_ID,
    nick = Twitchkeys.NICK,
    prefix = Twitchkeys.PREFIX,
    initial_channels = Twitchkeys.INITIAL_CHANNELS
)

@bot.event
async def event_ready():
    print("Bot OK")

@bot.event
async def event_message(ctx):
    print(ctx.content)
    testRun.parseCommande(ctx.content)
bot.run()

#while 1:
#    cmd = input(">>> ")
#    try:
#        testRun.parseCommande(cmd)
#    except:
#        print("Commande invalide.")