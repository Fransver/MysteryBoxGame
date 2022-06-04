from mysteryBox.SerialArduino import SerialArduino


class SerialArduinoMocked(SerialArduino):
    def __init__(self):
        self.current_message = ""
        self.last_message = ""

    def write_to_arduino(self):  # override
        print(f"Message \"{self.current_message}\" sent to Arduino!")
        self.last_message = self.current_message
