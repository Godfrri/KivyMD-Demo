from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.uix.button import *

# Example screen_helper
screen_helper = '''
BoxLayout:
    orientation: 'vertical'

    MDLabel:
        text: "Theme Changer Example"
        theme_text_color: "Primary"
        halign: 'center'

    MDRectangleFlatButton:
        text: "Toggle Dark/Light Theme"
        on_release: app.toggle_theme()
'''

class ThemeChangerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_string(screen_helper)

    def toggle_theme(self):
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
            self.theme_cls.primary_palette = 'BlueGray'
        else:
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'DeepOrange'

if __name__ == '__main__':
    ThemeChangerApp().run()