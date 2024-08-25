import easyocr
import moviepy.editor as mp
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip


# Função para criar o arquivo SRT com legendas
def create_srt_file(texts, filename='legenda.srt'):
    with open(filename, 'w') as f:
        for i, text in enumerate(texts):
            start_time = f"00:00:{i * 5:02},000"
            end_time = f"00:00:{(i + 1) * 5:02},000"
            f.write(f"{i + 1}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{text}\n")
            f.write("\n")


# Criar um leitor OCR
reader = easyocr.Reader(['pt'])

# Caminho para a imagem
image_path = 'images/caneca.jpg'

try:
    # Realizar OCR
    results = reader.readtext(image_path)

    # Coletar o texto extraído
    texts = [result[1] for result in results]

    # Exibir os resultados
    print("Texto extraído:")
    for result in results:
        box = result[0]  # Coordenadas da caixa de texto
        text = result[1]  # Texto extraído
        confidence = result[2]  # Pontuação de confiança

        print(f"Texto: {text}")
        print(f"Coordenadas da caixa: {box}")
        print(f"Confiança: {confidence}")
        print()

    print(f"Texto FINAL: {texts}")

    # Criar o arquivo SRT (legenda)
    create_srt_file(texts)

    # Configurações do vídeo de saída
    width, height = 640, 480  # Dimensões do vídeo
    duration = len(texts) * 5  # Duração total do vídeo em segundos (5 segundos por legenda)
    fps = 24  # Taxa de quadros por segundo

    # Criar um fundo preto
    video = mp.ColorClip(size=(width, height), color=(0, 0, 0), duration=duration)
    video = video.set_fps(fps)


    # Função para gerar o clip de legenda
    def generator(txt):
        return TextClip(txt, fontsize=24, color='white', size=(width, height)).set_duration(5)


    # Criar o clip de legendas
    subtitles = SubtitlesClip('legenda.srt', generator)

    # Adicionar legendas ao fundo preto
    final_video = CompositeVideoClip([video, subtitles.set_pos(('center', 'bottom'))])
    final_video = final_video.set_fps(fps)
    final_video.write_videofile('video_com_legendas.mp4', codec='libx264', fps=fps)

except Exception as e:
    print(f"Erro ao processar a imagem ou o vídeo: {e}")
