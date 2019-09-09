from matplotlib import pyplot as plt
import cv2

#print(imagem[0][0])

# LER IMAGEM
imagem   = cv2.imread("t2.png")
gray_img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

h = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

plt.figure()
plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(h)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

# grafico escala de cinza
import numpy as np
img = cv2.imread('t2.png', cv2.IMREAD_GRAYSCALE)
img = cv2.equalizeHist(img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color='gray' )

# plt.xlabel('intensidad de iluminacion')
# plt.ylabel('cantidad de pixeles')
plt.show()

img = cv2.imread('t2.png')
cv2.imshow('t2.png', img)

color = ('b','g','r')

for i, c in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

plt.show()



cv2.imshow("Imagem 2", gray_img)
cv2.waitKey(0)