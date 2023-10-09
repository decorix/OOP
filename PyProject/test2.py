import numpy as np
import cv2
from PIL import Image

# def find_object_slope(image_path):
#     # Загрузка изображения
#     image = cv2.imread(image_path)

#     # Преобразование изображения в оттенки серого
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Применение алгоритма Canny для выделения границ объекта
#     edges = cv2.Canny(gray, 50, 150)

#     # Поиск прямых на изображении с помощью преобразования Хафа
#     lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

#     # Вычисление угла наклона прямой
#     slope = np.degrees(np.arctan2(lines[0][0][3] - lines[0][0][1], lines[0][0][2] - lines[0][0][0]))

#     return slope

# Пример использования
image_path = 'C:\\Users\\User\\Desktop\\4sem\\OOP\\PyProject\\vizitka.png'
im = Image.open(image_path)
width, height = im.size
print(width, height)
# slope = find_object_slope(image_path)
# print('Угол наклона объекта:', slope, 'градусов')













# import cv2
# import numpy as np

# def find_rotation_angle(image_path):
#     # Загрузка изображения
#     image = cv2.imread(image_path)

#     # Преобразование изображения в оттенки серого
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Поиск контуров на изображении
#     contours, _ = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Определение наименьшего прямоугольника, описывающего все контуры
#     rect = cv2.minAreaRect(contours[0])

#     # Вычисляем угол поворота
#     rotation_angle = rect[-1]

#     return rotation_angle

# # Пример использования
# image_path = "moneta2.png"
# rotation_angle = find_rotation_angle(image_path)
# print(f"Угол поворота изображения: {rotation_angle} градусов")
