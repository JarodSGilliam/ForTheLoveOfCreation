
renderMap = {
     0 : '🟩',
     1 : '🟦',
     2 : '🔥',
     3 : '🧯',
    '?': '❓',
    'h': '❤️',
    'I': '✨',
}

class frame():
    
    map = None
    health = ""
    

    def Frame(self):
        print()
    
    def paintBackground(self, Map) -> None:
        self.map = []
        for i in range(len(Map)):
            self.map.append([])
            for a in Map[i]:
                self.map[i].append(renderMap[a])
    
    def getRepersentation(tile):
        if (tile == 0):
            return '🟩'
        elif (tile == 1):
            return '🟦'
        elif (tile == 2):
            return '🔥'
        elif (tile == 3):
            return '🧯'
        else:
            return '❓'

    def paintHero(self, hero) -> None:
        spot = hero.spot
        self.map[spot[1]][spot[0]] = hero.icon
    
    def paintHealth(self, health) -> None:
        self.health = '|'
        for i in range(health['health']):
            self.health += renderMap['h'] + ' '
        for i in range(health['max health']-health['health']):
            self.health += '  '
        self.health += '|'
    
    def print(self, debug: bool = False):
        if not debug:
            print(chr(27)+'[2j')
            print('\033c')
            print('\x1bc')
        print()
        self.__printMap()
        self.__printUI()
    
    def __printMap(self):
        if (self.map == None):
            return
        for row in range(len(self.map)):
            print('     ', end ="")
            output = ""
            for b in range(len(self.map[row])):
                print(self.map[row][b], end ="")
            print()

    def __printUI(self):
        inventory = []
        inventoryText = '     '
        inventoryText += self.health
        for i in range(5-len(self.health)):
            inventoryText += '  '
        for i in range(16-14):
            inventoryText += '  '
        inventoryText += ' |'
        for a in inventory:
            inventoryText += a + ' '
        for i in range(12 - 2*len(inventory)):
            inventoryText += ' '
        inventoryText += '|'
        print(inventoryText)

