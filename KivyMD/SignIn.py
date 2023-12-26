from kivymd.app import MDApp
from kivymd.uix.screen import Screen
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog


from helper import username_helper




class DemoApp(MDApp):
    
    def build(self): 

        screen = Screen()
        self.theme_cls.primary_palette = 'Green'

        # username = MDTextField(text = 'Enter username',
        #                        pos_hint= {"center_x": .5, "center_y": .5},
        #                        size_hint_x = None, width = 300)

        self.username = Builder.load_string(username_helper)


        btn = MDRectangleFlatButton(text = 'Show',
                                    pos_hint= {"center_x": .5, "center_y": .4},
                                    on_release = self.signIn)
        
        screen.add_widget(self.username)
        screen.add_widget(btn)

        return screen


    def signIn(self, obj):
        if self.username.text == '':
            message = 'Please Enter username'
        else:
            message = self.username.text + ' does not exist'
        
        close_btn = MDFlatButton(text = 'Close',
                                 on_release = self.closeDialog)
        
        self.dialog = MDDialog(title = 'Username Check',
                          text = message,
                          size_hint = (0.7, 1),
                          buttons = [close_btn])
        
        self.dialog.open()
        # print(self.username.text)

    
    def closeDialog(self, obj):
        self.dialog.dismiss()


DemoApp().run()