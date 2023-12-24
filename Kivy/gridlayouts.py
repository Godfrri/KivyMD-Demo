from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout


Window.clearcolor = (1,1,1,1)
Window.size = (360, 600)


class MainApp(App):
    def build(self):
        layout = GridLayout(cols = 2, row_force_default = True, row_default_height = 40)

        btn = Button(text = 'Button 1', size_hint = (None, None), width = 100, height = 40)
        btn2 = Button(text = 'Button 2')

        btn3 = Button(text = 'Button 3', size_hint = (None, None), width = 100, height = 40)
        btn4 = Button(text = 'Button 4')

        layout.add_widget(btn)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout


MainApp().run()