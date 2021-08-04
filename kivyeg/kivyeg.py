from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class MyLayout(GridLayout):

    def set_value(self, event):
        if not event.text:
            self.steps += 1
            event.text = self.player
            if self.player == "O":
                self.player = "X"
            else:
                self.player = "O"

        if self.steps == 9:
            self.steps = 0
            self.make_board()


    def make_board(self):
        self.board = []
        for row in range(3):
            line = []
            for col in range(3):
                button = Button(text='')
                button.bind(on_press=self.set_value)
                line.append(button)
                self.add_widget(button)
            self.board.append(line)

    def __init__(self):
        super(MyLayout, self).__init__()
        self.steps = 0
        self.player = "O"
        self.rows = 3
        self.cols = 3

        self.make_board()



class MyApp(App):

    def build(self):
        return MyLayout()


app = MyApp()
app.run()
