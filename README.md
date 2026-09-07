# 🚀 TikTok Auto Uploader "Raiz"

Um script de automação em Python para postar e agendar vídeos em massa no **TikTok Studio Web**. 

Em vez de usar ferramentas web que deixam rastros e correm o risco de tomar *shadowban*, este bot foi feito com **PyAutoGUI**. Ele literalmente assume o controle do seu mouse e teclado, simulando o comportamento humano com pausas aleatórias para passar ileso pelo radar anti-bot do TikTok.

---

## ✨ Funcionalidades

* 🤖 **Comportamento Humano:** Digitação letra por letra e tempos de espera aleatórios entre os cliques.
* 📝 **Auto-preenchimento:** Limpa a caixa de texto e insere sua legenda padrão automaticamente.
* 🗓️ **Agendamento Inteligente:** O script faz todo o trabalho braçal e pausa estrategicamente para você escolher a data e hora do calendário. Apertou a barra de espaço, ele finaliza e já puxa o próximo vídeo.
* 🔁 **Loop Contínuo:** Suporta listas de dezenas de vídeos para rodar em sequência.

---

## 🛠️ O que você precisa instalar

Você vai precisar do Python instalado na sua máquina e de duas bibliotecas principais. Abra o seu terminal e rode:

`pip install pyautogui keyboard`

---

## ⚙️ Como configurar para o seu PC

Como o script usa as coordenadas (X e Y) da **sua** tela, você precisa mapear onde os botões do TikTok estão no seu monitor, já que isso muda dependendo da resolução.

**1. Mapeie os botões:**
Abra o TikTok Studio Web com a tela maximizada e use o seu arquivo `marca_pos.py` para descobrir o X e Y de cada botão.

**2. Atualize o código (`utils.py`):**
Vá no seu arquivo de utilitários e substitua os números pelos que você encontrou:
`BOTAO_UPLOAD_INICIAL = pyautogui.Point(x=1415, y=523)`
`CAIXA_DESCRICAO      = pyautogui.Point(x=1220, y=464)`
*(atualize os outros botões)*

**3. Ajuste suas variáveis:**
Ainda no `utils.py`, coloque o caminho da pasta onde ficam seus vídeos e a legenda padrão:
`DESCRICAO_VIDEO = "VIDEO COMPLETO NO CANAL DO MEGA !!! @ocanaldomegaa"`
`DIRETORIO_VIDEOS = r"C:\Users\pierr\Videos"`

---

## 🚀 Como usar

1. Rode o script `lista_posts.py` para gerar a lista dos nomes dos seus vídeos.
2. Cole a lista gerada na variável `videos_para_subir` no `main.py`.
3. Abra a tela de upload do **TikTok Studio Web** e deixe a janela maximizada.
4. Rode o `main.py` no terminal.
5. **Solte o mouse!** Deixe o robô trabalhar.
6. Quando ele clicar no botão de "Schedule" (Agendar), o terminal vai avisar. Escolha a data/hora com o mouse e aperte **ESPAÇO** para o script continuar e puxar o próximo vídeo.

---

## 🚨 Freio de Emergência (Failsafe)

Deu ruim? O script clicou fora ou o TikTok jogou um Captcha na tela? 
**Jogue o ponteiro do mouse com força para qualquer um dos 4 cantos do seu monitor.** 
Isso ativa a trava de segurança do PyAutoGUI e encerra o script na mesma hora.