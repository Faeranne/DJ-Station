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
    screen1_1_text=StringProperty('Screen1')
    screen1_2_text=StringProperty('Screen1')
    screen1_3_text=StringProperty('Screen1')
    screen1_4_text=StringProperty('Screen1')
    screen2_1_text=StringProperty('Screen2')
    screen2_2_text=StringProperty('Screen2')
    screen2_3_text=StringProperty('Screen2')
    screen2_4_text=StringProperty('Screen2')
    screen3_1_text=StringProperty('Screen3')
    screen3_2_text=StringProperty('Screen3')
    screen3_3_text=StringProperty('Screen3')
    screen3_4_text=StringProperty('Screen3')
    screen4_1_text=StringProperty('Screen4')
    screen4_2_text=StringProperty('Screen4')
    screen4_3_text=StringProperty('Screen4')
    screen4_4_text=StringProperty('Screen4')
    def screen1_1(self):
        self.screen1_1_text='Active'
        self.screen1_2_text='Off'
        self.screen1_3_text='Off'
        self.screen1_4_text='Off'
    def screen1_2(self):
        self.screen1_2_text='Active'
        self.screen1_1_text='Off'
        self.screen1_3_text='Off'
        self.screen1_4_text='Off'
    def screen1_3(self):
        self.screen1_3_text='Active'
        self.screen1_1_text='Off'
        self.screen1_2_text='Off'
        self.screen1_4_text='Off'
    def screen1_4(self):
        self.screen1_4_text='Active'
        self.screen1_1_text='Off'
        self.screen1_3_text='Off'
        self.screen1_2_text='Off'
    def screen2_1(self):
        self.screen2_1_text='Active'
        self.screen2_2_text='Off'
        self.screen2_3_text='Off'
        self.screen2_4_text='Off'
    def screen2_2(self):
        self.screen2_2_text='Active'
        self.screen2_1_text='Off'
        self.screen2_3_text='Off'
        self.screen2_4_text='Off'
    def screen2_3(self):
        self.screen2_3_text='Active'
        self.screen2_1_text='Off'
        self.screen2_2_text='Off'
        self.screen2_4_text='Off'
    def screen2_4(self):
        self.screen2_4_text='Active'
        self.screen2_1_text='Off'
        self.screen2_3_text='Off'
        self.screen2_2_text='Off'
    def screen3_1(self):
        self.screen3_1_text='Active'
        self.screen3_2_text='Off'
        self.screen3_3_text='Off'
        self.screen3_4_text='Off'
    def screen3_2(self):
        self.screen3_2_text='Active'
        self.screen3_1_text='Off'
        self.screen3_3_text='Off'
        self.screen3_4_text='Off'
    def screen3_3(self):
        self.screen3_3_text='Active'
        self.screen3_1_text='Off'
        self.screen3_2_text='Off'
        self.screen3_4_text='Off'
    def screen3_4(self):
        self.screen3_4_text='Active'
        self.screen3_1_text='Off'
        self.screen3_3_text='Off'
        self.screen3_2_text='Off'
    def screen4_1(self):
        self.screen4_1_text='Active'
        self.screen4_2_text='Off'
        self.screen4_3_text='Off'
        self.screen4_4_text='Off'
    def screen4_2(self):
        self.screen4_2_text='Active'
        self.screen4_1_text='Off'
        self.screen4_3_text='Off'
        self.screen4_4_text='Off'
    def screen4_3(self):
        self.screen4_3_text='Active'
        self.screen4_1_text='Off'
        self.screen4_2_text='Off'
        self.screen4_4_text='Off'
    def screen4_4(self):
        self.screen4_4_text='Active'
        self.screen4_1_text='Off'
        self.screen4_3_text='Off'
        self.screen4_2_text='Off'
    
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
