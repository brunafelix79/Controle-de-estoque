from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '200')


import pyodbc
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Function to display a message box
def show_message(title, message):
    popup_layout = BoxLayout(orientation='vertical')
    popup_layout.add_widget(Label(text=message))
    ok_button = Button(text='OK')
    popup_layout.add_widget(ok_button)
    popup = App.get_running_app().popup
    popup.content = popup_layout
    popup.title = title
    popup.open()

# Function to validate login in the database
def validar_login(nome, senha, confirmar_senha):
    try:
        # Database connection settings
        server = 'DESKTOP-4HA0FVH'
        database = 'controle_estoque'
        username = 'sa'
        password = '123456'

        # Connection string
        conn_str = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};'

        # Connecting to the database
        conn = pyodbc.connect(conn_str)

        # Creating a cursor
        cursor = conn.cursor()

        # Check if the username already exists
        query = "SELECT * FROM colaboradores WHERE nome = ?"
        cursor.execute(query, (nome,))
        if cursor.fetchone():
            show_message("Cadastro Failed", "Username already exists. Please choose a different username.")
        elif senha != confirmar_senha:
            show_message("Cadastro Failed", "Password and confirmation password do not match. Please try again.")
        else:
            # Executing SQL query to insert new user
            query = "INSERT INTO colaboradores(nome, senha) VALUES (?, ?)"
            cursor.execute(query, (nome, senha))
            conn.commit()
            show_message("Cadastro Successful", "Registration successful!")
            # Do whatever you need here after successful registration

        # Closing cursor and connection
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error connecting to the database:", e)

class CadastroApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Cadastrar novo usuário"))
        self.nome_input = TextInput(hint_text="Nome", font_size=12)
        self.senha_input = TextInput(hint_text="Senha", password=True, font_size=12)
        self.confirmar_senha_input = TextInput(hint_text="Confirmar Senha", password=True, font_size=12)
        layout.add_widget(self.nome_input)
        layout.add_widget(self.senha_input)
        layout.add_widget(self.confirmar_senha_input)
        botao = Button(text="Cadastrar")
        botao.bind(on_press=self.cadastrar)
        layout.add_widget(botao)
        return layout

    def cadastrar(self, instance):
        nome = self.nome_input.text
        senha = self.senha_input.text
        confirmar_senha = self.confirmar_senha_input.text
        validar_login(nome, senha, confirmar_senha)

if __name__ == '__main__':
    CadastroApp().run()
