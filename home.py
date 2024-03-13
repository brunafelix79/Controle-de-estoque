from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from datetime import datetime


class Produto:
    def __init__(self, codigo_barra, nome, data_compra, validade, quantidade, preco, categoria, descricao, preco_compra, fornecedor, unidade_medida, imagem, observacoes):
        self.codigo_barra = codigo_barra
        self.nome = nome
        self.data_compra = data_compra
        self.validade = validade
        self.quantidade = quantidade
        self.preco = preco
        self.categoria = categoria
        self.descricao = descricao
        self.preco_compra = preco_compra
        self.fornecedor = fornecedor
        self.unidade_medida = unidade_medida
        self.imagem = imagem
        self.observacoes = observacoes

    def dias_para_validade(self):
        hoje = datetime.now().date()
        return (self.validade - hoje).days


class SistemaCadastro:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def produtos_proximos_validade(self):
        hoje = datetime.now().date()
        produtos_proximos = []
        for produto in self.produtos:
            if produto.validade >= hoje and produto.dias_para_validade() <= 30:
                produtos_proximos.append(produto)
        return produtos_proximos


class DateInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if len(self.text) == 10:
            return
        if not substring.isdigit():
            return
        if len(self.text) in [2, 5]:
            self.text += '/'
        super(DateInput, self).insert_text(substring, from_undo=from_undo)


class GUI(BoxLayout):
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.sistema = SistemaCadastro()

        self.frame_cadastro = GridLayout(cols=2, spacing=7, padding=7)
        self.add_widget(self.frame_cadastro)

        # Criação dos campos de entrada
        self.codigo_barra_entry = TextInput(height=30, font_size=16, size_hint_y=None, input_filter='int')
        self.frame_cadastro.add_widget(Label(text="Código de Barras:", font_size=16))
        self.frame_cadastro.add_widget(self.codigo_barra_entry)

        self.nome_entry = TextInput(height=30, font_size=16, size_hint_y=None)
        self.frame_cadastro.add_widget(Label(text="Nome do Produto:", font_size=16))
        self.frame_cadastro.add_widget(self.nome_entry)

        self.data_compra_entry = DateInput(height=30, font_size=16, size_hint_y=None)
        self.frame_cadastro.add_widget(Label(text="Data de Compra:", font_size=16))
        self.frame_cadastro.add_widget(self.data_compra_entry)

        self.validade_entry = DateInput(height=30, font_size=16, size_hint_y=None)
        self.frame_cadastro.add_widget(Label(text="Validade:", font_size=16))
        self.frame_cadastro.add_widget(self.validade_entry)

        self.quantidade_entry = TextInput(height=30, font_size=16, size_hint_y=None, input_filter='int')
        self.frame_cadastro.add_widget(Label(text="Quantidade:", font_size=16))
        self.frame_cadastro.add_widget(self.quantidade_entry)

        self.preco_entry = TextInput(height=30, font_size=16, size_hint_y=None)
        self.frame_cadastro.add_widget(Label(text="Preço:", font_size=16))
        self.frame_cadastro.add_widget(self.preco_entry)

        self.categoria_spinner = Spinner(
            text="Selecione",  # Texto inicial exibido no Spinner
            values=["Alimentos Básicos", "Produtos congelados", "Produtos enlatados e embalados",
                    "Produtos de higiene pessoal e cosméticos", "Medicamentos e suplementos", "Bebidas"],
            # Lista de opções disponíveis
            height=30,  # Altura do Spinner
            size_hint_y=None,  # Desativar o tamanho automático na direção y
            font_size=16  # Tamanho da fonte do texto no Spinner
        )
        self.frame_cadastro.add_widget(Label(text="Categoria do Produto:", font_size=16))
        self.frame_cadastro.add_widget(self.categoria_spinner)

        self.descricao_entry = TextInput(height=30, font_size=16, size_hint_y=None)
        self.frame_cadastro.add_widget(Label(text="Descrição do Produto:", font_size=16))
        self.frame_cadastro.add_widget(self.descricao_entry)

        self.preco_compra_entry = TextInput(height=30, font_size=16, size_hint_y=None)
        self.frame_cadastro.add_widget(Label(text="Preço de Compra:", font_size=16))
        self.frame_cadastro.add_widget(self.preco_compra_entry)

        self.fornecedor_entry = TextInput(height=30, font_size=16, size_hint_y=None)
        self.frame_cadastro.add_widget(Label(text="Fornecedor:", font_size=16))
        self.frame_cadastro.add_widget(self.fornecedor_entry)

        self.unidade_medida_spinner = Spinner(
            text="Selecione",  # Texto inicial exibido no Spinner
            values=["mg", "g", "kg", "ml", "L", "oz", "lb"],  # Lista de opções disponíveis
            height=30,  # Altura do Spinner
            size_hint_y=None,  # Desativar o tamanho automático na direção y
            font_size=16  # Tamanho da fonte do texto no Spinner
        )
        self.frame_cadastro.add_widget(Label(text="Unidade de Medida:", font_size=16))
        self.frame_cadastro.add_widget(self.unidade_medida_spinner)

        self.imagem_entry = TextInput(height=30, font_size=16, size_hint_y=None)
        self.frame_cadastro.add_widget(Label(text="Imagem do Produto:", font_size=16))
        self.frame_cadastro.add_widget(self.imagem_entry)

        self.observacoes_entry = TextInput(height=30, font_size=16, size_hint_y=None)
        self.frame_cadastro.add_widget(Label(text="Observações Adicionais:", font_size=16))
        self.frame_cadastro.add_widget(self.observacoes_entry)

        # Botão para adicionar produto
        self.adicionar_button = Button(text="Adicionar Produto", on_press=self.adicionar_produto, font_size=16,
                                       size_hint_y=None, height=50)
        self.frame_cadastro.add_widget(self.adicionar_button)

        # Pouch para os produtos próximos da validade
        self.frame_proximos = BoxLayout(orientation='vertical')
        self.add_widget(self.frame_proximos)

        self.frame_proximos.add_widget(Label(text="Produtos Próximos da Validade:", font_size=16))

        self.lista_proximos = BoxLayout(orientation='vertical')
        self.frame_proximos.add_widget(self.lista_proximos)

    def adicionar_produto(self, instance):
        codigo_barra = self.codigo_barra_entry.text
        nome = self.nome_entry.text
        data_compra_text = self.data_compra_entry.text
        validade_text = self.validade_entry.text
        quantidade = self.quantidade_entry.text
        preco = self.preco_entry.text
        categoria = self.categoria_spinner.text
        descricao = self.descricao_entry.text
        preco_compra = self.preco_compra_entry.text
        fornecedor = self.fornecedor_entry.text
        unidade_medida = self.unidade_medida_spinner.text
        imagem = self.imagem_entry.text
        observacoes = self.observacoes_entry.text

        if data_compra_text and validade_text and quantidade and preco and categoria and descricao and preco_compra and fornecedor and unidade_medida and imagem and observacoes:
            data_compra = datetime.strptime(data_compra_text, "%d/%m/%Y").date()
            validade = datetime.strptime(validade_text, "%d/%m/%Y").date()
            quantidade = int(quantidade)
            preco = float(preco)
            preco_compra = float(preco_compra)

            produto = Produto(codigo_barra, nome, data_compra, validade, quantidade, preco, categoria, descricao,
                              preco_compra, fornecedor, unidade_medida, imagem, observacoes)
            self.sistema.adicionar_produto(produto)
            self.codigo_barra_entry.text = ''
            self.nome_entry.text = ''
            self.data_compra_entry.text = ''
            self.validade_entry.text = ''
            self.quantidade_entry.text = ''
            self.preco_entry.text = ''
            self.categoria_spinner.text = 'Selecione'
            self.descricao_entry.text = ''
            self.preco_compra_entry.text = ''
            self.fornecedor_entry.text = ''
            self.unidade_medida_spinner.text = 'Selecione'
            self.imagem_entry.text = ''
            self.observacoes_entry.text = ''

            self.atualizar_lista_proximos()
        else:
            popup = Popup(title='Erro', content=Label(text='Todos os campos devem ser preenchidos.'), size_hint=(None, None),
                          size=(400, 200))
            popup.open()

    def selecionar_data_compra(self, instance):
        self.popup = Popup(title='Selecionar Data de Compra', content=TextInput(), size_hint=(None, None), size=(300, 100))
        self.popup.open()

    def selecionar_validade(self, instance):
        self.popup = Popup(title='Selecionar Data de Validade', content=TextInput(), size_hint=(None, None), size=(300, 100))
        self.popup.open()

    def atualizar_lista_proximos(self):
        self.lista_proximos.clear_widgets()
        produtos_proximos = self.sistema.produtos_proximos_validade()
        for produto in produtos_proximos:
            label = Label(text=f"{produto.nome} - Dias para Validade: {produto.dias_para_validade()}", font_size=20)
            self.lista_proximos.add_widget(label)


class CadastroApp(App):
    def build(self):
        return GUI()

if __name__ == "__main__":
    CadastroApp().run()
