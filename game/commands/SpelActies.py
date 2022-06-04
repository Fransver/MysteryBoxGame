from mysteryBox.SerialArduinoMocked import SerialArduinoMocked
import time

# ================ Attributes

arduino = SerialArduinoMocked()


def action_count_fingers(geheime_code_standaard, ingevoerde_code):
    print("Test 1 keer code nummer " + str(geheime_code_standaard[0]))
    message = str(geheime_code_standaard[0])
    arduino.send_to_arduino(message)
    geheime_code_standaard.pop(0)  # Met pop haal ik de eerste index weer uit de lijst
    print(ingevoerde_code)
    pass


def count_action(geheime_code_standaard, ingevoerde_code):
    ingevoerde_code.append(geheime_code_standaard.code[0])
    message = str(geheime_code_standaard.code[0])
    time.sleep(0.5)  # kort moment van input zodat er niet meteen achter elkaar gedrukt kan worden.
    arduino.send_to_arduino(message)
    print(ingevoerde_code)
    geheime_code_standaard.code.pop(0)  # Met pop haal ik de eerste index weer uit de lijst

