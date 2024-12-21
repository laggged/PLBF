import pyautogui

# Obtener la posición actual del cursor
posicion_cursor = pyautogui.position()

# Imprimir la posición del cursor
print("La posición actual del cursor es:", posicion_cursor)
print("La coordenada x es:", posicion_cursor.x)
print("La coordenada y es:", posicion_cursor.y)
