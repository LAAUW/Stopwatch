import time
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

from kivy.properties import NumericProperty


class StopwatchGrid(GridLayout):
    time_counter = NumericProperty(0)

    def tick(self, *_):
        self.time_counter += 1
    
    def updateTime(self, *args):
        pass

    def start(self):
        if not hasattr(self, "cb"):
            self.cb = Clock.schedule_interval(self.tick,1)
    
    def pause(self):
        if hasattr(self, "cb"):
            Clock.unschedule(self.cb)
            del self.cb
    
    def stop(self):
        self.time_counter = 0
        if hasattr(self, "cb"):
            del self.cb
    
class StopwatchApp(App):
    def build(self):
        return StopwatchGrid()

if __name__ == '__main__':
    StopwatchApp().run()