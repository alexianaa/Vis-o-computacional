import cv2

image = cv2.imread("lena.png") #le a imagem

print(image.shape) #printa o tamanho da imagem

cv2.imshow("imagem",image) #mostra a imagem
cv2.waitKey(0) #tempo em milisegundos para mostrar

#se tiver cv2.waitKey(0) a janela ira esperar alguma interação para fechar