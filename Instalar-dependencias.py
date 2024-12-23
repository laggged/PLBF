import os
import subprocess


mainpath = os.path.abspath(__file__)
maindir = os.path.dirname(mainpath)

firstime = os.path.join(maindir, "cache.txt")

if not os.path.exists(firstime):
    with open(firstime, "w") as file:
        file.write("Este archivo es para comprobar si has ejecutado antes el bot")
    print("Creando", firstime)
    if os.path.isfile(firstime):
        print("El archivo está en el directorio actual.")

    subprocess.run(["pip", "install", "-r", "requirements.txt"], cwd=maindir)

else:
    # Si el archivo ya existe, simplemente no se hace nada
    print("Las librerias ya se han instalado")
