import pyautogui
import time
import os

# Caminhos dos arquivos
caminho_imagem = os.path.join("imagem", "imagem_alvo.png")
caminho_config = "config.txt"

def ler_config():
    config = {"horizontal": None, "vertical": None, "tempo": None}
    try:
        with open(caminho_config, "r") as f:
            for linha in f:
                if "=" in linha:
                    chave, valor = linha.split("=")
                    chave = chave.strip().lower()
                    valor = int(valor.strip())
                    if chave in config:
                        config[chave] = valor
    except Exception as e:
        print(f"Erro ao ler config.txt: {e}")
    return config["horizontal"], config["vertical"], config["tempo"]

def procurar_e_clicar():
    global tempo
    print("Verificando imagem na tela...")
    local = pyautogui.locateOnScreen(caminho_imagem, confidence=0.8)
    if local:
        horizontal, vertical, tempo = ler_config()
        if horizontal is not None and vertical is not None:
            print(f"Imagem encontrada! Clicando em ({horizontal}, {vertical})")
            pyautogui.click(x=horizontal, y=vertical)
        else:
            print("Configuração incompleta no config.txt.")
    else:
        print("Imagem não encontrada.")

def loop_monitoramento():
    global tempo
    horizontal, vertical, tempo = ler_config()
    while True:
        try:
            procurar_e_clicar()
            print('sim')
        except:
            print('não')
        time.sleep(tempo)

if __name__ == "__main__":
    loop_monitoramento()
