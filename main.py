from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock

screen_stack = []

stack = list()

class AppOpen(Screen):
    def on_enter(self, *args):
        if self.manager.current != 'HomeScreen':
            Clock.schedule_once(self.callback, 3)

    def callback(self, dt):
        self.manager.current = 'HomeScreen'
        screen_stack.append(self.manager.current)


class Home(Screen):
    pass


class Register(Screen):
    def check_credentials(self):
        print(self.register_name.text)
        print(self.register_phone.text)
        print(self.register_username.text)
        print(self.register_password.text)
    def prev_screen(self):
        self.manager.current = list(set(screen_stack)).pop()
        self.manager.transition.direction = 'right'


class Login(Screen):
    def check_login(self):
        pass
    def prev_screen(self):
        self.manager.current = list(set(screen_stack)).pop()
        self.manager.transition.direction = 'right'


class Map(Screen):
    pass


class WelcomeScreen(Screen):
    pass


class Dashboard(Screen):
    pass


class RakshakApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'BlueGray'
        screen = Screen()
        layout = Builder.load_file('rakshak.kv')
        screen.add_widget(layout)
        return screen


if __name__ == '__main__':
    Window.size = (300, 500)
    sm = ScreenManager()
    sm.add_widget(AppOpen(name='AppOpenScreen'))
    sm.add_widget(Home(name='HomeScreen'))
    RakshakApp().run()