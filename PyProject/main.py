from rembg import remove 
from PIL import Image 
import easygui as eg
import numpy as np
import cv2
# from gui import resizePicture
input_name_file='dsdsds'
output_name_file=''


def delete_background():
    print("delete_background")
    # input_path = eg.fileopenbox(title='Исходное изображение')
    input_path='C:\\Users\\User\\Desktop\\4sem\\OOP\\PyProject\\spider.png'
    # result = input_path.split('.')
    # output_path = result[0]+'Finished.' + result[1]
    reverse = False
    input = Image.open(input_path)
    output = remove(input)

    output.save(input_path)

    search_degrees(input_path, reverse)
    # resizePicture(input_path)
  

def search_degrees(image_path, reverse):
    print("search_degrees")
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Преобразование изображения в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Применение алгоритма Canny для выделения границ объекта
    edges = cv2.Canny(gray, 50, 150)

    # Поиск прямых на изображении с помощью преобразования Хафа
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

    # Вычисление угла наклона прямой
    slope = np.degrees(np.arctan2(lines[0][0][3] - lines[0][0][1], lines[0][0][2] - lines[0][0][0]))
    print(str(slope))
    return rotate_picture(int(slope), image_path, reverse)


def rotate_picture(degress, image_path, reverse):
    print("rotate_picture")
    im = Image.open(image_path)
    # if (reverse==True):
    #     im_rotate = im.rotate(degress+180)
    # else:
    # im_rotate = im.rotate(degress)
    # if (degress>5):
    #     im_rotate = im.rotate(degress-90)
    # elif (degress<5):
    #     im_rotate = im.rotate(90+degress)
    # else:
    #     im_rotate = im.rotate(0)
    # im_rotate.save(image_path, quality=95)
    im.close()
    resizePicture(image_path)

def resizePicture(image_path):
    print(image_path)
    result = image_path.split('.')
    img = Image.open(image_path)
                    # изменяем размер
    new_image = img.resize((300, 300))
    new_image.show()
                    # сохранение картинки
    new_image.save(result[0]+'Resize.' + result[1])
    print(result[0]+'Resize.' + result[1])
    
delete_background()

    
    


