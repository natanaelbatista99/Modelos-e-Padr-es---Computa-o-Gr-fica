import cv2, queue, math

#print(imagem[0][0])

# LER IMAGEM
imagem = cv2.imread("corte43.png")
HSV_img = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

lih = 256
lsh = 0

for l in HSV_img:
    for c in l:
        #print(c)
        (h, s, v) = c

        if(h >= lsh):
            lsh = h
        if(h <= lih):
            lih = h

#exit()

imagem  = cv2.imread("t2.png")

print("Altura (height): %d pixels" % (imagem.shape[0]))
print("Largura (width): %d pixels" % (imagem.shape[1]))
print("Canais (channels): %d"      % (imagem.shape[2]))
print("%d %d|" % (lih, lsh))

HSV_img = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

for l in HSV_img:
    for c in l:
        (h, s, v) = c

        if(h >= lih + 5 and h <= lsh - 5 and s > 90):
            c[2] = 255
            c[1] = 0
            c[0] = 0

# ESCREVER NOVA IMAGEM
cv2.imwrite("newimgHSV.png", HSV_img)

cv2.imshow("Imagem", HSV_img)
cv2.waitKey(0)

imagem  = cv2.imread("t2.png")

print("Altura (height): %d pixels" % (imagem.shape[0]))
print("Largura (width): %d pixels" % (imagem.shape[1]))
print("Canais (channels): %d"      % (imagem.shape[2]))
print("%d %d|" % (lih, lsh))

gray_img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem", gray_img)
cv2.waitKey(0)