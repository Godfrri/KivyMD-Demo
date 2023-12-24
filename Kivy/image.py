from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        # this is to load image locally
        img = Image(source = 'Image\CITYSCAPE1142023.png')

        # this is to load from URL
        # img = AsyncImage(source = 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg')

        return img

MainApp().run()