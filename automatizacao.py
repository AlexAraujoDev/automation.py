# Automalização de tarefa usando Python. dinâmica seguida pelo canal do Dev Aprender. (Usado arquivos disponibilizados pelo canal e VSCode).

import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuário;
pyautogui.click(987,541,duration=0.1)
pyautogui.write('Alex')
# 2 - Clicar e digitar minha senha;
pyautogui.click(988,573,duration=0.1)
pyautogui.write('123456')
# 3 - Clicar em "Entrar"
pyautogui.click(848,611,duration=0.1)
# 4 - Extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #     1 - Clicar e digitar produto
        pyautogui.click(667,531,duration=0.1)
        pyautogui.write(produto)
        #     2 - Clicar e digitar quantidade
        pyautogui.click(667,558,duration=0.1)
        pyautogui.write(quantidade)
        #     3 - Clicar e digitar preço
        pyautogui.click(650,592,duration=0.1)
        pyautogui.write(preco)
        #     4 - Clicar em registrar
        pyautogui.click(506,795,duration=0.1)
        sleep(1)
