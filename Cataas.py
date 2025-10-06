'''Создание связи python с интернетом'''
from cProfile import label
from tkinter import *
from PIL import Image, ImageTk  # библиотека для работы с картинками
import requests              # библиотека для обеспечения связи python с интернетом
from io import BytesIO      # библиотека io для ввода и вывода информации

from pygame.examples.chimp import load_image

# BytesIO для преобразования информации из десятичной системы в изображение

window = Tk()
window.title('Cats')
window.geometry('600x480')

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)  # устанавливаем картинку на метку
    label.image = img    # это нужно для того, чтобы сборщика нашу картинку не удалил

window.mainloop()


