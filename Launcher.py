import os
 
 # _____    _        ____    ______ 
 #|  __ \  | |      |  _ \  |  ____|
 #| |__) | | |      | |_) | | |__   
 #|  ___/  | |      |  _ <  |  __|  
 #| |      | |____  | |_) | | |     
 #|_|      |______| |____/  |_|     
                                  
print("Esta utilizando PLBF(Paid Link Bot Farm)")
print("Hecho por Laggg")
print("-El proyecto esta en fase de pruebas y tiene muchos fallos que se solucionaran en futuras actualizaciones")
print("Elija su modo")
print("1-Modo normal(Para usuarios normales)")
print("2-Modo link fijo (No es dificil pero hay que editar codigo se recomienda usar solo usuarios avanzados)")

mainpath = os.path.dirname(os.path.realpath(__file__))

filename1 = "main.py"
filename2 = "modo-link-fijo.py"

fullpath1 = os.path.join(mainpath, filename1)
fullpath2 = os.path.join(mainpath, filename2)

while True:
    mode = input("Elija el modo(1 o 2):" )
    if mode == "1":
        os.system(fullpath1)
        break
    elif mode == "2":
        os.system(fullpath2)
        break
    else:
        print("Elija algo válido")
