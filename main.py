import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty

class ScreenWidget(Scatter):
    def screen1_1(self):
        pass
    def screen1_2(self):
        pass
    def screen1_3(self):
        pass
    def screen1_4(self):
        pass
    def screen2_1(self):
        pass
    def screen2_2(self):
        pass
    def screen2_3(self):
        pass
    def screen2_4(self):
        pass
    def screen3_1(self):
        pass
    def screen3_2(self):
        pass
    def screen3_3(self):
        pass
    def screen3_4(self):
        pass
    def screen4_1(self):
        pass
    def screen4_2(self):
        pass
    def screen4_3(self):
        pass
    def screen4_4(self):
        pass
class SelectorWidget(Scatter):
    screen=ObjectProperty(None)
    screenon=False
    def set_screen(self):
        if(self.screen.active):
            MainApp().addscreen()
        else:
            MainApp().removescreen()
    def set_mix(self):
        print "click2"
    def set_video(self):
        print "click3"
class MainApp(App):
    def build(self):
        global root
        global screen
        self.screen=ScreenWidget()
        screen=self.screen
        self.select = SelectorWidget()
        root = self.root
        root.add_widget(self.select)
        return root
    def addscreen(self):
        root.add_widget(screen)
    def removescreen(self):
        root.remove_widget(screen)
if __name__ in ('__main__', '__android__'):
    MainApp().run()
