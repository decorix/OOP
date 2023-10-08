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

        
        self.enabled = IntVar()
        
        self.enabled_checkbutton = tkinter.Checkbutton(text="Картинка перевернута", variable=self.enabled, command=self.checkbutton_changed)
        self.enabled_checkbutton.grid(row=3, column=1)
        
        self.reverse = False  #проверка перевернута ли фотография
        self.status = False

        # Добавим метку
        self.label = tkinter.Label(self.frame, text="Hello, World!").grid(row=1, column=1)

        self.image1 = Image.open("C:\\Users\\User\\Desktop\\4sem\\OOP\\PyProject\\whiteBG.png")
        self.photo1 = ImageTk.PhotoImage(self.image1)
        
        self.path = ''
        
        self.image2 = Image.open("C:\\Users\\User\\Desktop\\4sem\\OOP\\PyProject\\whiteBG.png")
        self.photo2 = ImageTk.PhotoImage(self.image2)

        # вставляем кнопку
        self.but = tkinter.Button(self.frame, text="Загрузить картинку", command=self.my_event_handler).grid(row=2, column=1)
        # self.open_button = tkinter.Button(text="Открыть файл", command=self.open_file).pack(row=1, column=3)
        self.but2 = tkinter.Button(self.frame2, text="Редактировать картинку", command=self.editingPicture).grid(row=1, column=2)
        self.but3 = tkinter.Button(self.frame3, text="Влево", command=self.leftRotate).grid(row=1, column=1)
        self.but4 = tkinter.Button(self.frame3, text="Вправо", command=self.rightRotate).grid(row=1, column=2)


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

app= App()