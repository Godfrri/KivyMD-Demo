from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import BooleanProperty

# Define KV language string
KV = '''
Screen:

   MDCheckbox:
      id: checkbox
      size_hint: None, None
      size: dp(48), dp(48)
      pos_hint: {'center_x': 0.5, 'center_y': 0.5}
      on_active: app.update_label(self.active)
   
   MDLabel:
      id: label
      text: 'Checkbox is inactive'
      halign: 'center'
      valign: 'center'
      pos_hint: {'center_x': 0.5, 'center_y': 0.3}        
'''
class TutorialsPointApp(MDApp):
   checkbox_active = BooleanProperty(False)    
   def build(self):
      # Load the KV language string
      self.root = Builder.load_string(KV)
      return self.root 
      
   def update_label(self, active):
      # Update the label text based on the checkbox state
      self.root.ids.label.text = 'Checkbox is ' + ('active' if active else 'inactive')
if __name__ == '__main__':
   TutorialsPointApp().run()