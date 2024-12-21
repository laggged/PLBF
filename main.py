import pyautogui as pag
import time as t

 # _____    _        ____    ______ 
 #|  __ \  | |      |  _ \  |  ____|
 #| |__) | | |      | |_) | | |__   
 #|  ___/  | |      |  _ <  |  __|  
 #| |      | |____  | |_) | | |     
 #|_|      |______| |____/  |_|  

print("ESTA UTILIZANDO P.L.B.F (Paid link bot farm) Hecho por Laggg en su modo normal")
paylink = input("introduzca el link de pago:" )
browser = input("Introduzca su navegador:" )
step = 0 

#mi link https://ouo.io/21sGS8s

def stepuno():
    pag.press("win")
    print("Esperando un segundo por seguridad")
    t.sleep(1.00)
    pag.typewrite(browser)
    t.sleep(0.100)
    pag.press("enter")
    t.sleep(0.500)
    step = 1
    repeat()

def repeat():
    print("Abriendo link")
    pag.typewrite(paylink)
    t.sleep(0.500)
    pag.press("enter")
    step = 2 #Se a abierto el link
    stepdos()


def stepdos():
    pag.moveTo(717, 458)#Esto puede cambiar dependiendo donde este su firefox y de la resolucion de su monitor
    t.sleep(10.0)
    print("Esperando...")
    pag.click()
    print("En este punto deberia estar en el contador")
    step = 3
    steptres()

def steptres():
    print("Esperando a que cargue la pagina")
    t.sleep(1.00)
    pag.moveTo(712,625)
    print("Esperando a que el contador llegue a 0")
    t.sleep(5.00)
    print("Haciendo click")
    pag.click()
    t.sleep(0.200)
    step = 4
    stepcuatro()

def stepcuatro():
    pag.moveTo(723,117)
    t.sleep(0.100)
    pag.click()
    t.sleep(0.100)
    step = 1
    repeat()


if step == 0:
    stepuno()



