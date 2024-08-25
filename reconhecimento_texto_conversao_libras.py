import easyocr
import os
from moviepy.editor import VideoFileClip
from enelvo.normaliser import Normaliser


# Função para verificar se o vídeo existe e exibi-lo usando moviepy
def play_video(video_path):
    if os.path.exists(video_path):
        print(f"Exibindo vídeo: {video_path}")

        # Carregar e exibir o vídeo usando moviepy
        clip = VideoFileClip(video_path)
        clip.preview()

    else:
        print(f"Vídeo não encontrado: {video_path}")


# Criar um leitor OCR
reader = easyocr.Reader(['en', 'pt'])

# Caminho para a imagem
image_path = 'images/espelho.jpg'
text_final = ""

# Caminho para a pasta de vídeos
videos_folder = 'Sinalizador02/Canon'

# Instanciando o normalizador de texto
norm = Normaliser(tokenizer='readable')

try:
    # Realizar OCR
    results = reader.readtext(image_path)

    # Exibir os resultados
    print("Texto extraído:")

    for result in results:
        box = result[0]  # Coordenadas da caixa de texto
        text = result[1]  # Texto extraído
        confidence = result[2]  # Pontuação de confiança
        text_final = text_final + " " + text

        print(f"Texto: {text}")
        print(f"Coordenadas da caixa: {box}")
        print(f"Confiança: {confidence}")
        print()

    print(f"Texto FINAL: {text_final}")
    text_final = norm.normalise(text_final)
    print(f"Texto final NORMALIZADO: {text_final}")

    # Separar as palavras do texto final
    words = text_final.split()
    print(f"Palavras a procurar: {words}")

    # Procurar vídeos correspondentes na pasta
    found_words = set()
    for word in words:
        video_found = False
        for file_name in os.listdir(videos_folder):
            # Normalizar o nome do arquivo e a palavra
            file_name_normalized = file_name.lower()
            word_normalized = word.lower()

            # Verificar se a palavra está no nome do arquivo
            if word_normalized in file_name_normalized:
                video_path = os.path.join(videos_folder, file_name)
                print(f"Vídeo correspondente encontrado: {video_path}")
                play_video(video_path)
                video_found = True
                found_words.add(word)
                print(f"Palavra encontrada: {word}")  # Mostrar a palavra encontrada
                break

        if not video_found:
            print(f"Palavra não encontrada: {word}")


    # Verificar se todas as palavras foram encontradas
    missing_words = set(words) - found_words
    if missing_words:
        print(f"Palavras não encontradas: {', '.join(missing_words)}")

except Exception as e:
    print(f"Erro ao processar a imagem: {e}")
