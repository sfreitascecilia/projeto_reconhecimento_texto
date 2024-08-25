import easyocr
from enelvo.normaliser import Normaliser

# Criar um leitor OCR
reader = easyocr.Reader(['en', 'pt'])

# Caminho para a imagem
image_path = 'images/teste_manuscrito_01.jpg'
text_final = ""

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

except Exception as e:
    print(f"Erro ao processar a imagem: {e}")
