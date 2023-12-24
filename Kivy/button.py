from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        button = Button(text = 'Print This', 
                        size_hint = (0.25, 0.1),
                        font_size = '20sp',
                        pos_hint = {'center_x':0.5, 'center_y':0.5},
                        on_press = self.printpress,
                        on_release = self.printrelease)
        return button

    def printpress(self, obj):
        print('\nButton pressed')

    def printrelease(self, obj):
        print('\nButton released')






MainApp().run( )