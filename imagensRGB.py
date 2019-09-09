
import cv2, queue, math

def inGrid(l, c, hl, hc):
    return 1 if(l >= 0 and c >= 0 and l < hl and c < hc) else 0

# LER IMAGEM
imagem = cv2.imread("corte7.png")
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

imagem = cv2.imread("t2.png")

height = imagem.shape[0]
width  = imagem.shape[1]

for l in range(0, height):
        for c in range(0, width):
                (b, g, r) = imagem[l][c]
                #print(imagem[l][c])

                if(((r >= lir + 12 and r <= lsr - 12) and (g >= lig + 12 and g <= lsg - 12) and (b >= lib + 12 and b <= lsb - 12)) or
                   ((r >= 9 and r <= 29) and (g >= 20 and g <= 40) and (b >= 135 and b <= 155)) or
                   ((r >= 16 and r <= 36) and (g >= 26 and g <= 46) and (b >= 171 and b <= 191)) or
                   ((r >= 8 and r <= 28) and (g >= 14 and g <= 34) and (b >= 102 and b <= 122)) or
                   ((r >= 94 and r <= 114) and (g >= 144 and g <= 164) and (b >= 239 and b <= 259)) or
                   ((r >= 27 and r <= 47) and (g >= 25 and g <= 45) and (b >= 154 and b <= 174)) or
                   ((r >= 31 and r <= 51) and (g >= 34 and g <= 54) and (b >= 130 and b <= 150)) or
                   ((r >= 53 and r <= 73) and (g >= 112 and g <= 132) and (b >= 236 and b <= 256)) or
                   ((r >= 111 and r <= 131) and (g >= 132 and g <= 152) and (b >= 212 and b <= 232)) or
                   ((r >= 117 and r <= 137) and (g >= 163 and g <= 183) and (b >= 241 and b <= 255))):

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
cv2.imwrite("newimgRGB.png", imagem)

# MOSTRA A IMAGEM
cv2.imshow("Fatia da imagem", imagem)
cv2.waitKey(0)