from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

KV = '''
ScreenManager:
    HomeScreen:

<HomeScreen>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            id: status_label
            text: 'Initial Text'
        MDRaisedButton:
            text: 'Start Updating Every 10 Seconds'
            on_release: app.start_updating()
'''

class AnotherClass:
    def update_text(self):
        print("Updating text every 10 seconds")
        # Perform your logic to update the text
        return "Updated Text"

class HomeScreen(Screen):
    pass

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def start_updating(self):
        self.another_instance = AnotherClass()
        # Schedule the update function every 10 seconds
        Clock.schedule_interval(self.update_text_callback, 10)

    def update_text_callback(self, dt):
        updated_text = self.another_instance.update_text()
        # Update the text in the HomeScreen
        self.root.get_screen('home').ids.status_label.text = updated_text

if __name__ == '__main__':
    TestApp().run()