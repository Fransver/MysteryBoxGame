from game.states.CameraGameStateMain import CameraGame
from game.states.CompleteWindow import *
from game.states.StartingScreen import *

game = CameraGame  # Game selecteren.
window_start = Window()


def main():
    window_start.mainloop()
    game()  # Aanroepen van de game
    window_complete()  # Scherm wat opkomt als het spel voltooid is


if __name__ == "__main__":
    main()
