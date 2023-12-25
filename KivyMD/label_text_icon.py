from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class DemoApp(MDApp):
    def build(self):
        label = MDLabel (text= 'Hello World', halign= 'center', 
                         theme_text_color= 'Custom', text_color= (0,1,1,1),
                         font_style = 'H2')

        label_icon = MDIcon(icon= 'language-python', pos_hint= {"center_x": .5, "center_y": .5})

        return label_icon

DemoApp().run()

