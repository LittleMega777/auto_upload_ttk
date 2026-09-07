import time
import os

from utils import inserir_arquivo, preencher_descricao, agendar_e_resetar_pagina
from utils import DIRETORIO_VIDEOS, DESCRICAO_VIDEO

videos_para_subir = [
    "shorts - 0908.mp4",
    "shorts2 - 0908.mp4"
]

print("O script vai começar em 3 segundos. Deixe o TikTok na tela e solte o mouse!")
time.sleep(3)

# O loop agora fica super legível, quase como ler em português
for nome_do_arquivo in videos_para_subir:
    print(f"\n--- Subindo o vídeo: {nome_do_arquivo} ---")
    caminho_completo = os.path.join(DIRETORIO_VIDEOS, nome_do_arquivo)
    
    inserir_arquivo(caminho_completo)
    preencher_descricao(DESCRICAO_VIDEO)
    agendar_e_resetar_pagina()

print("\n🚀 Todos os vídeos da lista foram agendados com sucesso!")