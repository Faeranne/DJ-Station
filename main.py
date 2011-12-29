import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.image import Image

class ScreenWidget(Scatter):
    def ScreenWidget(self):
        lay = FloatLayout(size=(200,200))
        image = Image(source='data/logo/kivy-icon-512.png', size_hint=(.6,.6), pos_hint={'x':.5,'y':.5})
        lay.add_widget(image)
        lay.add_widget(exit)
        self.add_widget(lay)
        return lay

class MainApp(App):
    def screens(self, instance):
        if instance.state=="down":
            self.layout.add_widget(self.scat)
        else:
            self.layout.remove_widget(self.scat)
        
    def build(self):
        s = Scatter(do_rotation=False)
        screen = ToggleButton(text='Screens')
        screen.bind(on_press=self.screens)
        s.add_widget(screen)
        self.layout = FloatLayout(size=(800,600))
        self.layout.add_widget(s)
        self.scat = ScreenWidget()
        return self.layout

if __name__ in ('__main__', '__android__'):
    MainApp().run()
