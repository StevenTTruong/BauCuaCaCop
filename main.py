from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.image import Image as CoreImage
import random


class Dice(Widget):
    img_rect = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Select a random image and set it as the source of the Rectangle instruction
        self.img_source = self.images()
        self.img_rect = Rectangle(source=self.img_source, pos=self.pos, size=self.size, aspect_ratio=None)
        self.canvas.add(self.img_rect)

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        # Load original image size
        img = CoreImage(self.img_source)
        iw, ih = img.size
        ww, wh = self.size

        # Keep aspect ratio
        scale = min(ww / iw, wh / ih)
        new_w = iw * scale
        new_h = ih * scale

        # Center the image
        x = self.x + (ww - new_w) / 2
        y = self.y + (wh - new_h) / 2

        self.img_rect.pos = (x, y)
        self.img_rect.size = (new_w, new_h)

    def on_size(self, *args):
        # Update the size of the Rectangle instruction when the widget is resized
        self.img_rect.size = self.size

    def on_pos(self, *args):
        # Update the position of the Rectangle instruction when the widget is moved
        self.img_rect.pos = self.pos

    def images(self):
        rolls = ["./images/caDice.png", "./images/tomDice.png", "./images/cuaDice.png", "./images/gaDice.png", "./images/bauDice.png", "./images/deerDice.png"]
        return random.choice(rolls)
    
    def update_image(self):
        #update with new random image
        self.img_source = self.images()
        self.img_rect.source = self.img_source
        self.update_rect()
    
class DiceApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Draw a white background behind everything
        # with self.canvas.before:
        #     Color(1, 1, 1, 1)  # white
        #     self.bg = Rectangle(pos=self.pos, size=self.size)
        # self.bind(pos=self.update_bg, size=self.update_bg)

        # Add background image
        with self.canvas.before:
            self.bg_image = Rectangle(source="./images/background.jpg", pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg, size=self.update_bg)

        #Create a dice widget and a button widget
        self.dice = Dice()
        self.dice2 = Dice()
        self.dice3 = Dice()
        self.button = Button(text="Roll Dice!", size_hint=(None, None), size=(200, 50))

        #Bind the button to the Dice widget's update_image method
        self.button.bind(on_press=lambda x:self.dice.update_image())
        self.button.bind(on_press=lambda x:self.dice2.update_image())
        self.button.bind(on_press=lambda x:self.dice3.update_image())

        self.add_widget(self.dice)
        self.add_widget(self.dice2)
        self.add_widget(self.dice3)
        self.add_widget(self.button)
    
    def update_bg(self, *args):
        # Keep background scaled to window
        img = CoreImage("./images/background.jpg")
        iw, ih = img.size
        ww, wh = self.size

        # Keep aspect ratio
        scale = min(ww / iw, wh / ih)
        new_w = iw * scale
        new_h = ih * scale

        # Center background
        x = self.x + (ww - new_w) / 2
        y = self.y + (wh - new_h) / 2

        self.bg_image.pos = (x, y)
        self.bg_image.size = (new_w, new_h)

class BauCua(App):
    def build(self):
        return DiceApp(orientation='vertical', spacing = 10, padding=10) 
    
def main():
    BauCua().run()

if __name__ == "__main__":
    main()
