import kivy
kivy.require('1.0.9')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty

class VideoWidget(Scatter):
    pass
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
    
class MixWidget(Scatter):
    pass
    
class SelectorWidget(Scatter):
    screen=ObjectProperty(None)
    mix=ObjectProperty(None)
    video=ObjectProperty(None)
    def set_screen(self):
        if(self.screen.active):
            MainApp().addscreen()
        else:
            MainApp().removescreen()
    def set_mix(self):        
        if(self.mix.active):
            MainApp().addmix()
        else:
            MainApp().removemix()
    def set_video(self):
        if(self.video.active):
            MainApp().addvideo()
        else:
            MainApp().removevideo()

class MainApp(App):
    def build(self):
        global root
        global screen
        global mix
        global video
        self.video=VideoWidget()
        video=self.video
        self.screen=ScreenWidget(size=(200,200))
        screen=self.screen
        self.mix=MixWidget(size=(200,200))
        mix=self.mix
        self.select = SelectorWidget(size=(300,500))
        root = self.root
        root.add_widget(self.select)
        return root
    def addscreen(self):
        root.add_widget(screen)
    def removescreen(self):
        root.remove_widget(screen)
    def addmix(self):
        root.add_widget(mix)
    def removemix(self):
        root.remove_widget(mix)
    def addvideo(self):
        root.add_widget(video)
    def removevideo(self):
        root.remove_widget(video)

if __name__ in ('__main__', '__android__'):
    MainApp().run()
