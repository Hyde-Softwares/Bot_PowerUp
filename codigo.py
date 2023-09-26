# Passo a passo do projeto

# Passo 1 : Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Passo 2 : Fazer Login;

# Passo 3: Importar a base de dados de produtos;

# Passo 4: Cadastrar 1 produto;

# Passo 5: Repetir o cadastro para todos os produtos;


# Instalar pyautogui
# Permite controlar a tela, mouse e teclado por codigo

import pyautogui

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalh(combinação de teclas)

pyautogui.PAUSE = 0.5

#abrir o chrome

pyautogui.press("win")
pyautogui.write("calculadora")
pyautogui.press("enter")

# entrar no link
# espera o site carregar