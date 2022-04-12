import game.commands.Codes
import keyboard
from arduino.SerialArduinoMocked import SerialArduinoMocked

# ================ Attributen

arduino = SerialArduinoMocked()
# ingevoerdeCode = None
# geheimeCodeStandaard = None
# ================

# ================================ Code
ingevoerdeCode = []
geheimeCodeStandaard = [2,3,4,1]




def actionCountFingers():
    print("Test 1 keer code nummer " + str(geheimeCodeStandaard[0]))
    message = str(geheimeCodeStandaard[0])
    arduino.send_to_arduino(message)
    geheimeCodeStandaard.pop(0)  # Met pop haal ik de eerste index weer uit de lijst
    print(ingevoerdeCode)
    pass
