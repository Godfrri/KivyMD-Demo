from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage


Window.clearcolor = (1,1,1,1)
Window.size = (360, 600)


class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation= 'vertical', spacing = 10, padding = 40)
        
        # btn = Button(text = 'Button 1')
        # btn2 = Button(text = 'Button 2')
        # layout.add_widget(btn)
        # layout.add_widget(btn2)

        img = Image(source = 'Image\CITYSCAPE1142023.png')
        btn3 = Button(text = 'Login',
                      size_hint = (None, None), width = 100, height = 35,
                      pos_hint = {'center_x': 0.5})
        layout.add_widget(img)
        layout.add_widget(btn3)

        return layout


MainApp().run()