import cv2 as cv
from matplotlib import pyplot as plt 

imagem = cv.imread('Fotos/gatos.jpg')

gatinhosNumaCesta=cv.cvtColor(imagem,cv.COLOR_BGR2RGB)

blur=cv.GaussianBlur(gatinhosNumaCesta,(5,5),cv.BORDER_DEFAULT)

contorno = cv.Canny(blur,125,175)


contornos,hierarquia=cv.findContours(contorno, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contornos)}, contornos contados ')

plt.imshow(contornos)

plt.show()
