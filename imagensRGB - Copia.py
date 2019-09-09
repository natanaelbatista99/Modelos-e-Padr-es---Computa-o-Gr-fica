
import cv2, queue, math

def inGrid(l, c, hl, hc):
    return 1 if(l >= 0 and c >= 0 and l < hl and c < hc) else 0

# LER IMAGEM
imagem = cv2.imread("corte2.png")
#cv2.imshow("Original", imagem)
 
print("Altura (height): %d pixels" % (imagem.shape[0]))
print("Largura (width): %d pixels" % (imagem.shape[1]))
print("Canais (channels): %d"      % (imagem.shape[2]))

#print(imagem[0][0])

lir = 256
lsr = 0
lig = 256
lsg = 0
lib = 256
lsb = 0

for l in imagem:
    for c in l:
        (b, g, r) = c

        if(r < lir):
            lir = r
        if(r > lsr):
            lsr = r

        if(g < lig):
            lig = g
        if(g > lsg):
            lsg = g

        if(b < lib):
            lib = b
        if(b > lsb):
            lsb = b

print("R[%3d - %3d]\nG[%3d - %3d]\nB[%3d - %3d]" % (lir, lsr, lig, lsg, lib, lsb))

imagem = cv2.imread("araraazul.jpg")

height = imagem.shape[0]
width  = imagem.shape[1]

for l in range(0, height):
        for c in range(0, width):
                (b, g, r) = imagem[l][c]
                #print(imagem[l][c])

                if(((r >= lir and r <= lsr) and (g >= lig and g <= lsg) and (b >= lib and b <= lsb)) or
                   ((r >= 0 and r <= 10) and (g >= 13 and g <= 33) and (b >= 157 and b <= 177)) or
                   ((r >= 0 and r <= 24) and (g >= 35 and g <= 55) and (b >= 110 and b <= 135)) or
                   ((r >= 0 and r <= 23) and (g >= 30 and g <= 50) and (b >= 160 and b <= 185)) or
                   ((r >= 0 and r <= 10) and (g >= 25 and g <= 50) and (b >= 140 and b <= 165)) or
                   ((r >= 18 and r <= 48) and (g >= 25 and g <= 50) and (b >= 140 and b <= 165)) or
                   ((r >= 1 and r <= 21) and (g >= 5 and g <= 25) and (b >= 79 and b <= 99)) or
                   ((r >= 6 and r <= 26) and (g >= 20 and g <= 40) and (b >= 59 and b <= 79))):

                        #print(inGrid(l - 1, c - 1, imagem.shape[0], imagem.shape[1]))
                        if(inGrid(l - 1, c - 1, height, width) == 1 and inGrid(l - 2, c - 2, height, width) == 1):
                                dist1 = math.sqrt(math.pow(r - imagem[l - 1][c - 1][2], 2) + math.pow(g - imagem[l - 1][c - 1][1], 2) + math.pow(b - imagem[l - 1][c - 1][0], 2))
                                dist2 = math.sqrt(math.pow(r - imagem[l - 2][c - 2][2], 2) + math.pow(g - imagem[l - 2][c - 2][1], 2) + math.pow(b - imagem[l - 2][c - 2][0], 2))

                                if(dist1 <= dist2):
                                        imagem[l - 1][c - 1][2] = 255
                                        imagem[l - 1][c - 1][1] = 0
                                        imagem[l - 1][c - 1][0] = 0

                        if(inGrid(l - 1, c, height, width) == 1 and inGrid(l - 2, c, height, width) == 1):
                                dist1 = math.sqrt(math.pow(r - imagem[l - 1][c][2], 2) + math.pow(g - imagem[l - 1][c][1], 2) + math.pow(b - imagem[l - 1][c][0], 2))
                                dist2 = math.sqrt(math.pow(r - imagem[l - 2][c][2], 2) + math.pow(g - imagem[l - 2][c][1], 2) + math.pow(b - imagem[l - 2][c][0], 2))

                                if(dist1 <= dist2):
                                        imagem[l - 1][c][2] = 255
                                        imagem[l - 1][c][1] = 0
                                        imagem[l - 1][c][0] = 0
                
                        if(inGrid(l - 1, c + 1, height, width) == 1 and inGrid(l - 2, c + 2, height, width) == 1):
                                dist1 = math.sqrt(math.pow(r - imagem[l - 1][c + 1][2], 2) + math.pow(g - imagem[l - 1][c + 1][1], 2) + math.pow(b - imagem[l - 1][c + 1][0], 2))
                                dist2 = math.sqrt(math.pow(r - imagem[l - 2][c + 2][2], 2) + math.pow(g - imagem[l - 2][c + 2][1], 2) + math.pow(b - imagem[l - 2][c + 2][0], 2))

                                if(dist1 <= dist2):
                                        imagem[l - 1][c + 1][2] = 255
                                        imagem[l - 1][c + 1][1] = 0
                                        imagem[l - 1][c + 1][0] = 0

                        if(inGrid(l, c - 1, height, width) == 1 and inGrid(l, c - 2, height, width) == 1):
                                dist1 = math.sqrt(math.pow(r - imagem[l][c - 1][2], 2) + math.pow(g - imagem[l][c - 1][1], 2) + math.pow(b - imagem[l][c - 1][0], 2))
                                dist2 = math.sqrt(math.pow(r - imagem[l][c - 2][2], 2) + math.pow(g - imagem[l][c - 2][1], 2) + math.pow(b - imagem[l][c - 2][0], 2))

                                if(dist1 <= dist2):
                                        imagem[l][c - 1][2] = 255
                                        imagem[l][c - 1][1] = 0
                                        imagem[l][c - 1][0] = 0

                        if(inGrid(l, c + 1, height, width) == 1 and inGrid(l, c + 2, height, width) == 1):
                                dist1 = math.sqrt(math.pow(r - imagem[l][c + 1][2], 2) + math.pow(g - imagem[l][c + 1][1], 2) + math.pow(b - imagem[l][c + 1][0], 2))
                                dist2 = math.sqrt(math.pow(r - imagem[l][c + 2][2], 2) + math.pow(g - imagem[l][c + 2][1], 2) + math.pow(b - imagem[l][c + 2][0], 2))

                                if(dist1 <= dist2):
                                        imagem[l][c + 1][2] = 255
                                        imagem[l][c + 1][1] = 0
                                        imagem[l][c + 1][0] = 0

                        if(inGrid(l + 1, c - 1, height, width) == 1 and inGrid(l + 2, c - 2, height, width) == 1):
                                dist1 = math.sqrt(math.pow(r - imagem[l + 1][c - 1][2], 2) + math.pow(g - imagem[l + 1][c - 1][1], 2) + math.pow(b - imagem[l + 1][c - 1][0], 2))
                                dist2 = math.sqrt(math.pow(r - imagem[l + 2][c - 2][2], 2) + math.pow(g - imagem[l + 2][c - 2][1], 2) + math.pow(b - imagem[l + 2][c - 2][0], 2))

                                if(dist1 <= dist2):
                                        imagem[l + 1][c - 1][2] = 255
                                        imagem[l + 1][c - 1][1] = 0
                                        imagem[l + 1][c - 1][0] = 0

                        if(inGrid(l + 1, c, height, width) == 1 and inGrid(l + 2, c, height, width) == 1):
                                dist1 = math.sqrt(math.pow(r - imagem[l + 1][c][2], 2) + math.pow(g - imagem[l + 1][c][1], 2) + math.pow(b - imagem[l + 1][c][0], 2))
                                dist2 = math.sqrt(math.pow(r - imagem[l + 2][c][2], 2) + math.pow(g - imagem[l + 2][c][1], 2) + math.pow(b - imagem[l + 2][c][0], 2))

                                if(dist1 <= dist2):
                                        imagem[l + 1][c][2] = 255
                                        imagem[l + 1][c][1] = 0
                                        imagem[l + 1][c][0] = 0

                        if(inGrid(l + 1, c + 1, height, width) == 1 and inGrid(l + 2, c + 2, height, width) == 1):
                                dist1 = math.sqrt(math.pow(r - imagem[l + 1][c + 1][2], 2) + math.pow(g - imagem[l + 1][c + 1][1], 2) + math.pow(b - imagem[l + 1][c + 1][0], 2))
                                dist2 = math.sqrt(math.pow(r - imagem[l + 2][c + 2][2], 2) + math.pow(g - imagem[l + 2][c + 2][1], 2) + math.pow(b - imagem[l + 2][c + 2][0], 2))

                                if(dist1 <= dist2):
                                        imagem[l + 1][c + 1][2] = 255
                                        imagem[l + 1][c + 1][1] = 0
                                        imagem[l + 1][c + 1][0] = 0

                        imagem[l][c][2] = 255
                        imagem[l][c][1] = 0
                        imagem[l][c][0] = 0

# ESCREVER NOVA IMAGEM
cv2.imwrite("newimg.png", imagem)

# MOSTRA A IMAGEM
cv2.imshow("Fatia da imagem", imagem)
cv2.waitKey(0)

'''
            fila = queue.Queue(maxsize=20)

            fila.put(5)
            fila.put(3)
            fila.put(1)

            print(fila.get())
'''
