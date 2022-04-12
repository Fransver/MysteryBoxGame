from game.mysteryBox.arduino.SerialArduinoMocked import SerialArduinoMocked

#================================ Arduino Creëren

arduino = SerialArduinoMocked()

#================================ Gegeven code

gegevenCode = [2,4,3,1]
ingevoerdeCode = []

lichtjeEen = "#52, lichtje 1 aan"
lichtjeTwee = "#53, lichtje 2 aan"
lichtjeDrie = "#54, lichtje 3 aan"
lichtjeVier = "#55, lichtje 4 aan"
lichtjesLijst = [lichtjeEen, lichtjeTwee, lichtjeDrie, lichtjeVier]



if __name__ == '__main__':
    while True:
        print("Voer het 1e groene nummer in wat je op de camera ziet !!")
        messageInput = int(input())
        if messageInput == gegevenCode[0]:
            message = lichtjesLijst[0]
            arduino.send_to_arduino(message)


