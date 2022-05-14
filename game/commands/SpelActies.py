from game.mysteryBox.arduino.SerialArduinoMocked import SerialArduinoMocked
import time

# ================ Attributes

arduino = SerialArduinoMocked()


def action_count_fingers(geheimeCodeStandaard, ingevoerdeCode):
    print("Test 1 keer code nummer " + str(geheimeCodeStandaard[0]))
    message = str(geheimeCodeStandaard[0])
    arduino.send_to_arduino(message)
    geheimeCodeStandaard.pop(0)  # Met pop haal ik de eerste index weer uit de lijst
    print(ingevoerdeCode)
    pass


def count_action(geheimeCodeStandaard, ingevoerdeCode):
    ingevoerdeCode.append(geheimeCodeStandaard.code[0])
    message = str(geheimeCodeStandaard.code[0])
    time.sleep(0.5)  # kort moment van input zodat er niet meteen achter elkaar gedrukt kan worden.
    arduino.send_to_arduino(message)
    print(ingevoerdeCode)
    geheimeCodeStandaard.code.pop(0)  # Met pop haal ik de eerste index weer uit de lijst

