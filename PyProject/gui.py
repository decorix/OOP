# from tkinter import *
# from main import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import filedialog
# import os


# input_name_file=''
# output_name_file=''


# def clicked():
#     print
    


#     # delete_background()
    
    


# window = Tk()
# window.geometry('1000x900')
# window.title("Обработчик изображений")

# ttk.Style().configure(".",  font="helvetica 13", foreground="#004D40", padding=8, background="#B2DFDB") 
 
# ttk.Label(text="Добро пожаловать!").pack(anchor=CENTER, padx=6, pady=6)
# ttk.Button(text="Выбрать изображение", command=clicked).pack(anchor=CENTER, padx=6, pady=6)

# canvas1 = Canvas(bg="white", width=300, height=300)

# ttk.Label(text="Исходное изображение").pack(anchor=CENTER, padx=6, pady=6)
# canvas1.pack(anchor=CENTER)
# python_image1 = PhotoImage(file=filepath)
# canvas1.create_image(0, 0, anchor=NW, image=python_image1)

# canvas2 = Canvas(bg="white", width=300, height=300)


# ttk.Label(text="Обработанное изображение").pack(anchor=CENTER, padx=6, pady=6)
# canvas2.pack(anchor=CENTER, expand=0)
                    
# python_image2 = PhotoImage(file="vizitkaresize.png")
                    
# canvas2.create_image(0, 0, anchor=NW, image=python_image2)

# # открываем файл в текстовое поле
# # def open_file():
# #     filepath = filedialog.askopenfilename()
# # def open_img():
# #     x = openfn()
# #     img = Image.open(x)
# #     img = img.resize((250, 250), Image.ANTIALIAS)
# #     img = ImageTk.PhotoImage(img)
# #     panel = Label(root, image=img)
# #     panel.image = img
# #     panel.pack()

# # open_button = ttk.Button(text="Открыть файл", command=open_file).pack(anchor=CENTER, padx=6, pady=6)
# window.mainloop()
