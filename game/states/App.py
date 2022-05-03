from game.states.StartingScreen import Window
from states.CameraGame import CameraGame


def main():
    game = CameraGame().game
    start_screen = Window(spel=game)
    start_screen.mainloop()


if __name__ == '__main__':
    main()
    quit()
