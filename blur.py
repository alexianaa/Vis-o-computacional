import cv2

image = cv2.imread("lena.png") #le a imagem

image_blur = cv2.blur(image, (7,7)) #cria uma imagem borrada, quanto maior a ordem da kernel mais borrada a imagem fica

image_blur2 = cv2.GaussianBlur(image, (7,7), 0)

cv2.imshow("imagem",image) 
cv2.imshow("borrada",image_blur)
cv2.imshow("borrada2",image_blur2)
cv2.waitKey(0)