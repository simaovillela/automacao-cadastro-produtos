import pyautogui
import time

def clicar(x, y):
    pyautogui.click(x, y)
    time.sleep(1)  

# repetições
num_iteracoes = 2

time.sleep(5)  

# loop de cadastro
for i in range(num_iteracoes):
    # copiar do excel
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1) 

    # alt tab pra ir no google
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1) 

    clicar(935, 281)  
    clicar(741, 274)  

    # colar o conteúdo
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  

    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    time.sleep(1) 

    pyautogui.hotkey('alt', 'tab')
    time.sleep(1) 

    pyautogui.hotkey('down')
    time.sleep(1) 

