m1 = [[0, 'I', 'I', 'I', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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


def getMap(id):
    if (id == 1):
        return m1
    return -1

def updateMap(id, update):
    if (id == 1):
        m1 = update
        return
    return -1
