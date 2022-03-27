# serial_arduino class
#
# Handles serial communication with Arduino device on the Mystery Box.
#
# Note: messages are only sent to the Arduino if they are different from
# the previous message. This is a 'quick fix' for a bug where the same
# message is sent over and over again by the Hand Detector code.

import serial


class SerialArduino(object):
    def __init__(self, com_port):
        # initialize members.
        self.connection = serial.Serial(com_port)
        self.current_message = ""
        self.last_message = ""

        # set baudrate and open serial connection.
        self.connection.baudrate = 9600

    # public interface
    def send_to_arduino(self, message):
        self.current_message = message

        if self.message_is_new():
            self.write_to_arduino()

    # "private" methods (nothing is really private in Python).
    def message_is_new(self):
        if self.current_message != self.last_message:
            print("message_is_new: True")
            return True
        else:
            print("message_is_new: False")
            return False

    def write_to_arduino(self):
        message_in_bytes = bytes(self.current_message, 'utf-8')
        self.connection.write(message_in_bytes)
        print(f"Message \"{self.current_message}\" sent to Arduino!")
        self.last_message = self.current_message
