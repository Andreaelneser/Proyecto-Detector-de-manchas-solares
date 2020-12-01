import cv2
import matplotlib.pyplot as plt
import glob
import os

counter = -1
def plotImg(img): #método para graficar imagenes
    if len(img.shape) == 2:
        plt.imshow(img, cmap='gray')
        plt.show()
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()

path = 'D:/Documents/Universidad/Lala/Hola/PROYECTO/Sol'
path_file = os.path.join(path, 'sol*.png')
images = glob.glob(path_file)

for img_name in images:
    img = cv2.imread(img_name)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thr_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 15, 15)
    plotImg(thr_img) #imagen con threshold
    _, _, boxes, _ = cv2.connectedComponentsWithStats(thr_img)

    boxes = boxes[1:]

    filtered_boxes = []
    for x, y, w, h, pixels in boxes:
        if pixels > 1 and h < 100 and w < 300 and h > 1 and w > 1: #tamaño de manchas
            filtered_boxes.append((x, y, w, h))

    for x, y, w, h in filtered_boxes:
        rectangulo = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1) #dibujo de las cajas sobre las manchas, delgados y de color rojo
        counter = counter + 1 #contador de cajas, el número de cajas es el número de manchas
    print("El numero de manchas es:", counter)
    counter = 0
    plotImg(img)

cv2.destroyAllWindows()
