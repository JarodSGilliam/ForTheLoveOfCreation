spotx = 0
spoty = 0
ground = [[0, 'I', 'I', 'I', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1 , 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
          [0, 0 , 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
          [0, 0 , 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
          [0, 1 , 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
          [0, 1 , 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
          [0, 0 , 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 3 , 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
          [0, 0 , 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
          [0, 1 , 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
          [0, 0 , 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
          [0, 0 , 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
          [0, 0 , 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def checkSpot(y, x):
    if ((x < 0) or (y < 0)):
        return False
    if ((x > len(ground)-1) or (y > len(ground[0])-1)):
        return False
    if (ground[x][y] == 1):
        return False
    return True

def paintGround(tile):
    if (tile == 0):
        return 'O '
    elif (tile == 1):
        return '  '
    elif (tile == 2):
        return '🔒'
    elif (tile == 3):
        return '🗝️ '
    else:
        return '? '

def getInventoryUI(inventory):
    inventoryText = '     '
    for i in range(5):
        inventoryText += '♡ '
    for i in range(len(ground[0])-13):
        inventoryText += '  '
    inventoryText += ' |'
    for a in inventory:
        inventoryText += a + ' '
    for i in range(12 - 2*len(inventory)):
        inventoryText += ' '
    inventoryText += '|'
    return inventoryText

def renderFrame(spotx, spoty):
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    for row in range(len(ground)):
        tempStr = ''
        for b in range(len(ground[row])):
            if ((row == spoty) and (b == spotx)):
                if (ground[row][b] == "I"):
                    tempStr += 'Y '
                    inventory.append('⛏️')
                    ground[row][b] = 0
                elif (ground[row][b] == 3):
                    tempStr += 'Y '
                    inventory.append('🗝️')
                    ground[row][b] = 0
                else:
                    tempStr += 'H '
            else:
                tempStr += paintGround(ground[row][b])
        print('     ' + tempStr)
    print(getInventoryUI(inventory))


inventory = []
userinput = ''
while (userinput != 'exit'):
    print()
    if ((userinput == "up") or (userinput == "w")):
        if (checkSpot(spotx, spoty-1)):
            spoty -= 1 
    elif ((userinput == "down") or (userinput == "s")):
        if (checkSpot(spotx, spoty+1)):
            spoty += 1
    elif ((userinput == "right") or (userinput == "d")):
        if (checkSpot(spotx+1, spoty)):
            spotx += 1
    elif ((userinput == "left") or (userinput == "a")):
        if (checkSpot(spotx-1, spoty)):
            spotx -= 1
    renderFrame(spotx, spoty)
    userinput = input()
