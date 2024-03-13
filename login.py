from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '200')

import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10, 10, 10, 10]
        self.spacing = 10

        self.add_widget(Label(text="Fazer Login", font_size=24, font_name="Roboto"))
        self.nome_input = TextInput(hint_text="Nome", multiline=False, font_size=16, size_hint_y=None, height=dp(30), width=dp(200))
        self.add_widget(self.nome_input)
        self.senha_input = TextInput(hint_text="Senha", multiline=False, password=True, font_size=16, size_hint_y=None, height=dp(30), width=dp(200))
        self.add_widget(self.senha_input)

        # Layout horizontal para os botões
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50))
        self.add_widget(button_layout)

        self.login_button = Button(text="Login", size_hint=(None, None), size=(150, 50), font_size=16)
        self.login_button.bind(on_press=self.validar_login)
        button_layout.add_widget(self.login_button)

        self.cadastro_button = Button(text="Cadastro", size_hint=(None, None), size=(150, 50), font_size=16)
        self.cadastro_button.bind(on_press=self.abrir_cadastro)
        button_layout.add_widget(self.cadastro_button)

    def validar_login(self, instance):
        # Implemente a lógica de login aqui
        pass

    def abrir_cadastro(self, instance):
        os.system("python cadastro.py")

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
