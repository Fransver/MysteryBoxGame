from game.gui.StartingScreen import Window


class CompleteScreen(Window):
    def __init__(self):
        super().__init__()

        self.geometry('800x600+50+50')
        self.title("You have won the game!!!")
        self.configure(background='green')


if __name__ == '__main__':
    complete_screen = CompleteScreen()
    complete_screen.mainloop()
