from arduino.SerialArduinoMocked import SerialArduinoMocked

#================================ Arduino Creëren

arduino = SerialArduinoMocked()

#================================ Gegeven code

gegevenCode = [2,4,3,1]
ingevoerdeCode = []


if __name__ == '__main__':
    while True:
        print("Voer het 1e groene nummer in wat je op de camera ziet !!")
        messageInput = int(input())
        if messageInput == 2:
            message = "#52, lichtje 1 aan"
            arduino.send_to_arduino(message)
