from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from datetime import datetime
import cv2
import numpy as np


class MyLayout(GridLayout):

    def tick(self, event):
        ret, frame = self.cap.read()
        frame = frame[::-1]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt="rgb")

        data = frame.tostring()
        texture.blit_buffer(data, bufferfmt="ubyte", colorfmt="rgb")
        self.image.texture = texture
        # print("tick")

    def take_photo(self, event):
        ret, image = self.cap.read()
        now = datetime.now()
        date_time = now.strftime("%Y_%m_%d__%H:%M:%S")
        print(date_time)
        cv2.imwrite("{}.png".format(date_time), image)


    def __init__(self):
        super(MyLayout, self).__init__()
        self.cap = cv2.VideoCapture(1)
        Clock.schedule_interval(self.tick, 1/30)

        self.rows = 1
        self.cols = 2

        self.image = Image()

        self.add_widget(self.image)
        self.click = Button(text="Take Photo")
        self.click.bind(on_press=self.take_photo)

        self.add_widget(self.click)




class MyApp(App):

    def build(self):
        return MyLayout()


app = MyApp()
app.run()


