import pyautogui 
import os 
from time import sleep

caminho = "C:\\Users\\mf056\\OneDrive\\Área de Trabalho\\PI 4° semestre\\Imagens testes"
arquivo = "imagem.png" 
foto = "Teste.png"
pesquisa = "pesquisa.png"
teste = "teste2.png"
novapesquisa = "tecnico.png"
novotexto="Novapesquisa.png"

if not os.path.exists(os.path.join(caminho, arquivo)):
    raise FileNotFoundError(f"O arquivo de imagem {arquivo} não foi encontrado no diretório {caminho}.")
os.chdir(caminho)
k = 0
n = 10 

while k < n:
    try:
        
        local = pyautogui.locateCenterOnScreen(arquivo)
        
        if local is not None:  
            pyautogui.moveTo(local, duration=0.8)  
            pyautogui.click()  
        
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)  


while k < n:
    try:
        
        local1 = pyautogui.locateCenterOnScreen(foto)
        
        if local1 is not None:  
            pyautogui.moveTo(local1, duration=0.8)  
            pyautogui.click()  
        
            break 

        k += 1 
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25) 

while k < n:
    try:
    
        local2 = pyautogui.locateCenterOnScreen(pesquisa)
        
        if local2 is not None:  
            pyautogui.moveTo(local2, duration=0.8)  
            pyautogui.click()  
            pyautogui.write ("Engenharia", interval= 0.2)
            pyautogui.press('enter') 
        
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local3 = pyautogui.locateCenterOnScreen(teste)
        
        if local3 is not None:  
            pyautogui.moveTo(local3, duration=0.8)  
            pyautogui.click()  
          
            break  

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local4 = pyautogui.locateCenterOnScreen(novapesquisa)
        
        if local4 is not None: 
            pyautogui.moveTo(local4, duration=0.8)  
            pyautogui.click()  
          
            break 

        k += 1 
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:

        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local5 = pyautogui.locateCenterOnScreen(novotexto)
        
        if local5 is not None:  
            pyautogui.moveTo(local5, duration=0.8) 
            pyautogui.click()  
            pyautogui.write ("Estetica", interval= 0.2) 
            pyautogui.press('enter') 
        
            break  

        k += 1
        print(f'Tentativa {k}/{n} - Imagem não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:

        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)





if k == n:
    pyautogui.alert(text='Teste de tela concluído com sucesso as funções não estão funcionando corretamente recomendo verificar novamente', title ='Teste de tela ', button ='OK')  