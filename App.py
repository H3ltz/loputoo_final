from Controller import Controller


class App:
    def __init__(self):
        app = Controller()
        app.view.mainloop()


if __name__ == "__main__": #Käivitamisel luuakse objekt App
    App()
