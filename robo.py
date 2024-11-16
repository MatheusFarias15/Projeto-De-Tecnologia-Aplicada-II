import pyautogui
import os
from time import sleep

caminho = "C:\\Users\\mf056\\OneDrive\\Área de Trabalho\\Projeto-De-Tecnologia-Aplicada-II-main\\Teste de Tela para a bomba correta"
botao = "Botao.png"
botao2 = "Botao.png"  
MF = "MaisFuncoes.png"

if not os.path.exists(os.path.join(caminho, botao)):
    raise FileNotFoundError(f"O arquivo de imagem {botao} não foi encontrado no diretório {caminho}.")
if not os.path.exists(os.path.join(caminho, botao2)):
    raise FileNotFoundError(f"O arquivo de imagem {botao2} não foi encontrado no diretório {caminho}.")
os.chdir(caminho)

n = 3
k = 0

while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(botao)
        if local is not None:  
            pyautogui.moveTo(local, duration=0.8)  
            pyautogui.click()  
            print("Botão 1 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {botao} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


k = 0  
while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(botao2)
        if local is not None:  
            pyautogui.moveTo(local, duration=0.8)  
            pyautogui.click()  
            print("Botão 2 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {botao2} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


k = 0  
while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(MF)
        if local is not None:  
            pyautogui.moveTo(local, duration=0.8)  
            pyautogui.click()  
            print("MF clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {MF} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)







if k == n:
    pyautogui.alert(
        text='Teste de tela concluído com sucesso, mas algumas funções não estão funcionando corretamente. Recomendo verificar novamente.',
        title='Teste de tela',
        button='OK'
    )
