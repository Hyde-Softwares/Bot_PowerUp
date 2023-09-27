# Passo a passo do projeto

# Passo 1 : Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Passo 2 : Fazer Login;

# Passo 3: Importar a base de dados de produtos;

# Passo 4: Cadastrar 1 produto;

# Passo 5: Repetir o cadastro para todos os produtos;


# Instalar pyautogui
# Permite controlar a tela, mouse e teclado por codigo

import time
import pyautogui

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalh(combinação de teclas)

pyautogui.PAUSE = 0.2

#abrir o chrome
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

# entrar no link
link_site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.click(x=684, y=69)

pyautogui.write(link_site)

time.sleep(0.2)

pyautogui.press("enter")

# espera o site carregar

time.sleep(1)


# Passo 2 : Fazer Login

pyautogui.click(x=640, y=451)


pyautogui.write("hydeoshy.kaled65@gmail.com")

time.sleep(1)

pyautogui.press("tab") #Pular para o campo da senha

pyautogui.write("sua senha aqui")

pyautogui.press("tab")
 
pyautogui.press("enter") 

time.sleep(3)

# Passo 3: Importar a base de dados de produtos;

import pandas


tabela = pandas.read_csv("produtos.csv")


# Passo 4: Cadastrar 1 produto;

pyautogui.click(x=775, y=309)

# Preencher os campos
pyautogui.write("Codigo")

pyautogui.press("tab")

pyautogui.write("Marca")

pyautogui.press("tab")

pyautogui.write("Tipo")

pyautogui.press("tab")

pyautogui.write("Categoria")

pyautogui.press("tab")

pyautogui.write("Preco")

pyautogui.press("tab")

pyautogui.write("Preco")

pyautogui.press("tab")

pyautogui.write("Custo")

pyautogui.press("tab")

pyautogui.write("OBS")

pyautogui.click(x=884, y=693)

pyautogui.press("enter")
# Passo 5: Repetir o cadastro para todos os produtos;