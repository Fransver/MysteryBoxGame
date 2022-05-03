from game.layer.HandenDectector import detectHandsLandmarks
from game.mysteryBox.arduino.SerialArduinoMocked import SerialArduinoMocked
import time

# ================ Attributen

arduino = SerialArduinoMocked()


def actionCountFingers(geheimeCodeStandaard, ingevoerdeCode):
    print("Test 1 keer code nummer " + str(geheimeCodeStandaard[0]))
    message = str(geheimeCodeStandaard[0])
    arduino.send_to_arduino(message)
    geheimeCodeStandaard.pop(0)  # Met pop haal ik de eerste index weer uit de lijst
    print(ingevoerdeCode)
    pass


def telActie(geheimeCodeStandaard, ingevoerdeCode):
    ingevoerdeCode.append(geheimeCodeStandaard.code[0])
    message = str(geheimeCodeStandaard.code[0])
    time.sleep(0.5)  # kort moment van input zodat er niet meteen achter elkaar gedrukt kan worden.
    arduino.send_to_arduino(message)
    print(ingevoerdeCode)
    geheimeCodeStandaard.code.pop(0)  # Met pop haal ik de eerste index weer uit de lijst

