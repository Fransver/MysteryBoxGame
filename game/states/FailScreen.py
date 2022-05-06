from game.states.StartingScreen import *


class FailScreen(Window):
    def __init__(self):
        super().__init__()
        self.title("fail fail fail")
        self.configure(background='red')

        # Labels
        self.fail_label = HomeLabel(self).update_tryagain()
        self.home_label.remove_home_label()


if __name__ == '__main__':
    fail_screen = FailScreen()
    fail_screen.mainloop()

