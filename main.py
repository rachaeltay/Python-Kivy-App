from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


# instantiate object and run (can only start kivy on virtualenv or windows)
TheLabApp().run()