import cv2

cap = cv2.VideoCapture(0) # recebe o video, num inteiro direciona para a camera do dispositivo

while True: # se nao houver video para a execucao
    ret, frame = cap.read()
    
    if not ret:
        break
    
    cv2.imshow("video",frame) #se tiver le o video
    # cv2.waitKey(33) : mostra o video, 30 fps -> 1/30 = 0.033s -> 33ms
    if cv2.waitKey(33) != -1: # se clicar numa tecla a funcao cap.waitKey retorna -1 e termina a execução
        break