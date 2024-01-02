from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

KV = '''
ScreenManager:
    HomeScreen:

<HomeScreen>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        MDRaisedButton:
            text: 'Call Function from Another Class'
            on_release: app.call_function_from_another_class()
'''

class AnotherClass:
    def some_function(self):
        print("Function from AnotherClass is called!")

class HomeScreen(Screen):
    pass

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def call_function_from_another_class(self):
        # Create an instance of AnotherClass
        another_instance = AnotherClass()
        # Call the function from AnotherClass
        another_instance.some_function()

if __name__ == '__main__':
    TestApp().run()