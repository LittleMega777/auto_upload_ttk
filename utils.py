import pyautogui
import time
import random
import keyboard
import os 

# ==========================================
# CONFIGURAÇÕES GERAIS
# ==========================================
DESCRICAO_VIDEO = "VIDEO COMPLETO NO CANAL DO MEGA !!! @ocanaldomegaa"
DIRETORIO_VIDEOS = r"C:\Users\pierr\Videos"

# ==========================================
# MAPEAMENTO DE COORDENADAS (X, Y)
# ==========================================
BOTAO_UPLOAD_INICIAL = pyautogui.Point(x=1415, y=523)
CAIXA_DESCRICAO      = pyautogui.Point(x=1220, y=464)
BOTAO_SCHEDULE_RADIO = pyautogui.Point(x=739, y=1081)
BOTAO_SCHEDULE_CONF  = pyautogui.Point(x=736, y=1294)
BOTAO_VALIDACAO      = pyautogui.Point(x=1476, y=790)
BOTAO_NOVO_UPLOAD    = pyautogui.Point(x=113, y=205)

# ==========================================
# FUNÇÕES DE AUTOMAÇÃO
# ==========================================
def pausa_aleatoria(minimo, maximo):
    """Gera um tempo de espera aleatório para simular comportamento humano."""
    tempo = random.uniform(minimo, maximo)
    time.sleep(tempo)

def inserir_arquivo(caminho_completo):
    """Clica na área de upload, digita o caminho do vídeo e dá Enter."""
    pyautogui.click(BOTAO_UPLOAD_INICIAL)
    pausa_aleatoria(1.5, 2.5)
    
    pyautogui.write(caminho_completo, interval=0.05)
    pausa_aleatoria(0.5, 1.0)
    pyautogui.press('enter')

def preencher_descricao(texto):
    """Clica na caixa de texto, apaga o conteúdo antigo e escreve a legenda nova."""
    pausa_aleatoria(1.5, 2.5)
    pyautogui.click(CAIXA_DESCRICAO)
    pausa_aleatoria(0.5, 1.0)
    
    pyautogui.hotkey('ctrl', 'a')
    pausa_aleatoria(0.2, 0.6)
    pyautogui.press('backspace')
    pausa_aleatoria(0.4, 0.9)
    
    pyautogui.write(texto, interval=0.05)
    pausa_aleatoria(3, 4)
    pyautogui.press('enter')
    pausa_aleatoria(3, 4)

def agendar_e_resetar_pagina():
    """Faz o fluxo final de agendamento com a pausa manual, e prepara pro próximo vídeo."""
    pyautogui.click(BOTAO_SCHEDULE_RADIO)
    pausa_aleatoria(1.0, 1.5)

    print("⏳ Sua vez! Escolha a data e o horário lá no TikTok.")
    print("Quando terminar, aperte a tecla ESPAÇO para o script continuar...")
    keyboard.wait('space')
    
    print("Boa! Seguindo o baile...")
    pausa_aleatoria(1.0, 2.0)

    pyautogui.click(BOTAO_SCHEDULE_CONF)
    pausa_aleatoria(1.0, 2.0)

    pyautogui.click(BOTAO_VALIDACAO)
    pausa_aleatoria(3, 4)

    pyautogui.click(BOTAO_NOVO_UPLOAD)
    print("Esperando a tela recarregar pro próximo vídeo...")
    pausa_aleatoria(5.0, 7.0)