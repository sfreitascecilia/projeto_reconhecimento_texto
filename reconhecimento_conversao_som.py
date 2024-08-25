import easyocr
from gtts import gTTS
import os
import pygame

# Inicializar pygame mixer
pygame.mixer.init()

# Criar um leitor OCR
reader = easyocr.Reader(['pt'])

# Caminho para a imagem
image_path = 'images/caneca.jpg'

try:
    # Realizar OCR
    results = reader.readtext(image_path)

    # Exibir os resultados e reproduzir o áudio
    for result in results:
        box = result[0]  # Coordenadas da caixa de texto
        text = result[1]  # Texto extraído
        confidence = result[2]  # Pontuação de confiança

        print(f"Texto: {text}")
        print(f"Coordenadas da caixa: {box}")
        print(f"Confiança: {confidence}")
        print()

        # Converter o texto extraído para fala
        if text.strip():  # Verificar se o texto não está vazio
            tts = gTTS(text=text, lang='pt')
            audio_file = 'som.mp3'
            tts.save(audio_file)

            # Reproduzir o áudio usando pygame
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

            # Aguardar a reprodução terminar
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            os.remove(audio_file)  # Remove o arquivo de áudio após a reprodução

except Exception as e:
    print(f"Erro ao processar a imagem: {e}")
finally:
    pygame.mixer.quit()
