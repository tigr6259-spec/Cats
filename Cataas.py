'''Создание связи python с интернетом'''
from cProfile import label
from idlelib.rpc import response_queue
from tkinter import *
from PIL import Image, ImageTk  # библиотека для работы с картинками
import requests              # библиотека для обеспечения связи python с интернетом
from io import BytesIO      # библиотека io для ввода и вывода информации

from django.utils.text import normalize_newlines


# BytesIO для преобразования информации из десятичной системы в изображение
#from pygame.examples.chimp import load_image


def load_image()
    try:
        response = requests.get(url)   # делаем запрос по ссылке url и положим в response
        response.raise_for_status()     # обрабока исключений
        image_data = BytesIO(response.content) # сама картинка будет обработана с помощью BytesIO
        img = Image.open(image_data)        # открываем изображение с помощью библиотеки PIL и кладём в img(локал.перем.)
        return ImageTk.PhotoImage(img)  # функция вернёт картинку и положит в другой img, которое прописано в window
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None



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


