# PLBF
Un bot para "Hacer trampa" en los links de pago y asi recibir mas visitas
 _____    _        ____    ______ 
|  __ \  | |      |  _ \  |  ____|
| |__) | | |      | |_) | | |__   
|  ___/  | |      |  _ <  |  __|  
| |      | |____  | |_) | | |     
|_|      |______| |____/  |_|  
Paid Link Bot Farm

PARA HACER FUNCIONAR EL BOT DEBE SEGUIR LOS SIGUENTES PASOS:

1-Instalar Python 3.12 o superior, durante la instalacion asegurece de marcar la casilla "Instalar en la raiz del sistema".
2-Ejecute el siguiente comando (Mediante el cmd):

pip install -r requirements.txt

Si el comando no funciona intente con el siguiente comando si da error vuelva a hacer el paso 1:

python -v

Una vez instaladas las dependencias, ejecute el launcher.py y elija el modo deseado.


POR AHORA SOLO FUNCIONA EN WINDOWS(Se a provado solo en windows 10 puede tener problemas en otras versiones)
POR AHORA SOLO FUNCIONA CON LINKS DE OUO.IO!
SOLO FUNCIONA SI TU NAVEGADOR TIENE LA EXTENSIÓN "uBlock Origins"
(Solo se a provado con firefox pero deberia funcionar correctamente en otros navegadores)


SOLUCION DE ALGUNOS DE LOS PROBLEMAS:

-El mouse no da click en el lugar donde deberia:
Esto puede ocurrir por varias razones ya sea por la resolucion de tu monitor o el navegador que 
estes usando y la unica manera de solucionarloes editando el codigo manualmente, para saber donde
se encuentran las cordenasdas del botonen tu monitor puedes utilizar el archivo Mouseinfo.py y ya
con esas cordenadas puedes editar el codigo en donde diria algo como pag.moveTo(x,y).

-Ocurre un error al ejecutar el launcher o el bot
Esto puede ocurrir por varias causas como por ejemplo no haber segudo correctamente los pasos anteriores
o haber editado el codigo de forma erronea. Puede solucionarse re instalando Python y los requirements 
o restaurando los archivos originales del bot. Si despues de hacer esto siguen sin ejecutarse intente con el
siguiente comando(Desde el cmd)

python Launcher.py

-Si tengo un problema a que no aparece aqui a quien contacto
Puedes poner tu issue en github ya que el programa esta en modo beta sin embargo es un proyecto personal 
y no es seguro que tenga actualizaciones.

