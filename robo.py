# Instalar o Python 3.10
# No site https://www.python.org/downloads/release/python-31015/ Extrair no computador 
# Rodar no prompt de comando pip install --upgrade Pillow, pip install pyautogui, pip install pyscreeze

import pyautogui #biblioteca para reconhecimento de tela
import os #biblioteca responsável por mexer no sistema operacional
from time import sleep

# Define o caminho correto e o arquivo de imagem
caminho = "C:\\Users\\mf056\\OneDrive\\Área de Trabalho\\PI 4° semestre\\Imagens testes"
arquivo = "imagem.png" 
foto = "Teste.png"
pesquisa = "pesquisa.png"
teste = "teste2.png"
novapesquisa = "tecnico.png"
novotexto="Novapesquisa.png"

# Verifica se o arquivo de imagem existe no diretório
if not os.path.exists(os.path.join(caminho, arquivo)):
    raise FileNotFoundError(f"O arquivo de imagem {arquivo} não foi encontrado no diretório {caminho}.")

# Muda para o diretório onde a imagem está localizada
os.chdir(caminho)


k = 0
n = 10 # Número de tentativas

while k < n:
    try:
        # Tenta localizar a imagem na tela
        local = pyautogui.locateCenterOnScreen(arquivo)
        
        if local is not None:  # Se a imagem foi encontrada
            pyautogui.moveTo(local, duration=0.8)  # Move o cursor até a imagem
            pyautogui.click()  # Clica na imagem
        
            break  # Sai do loop

        k += 1  # Incrementa a contagem de tentativas
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  # Espera um tempo antes da próxima tentativa

    except pyautogui.ImageNotFoundException:
        # Tratar exceção caso a imagem não seja encontrada na tela
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)  # Espera antes da próxima tentativa


while k < n:
    try:
        # Tenta localizar a imagem na tela
        local1 = pyautogui.locateCenterOnScreen(foto)
        
        if local1 is not None:  # Se a imagem foi encontrada
            pyautogui.moveTo(local1, duration=0.8)  # Move o cursor até a imagem
            pyautogui.click()  # Clica na imagem
        
            break  # Sai do loop

        k += 1  # Incrementa a contagem de tentativas
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  # Espera um tempo antes da próxima tentativa

    except pyautogui.ImageNotFoundException:
        # Tratar exceção caso a imagem não seja encontrada na tela
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)  # Espera antes da próxima tentativa


while k < n:
    try:
        # Tenta localizar a imagem na tela
        local2 = pyautogui.locateCenterOnScreen(pesquisa)
        
        if local2 is not None:  # Se a imagem foi encontrada
            pyautogui.moveTo(local2, duration=0.8)  # Move o cursor até a imagem
            pyautogui.click()  # Clica na imagem
            pyautogui.write ("Engenharia", interval= 0.2) # escreve msg na tela 
            pyautogui.press('enter') # pressiona enter no teclado 
        
            break  # Sai do loop

        k += 1  # Incrementa a contagem de tentativas
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  # Espera um tempo antes da próxima tentativa

    except pyautogui.ImageNotFoundException:
        # Tratar exceção caso a imagem não seja encontrada na tela
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        # Tenta localizar a imagem na tela
        local3 = pyautogui.locateCenterOnScreen(teste)
        
        if local3 is not None:  # Se a imagem foi encontrada
            pyautogui.moveTo(local3, duration=0.8)  # Move o cursor até a imagem
            pyautogui.click()  # Clica na imagem
          
            break  # Sai do loop

        k += 1  # Incrementa a contagem de tentativas
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  # Espera um tempo antes da próxima tentativa

    except pyautogui.ImageNotFoundException:
        # Tratar exceção caso a imagem não seja encontrada na tela
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        # Tenta localizar a imagem na tela
        local4 = pyautogui.locateCenterOnScreen(novapesquisa)
        
        if local4 is not None:  # Se a imagem foi encontrada
            pyautogui.moveTo(local4, duration=0.8)  # Move o cursor até a imagem
            pyautogui.click()  # Clica na imagem
          
            break  # Sai do loop

        k += 1  # Incrementa a contagem de tentativas
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  # Espera um tempo antes da próxima tentativa

    except pyautogui.ImageNotFoundException:
        # Tratar exceção caso a imagem não seja encontrada na tela
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        # Tenta localizar a imagem na tela
        local5 = pyautogui.locateCenterOnScreen(novotexto)
        
        if local5 is not None:  # Se a imagem foi encontrada
            pyautogui.moveTo(local5, duration=0.8)  # Move o cursor até a imagem
            pyautogui.click()  # Clica na imagem
            pyautogui.write ("Estetica", interval= 0.2) # escreve msg na tela 
            pyautogui.press('enter') # pressiona enter no teclado 
        
            break  # Sai do loop

        k += 1  # Incrementa a contagem de tentativas
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  # Espera um tempo antes da próxima tentativa

    except pyautogui.ImageNotFoundException:
        # Tratar exceção caso a imagem não seja encontrada na tela
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)





if k == n:
    pyautogui.alert(text='Teste de tela concluído com sucesso as funções não estão funcionando corretamente recomendo verificar novamente', title ='Teste de tela ', button ='OK')  # Esta função exibe uma janela de alerta simples com um botão para fechar.