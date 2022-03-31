import random

geheimeCode = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def geheimecodesrandom():
    code = random.sample(geheimeCode, 4)
    return code

def geheimecodetest():
    code = [4,5,3,2]
    return code

def lichtjeslijst():
    lichtjeEen = "#52, lichtje 1 aan"
    lichtjeTwee = "#53, lichtje 2 aan"
    lichtjeDrie = "#54, lichtje 3 aan"
    lichtjeVier = "#55, lichtje 4 aan"
    lichtjesLijst = [lichtjeEen, lichtjeTwee, lichtjeDrie, lichtjeVier]
    return lichtjesLijst
