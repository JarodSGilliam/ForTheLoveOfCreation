import RenderEngine as Renderer
# import Frame
import Maps
import time
import threading
import msvcrt


class Directions():
    LEFT = [-1, 0, 0]
    RIGHT = [1, 0, 0]
    UP = [0, -1, 0]
    DOWN = [0, 1, 0]
    BACK = [0, 0, -1]
    FORWARD = [0, 0, 1]
    STILL = [0, 0, 0]
    template = ["x", "y", "z"] # could add ', "t"'

    def displace(spot, direction):
        if (direction == None):
            direction = Directions.STILL
        output = []
        if (direction != None):
            for i in range(len(spot)):
                output.append(spot[i] + direction[i])
        return output


class Character():
    def __init__(self, spot, cClass):
        self.spot = spot
        self.cClass = cClass
        if cClass == "hero":
            self.icon = "🦸"
            self.health = 5
    
    def move(self, direction):
        self.spot = Directions.displace(self.spot, direction)
    
    def getSpot(self):
        return self.spot
    

    def Health(self):
        return {
            "health" : self.health,
            "max health" : self.__getMaxHealth()
        }

    def __getMaxHealth(self):
        if (self.cClass == "hero"):
            return 5
        if (self.cClass == "crazy"):
            return 1
        return None

# def move(hero, userinput):
#     if (checkSpot(hero.x, hero.y-1, ground)):
#         hero.y -= 1 
#     if (checkSpot(hero.x, hero.y+1), ground):
#         hero.y += 1
#     if (checkSpot(hero.x+1, hero.y), ground):
#         hero.x += 1
#     if (checkSpot(hero.x-1, hero.y), ground):
#         hero.x -= 1
#     return hero

def checkSpot(spot, ground):
    print(spot)
    if ((spot[0] < 0) or (spot[1] < 0)):
        return False
    if ((spot[0] > len(ground)-1) or (spot[1] > len(ground[0])-1)):
        return False
    if (ground[spot[1]][spot[0]] == 1):
        return False
    return True


def pickupItemAt(hero):
    spotsValue = ground[hero.spot[1]][hero.spot[0]]
    output = None
    if (spotsValue == "I"):
        spotsValue = 0
        output = '⛏️'
    elif (spotsValue == 3):
        spotsValue = 0
        output = '🗝️'
    ground[hero.spot[1]][hero.spot[0]] = spotsValue
    return output


def parseControls(input):
    if ((userinput == "up") or (userinput == b"w")):
        return Directions.UP
    elif ((userinput == "down") or (userinput == b"s")):
        return Directions.DOWN
    elif ((userinput == "right") or (userinput == b"d")):
        return Directions.RIGHT
    elif ((userinput == "left") or (userinput == b"a")):
        return Directions.LEFT
    elif (userinput == b"e"):
        return Directions.STILL






hero = Character([0, 0], "hero")
ground = Maps.getMap(1)
inventory = []
userinput = None




def update():
    createFrame()


frameStack = []
def createFrame():
    frame = Renderer.frame()
    frame.paintBackground(ground)
    frame.paintHero(hero)
    frame.paintHealth(hero.Health())
    # frame.paintInventory(hero.inventory)
    frameStack.append(frame)

class renderThread(threading.Thread):
    running = True
    
    def __init__(self) -> None:
        threading.Thread.__init__(self)
        self.currentFrame = createFrame()
    
    def run(self):
        while(self.running):
            if (len(frameStack) > 0):
                currentFrame = frameStack.pop(0)
                currentFrame.print(True)
            # while (len(frameStack) == 0):
            #     time.sleep(0.1)


    def stop(self):
        self.running = False



createFrame()
renderingThread = renderThread()
renderingThread.start()


while (userinput != 'exit'):
    # movement = parseControls(userinput)
    # print ('Press s or n to continue:\n')
    movement = parseControls(msvcrt.getch())
    if (movement == Directions.STILL):
        userinput = 'exit'
        exit()
    # print(input_char.upper())
    # if input_char.upper() == b'S':
    #     print ('YES')
    if (checkSpot(Directions.displace(hero.spot, movement), ground)):
        hero.move(movement)
        update()
    # hero = move(hero, userinput)
    item = pickupItemAt(hero)
    if (item != None):
        inventory.append(item)
        update()
        # hero.icon = Renderer.getSymbol("foundItem")
    else:
        hero.icon = "🦸"
    # Renderer.renderFrame(ground, hero, inventory)
    # Renderer.renderUI(hero.health, hero.expectedHealth(), inventory, len(ground[0]))
    # userinput = input()
renderingThread.stop()
exit()
