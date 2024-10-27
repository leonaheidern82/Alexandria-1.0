from IPython import get_ipython
import ipywidgets as widgets
from IPython.display import display

import requests
import smtplib
from email.message import EmailMessage

#Criar widgets para inputs de cadastro 
client_id = widgets.Text(placeholder='Informe o ID do cliente')
infodata = widgets.Text(placeholder='Informe a data de entrega')
infohora = widgets.Text(placeholder='Informe a hora de entrega')
infovend = widgets.Text(placeholder='Informe o nome de quem efetuou a venda')

# Criar uma área de texto para informações adicionais 
print("\nInsira abaixo informações adicionais:")
text_area = widgets.Textarea(
    value='',
    placeholder='Caso necessário, insira aqui informações adicionais',
    description='',
    rows=10  
)

# Criar um botão
button = widgets.Button(description="Confirmar")

#Variável global para armazenar os dados
index = []

# Função para lidar com o evento do botão e enviar o e-mail
def on_button_clicked(b):
    global index
    
    #Criar uma lista com os valores de todos os inputs
    todos_imputs = [
    client_id.value,
    infodata.value,
    infohora.value,
    infovend.value,
    text_area.value
    ]

    #Atribuir a lista a index
    index = todos_imputs
       
    # Usando f-string para interpolar a variável
    corpo_email = f"""
    <p><b> Cadastro: </b></p>
    <p>ID do Cliente: {index[0]}<br>
    Data de Entrega: {index[1]}<br>
    Hora de Entrega: {index[2]}<br>
    Vendedor: {index[3]}<br>
    Informações Adicionais: {index[4]}</p>
    """

    msg = EmailMessage()
    msg['Subject'] = "Cadastro de nova ficha"
    msg['From'] = 'hekatepython@gmail.com'
    msg['To'] = 'daericktri@gmail.com'
    msg.set_content(corpo_email, subtype='html')

    # Enviar o e-mail
    with smtplib.SMTP('smtp.gmail.com', 587) as s:
      s.starttls()
      password = 'icykdgvymtoqoodr'
      s.login(msg['From'], password)
      s.send_message(msg)
      print('Email enviado')

# Conectar o evento do botão à função
button.on_click(on_button_clicked)

# Exibir os widgets
display(client_id, infodata, infohora, infovend, text_area, button)