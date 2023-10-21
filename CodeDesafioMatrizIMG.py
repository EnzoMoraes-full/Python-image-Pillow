#necessario a instalação da bibliteca Pillow

#importa a bibliteca e pega a imagem
from PIL import Image

#cria uma funcao que executa a media do RGB e retorna a media
def calcularMediaRGB(r, g , b):
    media = (r + g + b) // 3
#o retorno deve receber as 3 media, pois senao a img sofre distorcoes de cores sksk
    return (media, media, media)

#cria uma variavel img que recebe a imagem que eu escolhi
img = Image.open("cachoroTrajado.jpg")

#crio a variavel largura e altura e passo seus repectivos tamanhos (da imagem)
largura, altura = img.size

#crio uma variavel para receber a nova imagem e falo que ela será RGB e suas dimencoes
imgNew = Image.new("RGB", (largura, altura))

#crio as variaveis x e y para o loop
x = 0
y = 0

#crio um While e passo que o meu y tem que ser menor que a altura (da img).
while y < altura:
    
#falo que as variaveis r, g e b receberao os seus repectivos pixeis 
    r, g , b = img.getpixel((x, y))
    
#calculo a media
    mediaRGB = calcularMediaRGB(r, g , b)
    
#falo que os pixeis da nova img serão substituidos pela media dos memos
    imgNew.putpixel((x, y), mediaRGB)

#incremento mais 1 a minha linha
    x += 1

#se x for igual a largura, o x reseta e incrementa mais 1 na minha coluna
    if x == largura:
        x = 0
        y += 1

#crio a variavel enderecoDog e passo o endereco da nova img 
enderecoDog = "ChachorroPretoNoBranco.jpg"
#salva a nova img com o enderecoDOg
imgNew.save(enderecoDog)

#verifica se a imagem foi salva
if Image.open(enderecoDog):
    print("Tudo certo, meu parceiro!")
else:
    print("Algo de errado, ta não certo!")
#FIM