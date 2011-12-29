import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty

class SelectorWidget(FloatLayout):
    def set_screen(self):
        print "click"
    def set_mix(self):
        print "click2"
    def set_video(self):
        print "click3"

class MainApp(App):

    def build(self):
        return SelectorWidget()

if __name__ in ('__main__', '__android__'):
    MainApp().run()
