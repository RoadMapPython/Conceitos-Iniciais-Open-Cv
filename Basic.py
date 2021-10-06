import cv2 as cv
#Armazena a imagem em uma variavel
img=cv.imread('Fotos/woman.jpg')

#Inicio a imagem em uma escala de cinza
cinza=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Mostro a imagem em uma janela passando o parametro cinza
cv.imshow("Pessoa",cinza)


#imagem com blur
imagem_borrada=cv.GaussianBlur(cinza, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Borrado",imagem_borrada)

#contornos da imagem
contorno=cv.Canny(imagem_borrada,125,175)
cv.imshow("Contornos",contorno)


#Quantidade de contornos sem blur
contornos,hierarquia= cv.findContours(contorno,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contornos)} , contornos achados')



cv.waitKey(0)