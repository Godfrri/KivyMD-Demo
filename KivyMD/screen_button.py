from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


class DemoApp(MDApp):
    
    def build(self):
        screen = Screen()
        # btn_flat = MDFlatButton(text='Button1', 
        #                         pos_hint= {"center_x": .5, "center_y": .5})
        
        # btn_flat = MDRectangleFlatButton(text='Button2', 
        #                         pos_hint= {"center_x": .5, "center_y": .5})

        # btn_flat = MDIconButton(icon='android', 
        #                         pos_hint= {"center_x": .5, "center_y": .5})

        btn_flat = MDFloatingActionButton(icon='android', 
                                pos_hint= {"center_x": .5, "center_y": .5})
        
        screen.add_widget(btn_flat)

        return screen

DemoApp().run()