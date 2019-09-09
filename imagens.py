
import cv2, queue

def inGrid(l, c, hl, hc):
	1 if (l >= 0 and c >= 0 and l < hl and c < hc) else 0

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

print("%d - %d - %d - %d - %d - %d" % (lir, lsr, lig, lsg, lib, lsb))

imagem = cv2.imread("araraazul.jpg")

for l in range(0, imagem.shape[0]):
	for c in range(0, imagem.shape[1]):
		(b, g, r) = imagem[l][c]
		#print(imagem[l][c])

		if(((r >= lir and r <= lsr) and (g >= lig and g <= lsg) and (b >= lib and b <= lsb))):
			imagem[l][c][2] = 255
			imagem[l][c][1] = 0
			imagem[l][c][0] = 0


			if(inGrid(l - 1, c - 1, imagem.shape[0], imagem.shape[1]) == 1):
				print("aqui")

'''
			fila = queue.Queue(maxsize=20)

			fila.put(5)
			fila.put(3)
			fila.put(1)

			print(fila.get())
'''

			


# ESCREVER NOVA IMAGEM
cv2.imwrite("newimg.png", imagem)

# MOSTRA A IMAGEM
cv2.imshow("Fatia da imagem", imagem)
cv2.waitKey(0)