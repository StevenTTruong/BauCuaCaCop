from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random

class Dice(Widget):
    img_rect = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Select a random image and set it as the source of the Rectangle instruction
        img_source = self.images()
        self.img_rect = Rectangle(source=img_source, pos=self.pos, size=self.size, aspect_ratio=None)
        self.canvas.add(self.img_rect)

    def on_size(self, *args):
        # Update the size of the Rectangle instruction when the widget is resized
        self.img_rect.size = self.size

    def on_pos(self, *args):
        # Update the position of the Rectangle instruction when the widget is moved
        self.img_rect.pos = self.pos

    def images(self):
        rolls = ["./images/ca.png", "./images/tom.png", "./images/cua.png", "./images/ga.png", "./images/bau.png", "./images/deer.png"]
        return random.choice(rolls)
    
    def update_image(self):
        #update with new random image
        img_source = self.images()
        self.img_rect.source = img_source
    
class DiceApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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


class BauCua(App):
    def build(self):
        return DiceApp(orientation='vertical', spacing = 10, padding=10) 
    
def main():
    BauCua().run()

if __name__ == "__main__":
    main()
