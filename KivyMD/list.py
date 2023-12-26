from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):
    
    def build(self): 
        screen = Screen()

        list_view = MDList()
        scrool = ScrollView()

        item1 = OneLineListItem(text = 'Item 1', on_release = self.prinnnt)
        item2 = OneLineListItem(text = 'Item 2')

        list_view.add_widget(item1)
        list_view.add_widget(item2)

        scrool.add_widget(list_view)
        
        screen.add_widget(scrool)
        
        return screen

    def prinnnt(self, obj):
        print('Yupppppppppp')

DemoApp().run()