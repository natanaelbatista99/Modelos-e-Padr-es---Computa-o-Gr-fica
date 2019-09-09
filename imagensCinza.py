import cv2, queue, math

#print(imagem[0][0])

# LER IMAGEM
imagem    = cv2.imread("corte7.png")
gray_img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

lic = 999
lsc = -1

for l in gray_img:
    for c in l:
        #print(c)

        if c > lsc:
            lsc = c
        if c < lic:
            lic = c

#exit()

imagem  = cv2.imread("t2.png")

cv2.imshow("Imagem 1", imagem)
cv2.waitKey(0)

gray_img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

print("Altura (height): %d pixels" % (imagem.shape[0]))
print("Largura (width): %d pixels" % (imagem.shape[1]))
print("Canais (channels): %d"      % (imagem.shape[2]))
print("%d %d|" % (lic, lsc))

print(gray_img.shape)

for l in range(0, gray_img.shape[0]):
    for c in range(0, gray_img.shape[1]):
        if(gray_img[l][c] >= lic + 30 and gray_img[l][c] <= lsc - 30):
            gray_img[l][c] = 255

# ESCREVER NOVA IMAGEM
cv2.imwrite("newimgGray.png", gray_img)

cv2.imshow("Imagem 2", gray_img)
cv2.waitKey(0)