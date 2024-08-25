## Sobre

A proposta do exercício é produzir um algoritmo de reconhecimento de textos.
Após a extração do texto, considerou-se disponiblizar a solução para pessoas 
com diferentes necessidades e capacidades. Assim sendo, foi implementado: 1) 
um código para conversão de imagem/vídeo em texto; 2) um código para
conversão do texto em legenda; 3) um código para conversão do texto em som; 4) um código para conversão
do texto em libras.

## Sobre o programa para conversão de textos para libras

Após a localização e separação das palavras, o programa fará a busca do vídeo que contém a reperesentação em libras
daquele sinal. As palavras que não possuírem sinal correspondente serão listadas. Para aquelas que possuírem sinal
correspondente, será exibido um vídeo com a representação em libras do sinal. Para exemplificar o funcionamento
do código, deixei salvo apenas o arquivo '12EspelhoSinalizadoro2-1.mp4' e para encontrar a palavra "espelho" e o
sinal correspondente.

## Instalar dependências

    pip install -r requirements.txt

## Para instalar o ImageMagick

    https://imagemagick.org/script/download.php#google_vignette
    Verificar a instalação: magick --version

    Obs: talvez seja necessário editar o caminho de IMAGEMAGICK_BINARY 
    em .venv/Lib/site-packages/moviepy/config_defaults.py.
    Exemplo: IMAGEMAGICK_BINARY = r'C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe'

## Verificar a instalação do pygame

    python -m pygame.examples.aliens

## Atualizar pip

    python.exe -m pip install --upgrade pip


## Dataset utilizado - Língua Brasileira de Sinais (LIBRAS)

    V-librasil: https://libras.cin.ufpe.br/

    Outros datasets disponíveis:
    LIBRAS-HC-RGBDS: https://web.inf.ufpr.br/vri/databases/brazilian-sign-language-libras-hand-configurations-database/
    LIBRAS-UFOP: https://www.sciencedirect.com/science/article/abs/pii/S0957417420309143?via%3Dihub
    MINDS-Libras Dataset: https://zenodo.org/records/2667329