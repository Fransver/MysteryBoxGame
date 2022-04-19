from game.states.CameraGameStateMain import CameraGame
from game.states.CompleteWindow import *
from game.states.StartingScreen import *

game = CameraGame  # Game selecteren.


def main():
    window_start()  # Startscherm voor selecteren spel
    game()  # Aanroepen van de game
    window_complete()  # Scherm wat opkomt als het spel voltooid is


if __name__ == "__main__":
    main()
