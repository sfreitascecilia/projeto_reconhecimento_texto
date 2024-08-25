import easyocr

# Mapeamento Braille para letras e números em português
braille_map = {
    'a': '100000',
    'b': '101000',
    'c': '110000',
    'd': '110100',
    'e': '100100',
    'f': '111000',
    'g': '111100',
    'h': '101100',
    'i': '011000',
    'j': '011100',
    'k': '100010',
    'l': '101010',
    'm': '110010',
    'n': '110110',
    'o': '100110',
    'p': '111010',
    'q': '111110',
    'r': '101110',
    's': '011010',
    't': '011110',
    'u': '100011',
    'v': '101011',
    'w': '011101',
    'x': '110011',
    'y': '110111',
    'z': '100111',
    'á': '100000',
    'é': '100101',
    'í': '011001',
    'ó': '110010',
    'ú': '100011',
    'ç': '110100',
    '1': '100000',
    '2': '101000',
    '3': '110000',
    '4': '110100',
    '5': '100100',
    '6': '111000',
    '7': '111100',
    '8': '101100',
    '9': '011000',
    '0': '011100',
    ' ': '000000'
}


def text_to_braille(text):
    return [braille_map.get(char.lower(), '000000') for char in text]


# Criar um leitor OCR
reader = easyocr.Reader(['pt'])

# Caminho para a imagem
image_path = 'images/caneca.jpg'

# Inicializar variáveis para armazenar o texto e a representação em Braille
text_final = ""
braille_final = ""

try:
    # Realizar OCR
    results = reader.readtext(image_path)

    # Exibir os resultados
    print("Texto extraído:")

    for result in results:
        box = result[0]  # Coordenadas da caixa de texto
        text = result[1]  # Texto extraído
        confidence = result[2]  # Pontuação de confiança

        # Converter texto para Braille
        braille_representation = text_to_braille(text)

        text_final += " " + text
        braille_final += " " + " ".join(braille_representation)

        print(f"Texto: {text}")
        print(f"Braille: {' '.join(braille_representation)}")
        print(f"Coordenadas da caixa: {box}")
        print(f"Confiança: {confidence}")
        print()

    print(f"\n *** ATENÇÃO ***")
    print(f"\n O alfabeto Braille é composto por uma cela com seis pontos (2 colunas x 3 linhas), "
          f"\nsuas diferentes combinações formam letras, números, sinais, entre outros. "
          f"\nVale lembrar que, alguns símbolos do alfabeto mudam de país para país."
          f"\nNo exemplo gerado por este código, o número 1 representa a cela que será perfurada "
          f"\npela máquina Braille."
          f"\nPara conhecer um pouco mais sobre a grafia Braille, "
          f"\nacesse: http://portal.mec.gov.br/seesp/arquivos/pdf/grafiaport.pdf")
    print(f"\nTexto FINAL: {text_final}")
    print(f"\nTexto FINAL em Braille: {braille_final}")

except Exception as e:
    print(f"Erro ao processar a imagem: {e}")
