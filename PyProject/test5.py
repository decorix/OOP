import tkinter 
from PIL import Image, ImageTk
from tkinter import IntVar, filedialog
import numpy as np
import cv2
from rembg import remove 



class App:
    def __init__(self):
        self.root = tkinter.Tk()

        # создаем рабочую область
        self.frame = tkinter.Frame(self.root, borderwidth=2, relief='solid')
        self.frame.grid()
        self.frame2 = tkinter.Frame(self.root, borderwidth=2, relief='solid')
        self.frame2.grid()
        self.frame3 = tkinter.Frame(self.root, borderwidth=2, relief='solid')
        self.frame3.grid()

        # self.widthOld = 0
        # self.heightOld  = 0
        self.width = 0
        self.height = 0
        
        self.enabled = IntVar()
        
        # self.enabled_checkbutton = tkinter.Checkbutton(text="Картинка перевернута", variable=self.enabled, command=self.checkbutton_changed)
        # self.enabled_checkbutton.grid(row=3, column=1)
        
        self.reverse = False  #проверка перевернута ли фотография
        self.status = False

        # Добавим метку
        # self.label = tkinter.Label(self.frame, text="Hello, World!").grid(row=1, column=1)
        self.label = tkinter.Label(self.frame3, text="Расстояние между границей \n прозрачного фона и изображения").grid(row=1, column=4)

       


        self.image1 = Image.new(size=(250, 250), mode='RGBA', color='white')
        self.photo1 = ImageTk.PhotoImage(self.image1)
        
        self.path = ''
        
        
        self.image2 = Image.new(size=(250, 250), mode='RGBA', color='white')
        self.photo2 = ImageTk.PhotoImage(self.image2)

        # вставляем кнопку
        self.but = tkinter.Button(self.frame, text="Загрузить картинку", command=self.my_event_handler).grid(row=1, column=1)
        # self.open_button = tkinter.Button(text="Открыть файл", command=self.open_file).pack(row=1, column=3)
        self.but2 = tkinter.Button(self.frame2, text="Редактировать картинку", command=self.editingPicture).grid(row=1, column=2)
        self.but3 = tkinter.Button(self.frame3, text="Против часовой", command=self.leftRotate).grid(row=2, column=1)
        self.but4 = tkinter.Button(self.frame3, text="По часовой", command=self.rightRotate).grid(row=2, column=2)
        self.but5 = tkinter.Button(self.frame3, text="Удалить прозрачный фон", command=self.deleteBackground).grid(row=2, column=3)
        
        self.spinbox_var = 0
        
        self.spinbox = tkinter.Spinbox(self.frame3, from_=1.0, to=100.0, command=self.pixel)
        self.spinbox.grid(row=2, column=4)
        # self.but6 = tkinter.Button(self.frame3, text="По часовой", command=self.rightRotate).grid(row=1, column=2)



        # Добавим изображение
        self.canvas = tkinter.Canvas(self.frame, height=300, width=300, borderwidth=2, relief='solid')
        self.c_image = self.canvas.create_image(0, 0, anchor='nw')
        self.canvas.grid()
        
        self.canvas2 = tkinter.Canvas(self.frame2, height=300, width=300, borderwidth=2, relief='solid')
        self.c_image2 = self.canvas2.create_image(0, 0, anchor='nw')
        self.canvas2.grid()
        
        self.root.mainloop()

    def my_event_handler(self):
        print("my_event_handler")
        self.path = filedialog.askopenfilename()
        result = self.path.split('.')
        img = Image.open(self.path)
        self.width, self.height = img.size
        self.label = tkinter.Label(self.frame, text=f"Размер изображения: {self.width}x{self.height} ").grid(row=3, column=1)
        new_image = img.resize((300, 300))
        new_image.save(result[0]+'ResizeOld.' + result[1])
        self.image1=Image.open(result[0]+'ResizeOld.' + result[1])
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo1)
        self.canvas.grid(row=2, column=1)
        

              
    def editingPicture(self):
        print("editingPicture")
        print(self.path)
        
        input = Image.open(self.path)
        output = remove(input)
        output.save(self.path)
        self.search_degrees()

    
    def search_degrees(self):
        print("search_degrees")
        # Загрузка изображения
        image = cv2.imread(self.path)

        # Преобразование изображения в оттенки серого
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Применение алгоритма Canny для выделения границ объекта
        edges = cv2.Canny(gray, 50, 150)

        # Поиск прямых на изображении с помощью преобразования Хафа
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

        # Вычисление угла наклона прямой
        slope = np.degrees(np.arctan2(lines[0][0][3] - lines[0][0][1], lines[0][0][2] - lines[0][0][0]))

        print('Угол изображения: ' + str(slope))
        self.rotate_picture(slope)
        
    def rotate_picture(self, degress):
        print("rotate_picture")
        im = Image.open(self.path)
        if (self.status == True):
            im_rotate = im.rotate(degress)
        else:
            if (self.reverse==True):
                im_rotate = im.rotate(degress+180)
                self.status = True
            else:
                im_rotate = im.rotate(degress)
                self.status = True

        
        im_rotate.save(self.path, quality=95)
        im.close()
        self.resizePicture()
        
    def resizePicture(self):
        print(self.path)
        result = self.path.split('.')
        img = Image.open(self.path)
        self.width, self.height = img.size
        self.searchSize()

                        # изменяем размер
        new_image = img.resize((300, 300))
                        # сохранение картинки
        new_image.save(result[0]+'Resize.' + result[1])
        print(result[0]+'Resize.' + result[1])
        
        
        self.image2=Image.open(result[0]+'Resize.' + result[1])
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.c_image2 = self.canvas2.create_image(0, 0, anchor='nw', image=self.photo2)
        self.canvas2.grid(row=2, column=1)
        
    def checkbutton_changed(self):
        if self.enabled.get() == 1:
            self.reverse = True
        else:
            self.reverse = False
            
    def leftRotate(self):
        self.rotate_picture(90)
    def rightRotate(self):
        self.rotate_picture(-90)
        
    def deleteBackground(self):        
        image = Image.open(self.path)
        # Создаем список пикселей, содержащий непрозрачные пиксели
        transparent = Image.new('RGBA', image.size, (0, 0, 0, 0))
        transparent.paste(image, (0, 0), mask=image)
        
        # Находим левую, правую, верхнюю и нижнюю границы непрозрачных пикселей
        left, top, right, bottom = image.width, image.height, 0, 0
        for x in range(image.width):
            for y in range(image.height):
                pixel = transparent.getpixel((x, y))
                if pixel[3] != 0:  # Если пиксель непрозрачный
                    left = min(left, x)
                    top = min(top, y)
                    right = max(right, x)
                    bottom = max(bottom, y)
        
        # Обрезаем изображение по найденным границам
        cropped_image = image.crop((left-self.spinbox_var, top-self.spinbox_var, right+self.spinbox_var, bottom+self.spinbox_var))
        
        self.width=cropped_image.width
        self.height=cropped_image.height
        self.searchSize()

        # Сохраняем обрезанное изображение
        cropped_image.save(self.path)
        
    def searchSize(self):
        self.label = tkinter.Label(self.frame2, text=f"Размер изображения: {self.width}x{self.height} ").grid(row=3, column=1)

    def pixel(self):
        self.spinbox_var = int(self.spinbox.get())

        
app= App()