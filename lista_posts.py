import os

DIRETORIO_VIDEOS = r"C:\Users\pierr\Videos"

# Puxa todos os arquivos que estão dentro da pasta
arquivos_na_pasta = os.listdir(DIRETORIO_VIDEOS)

# Filtra para pegar apenas os vídeos (que terminam com .mp4) e que tenham "shorts" no nome
lista_videos = []
for arquivo in arquivos_na_pasta:
    if "shorts" in arquivo.lower() and arquivo.endswith(".mp4"):
        lista_videos.append(arquivo)

# Organiza a lista. Isso garante que "shorts - 0907" venha antes de "shorts2 - 0907" 
# e que o dia 07 venha antes do dia 08
lista_videos.sort()

# Imprime o resultado no formato exato da variável do seu robô
print("Copie o bloco abaixo e cole no seu script principal:\n")
print("videos_para_subir = [")
for i, video in enumerate(lista_videos):
    if i < len(lista_videos) - 1:
        print(f'    "{video}",')
    else:
        print(f'    "{video}"')
print("]")

videos_para_subir = [
    "shorts - 0911.mp4",
    "shorts - 0912.mp4",
    "shorts2 - 0907.mp4",
    "shorts2 - 0908.mp4",
    "shorts2 - 0909.mp4",
    "shorts2 - 0910.mp4",
    "shorts2 - 0911.mp4",
    "shorts2 - 0912.mp4"
]