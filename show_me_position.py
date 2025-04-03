import pyautogui
import threading
import time

parar = False

def esperar_enter():
    global parar
    input("Pressione Enter para parar...\n")
    parar = True

def mostrar_posicao():
    while not parar:
        x, y = pyautogui.position()
        print(f"Posição atual do mouse -> Horizontal: {x} | Vertical: {y}")
        time.sleep(1)

if __name__ == "__main__":
    # Rodar o "input" em uma thread separada
    thread_input = threading.Thread(target=esperar_enter)
    thread_input.start()

    # Mostrar posição do mouse
    mostrar_posicao()
