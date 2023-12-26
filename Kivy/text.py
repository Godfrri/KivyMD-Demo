from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)

class MainApp(App):
    def build(self):
        label = Label(text = 'This is Batman.', 
                      font_size = '20sp', 
                      bold = True, 
                      color =(0,0,0,1),
                      italic = True)
        return label

MainApp().run()