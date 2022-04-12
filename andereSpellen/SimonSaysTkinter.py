from tkinter import *

class Application(Frame):

    # initialize app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.gameOn = False

    # create widgets in separate function
    def createWidgets(self):


        self.superFrame = Frame()
        self.redFrame = Frame(self.superFrame,
                              bg="red4",
                              width=200,
                              height=200)
        self.greenFrame = Frame(self.superFrame,
                              bg="green4",
                              width=200,
                              height=200)
        self.blueFrame = Frame(self.superFrame,
                              bg="blue4",
                              width=200,
                              height=200)
        self.yellowFrame = Frame(self.superFrame,
                              bg="yellow4",
                              width=200,
                              height=200)


        self.superFrame.pack()
        self.redFrame.grid(row=0, column=0)
        self.greenFrame.grid(row=0, column=1)
        self.blueFrame.grid(row=1, column=0)
        self.yellowFrame.grid(row=1, column=1)

# create instance, launch window
if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Simon Says...")
    root.mainloop()