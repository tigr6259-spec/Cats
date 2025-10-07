'''Создание связи python с интернетом.
Окна будут оставться открытыми при вызове нового окна.
Отрытие изображений по тегам и без них'''


from tkinter import *
from tkinter import ttk         # библиотека улучшенных виджетов
from PIL import Image, ImageTk  # библиотека для работы с картинками
import requests              # библиотека для обеспечения связи python с интернетом
from io import BytesIO      # библиотека io для ввода и вывода информации
# BytesIO для преобразования информации из десятичной системы в изображение

Allowed_tags = ['sleep', 'jump', 'fight', 'black', 'white', 'bengal', 'siamese', 'cute']  #создаём список для кнопки



def load_image(url):
    try:
        response = requests.get(url)   # делаем запрос по ссылке url и положим в response
        response.raise_for_status()     # обрабока исключений
        image_data = BytesIO(response.content) # сама картинка будет обработана с помощью BytesIO
        img = Image.open(image_data)        # открываем изображение с помощью библиотеки PIL и кладём в img(локал.перем.)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)  # размещаем изображение  в окно  размером (600x480),
        # которое прописываем кортежем  # способ позволяет не уменьшать качество картинки, когда мы изменяем размер
        return ImageTk.PhotoImage(img)  # функция вернёт картинку и положит в другой img, которое прописано в window
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# def set_image():     # функция для работы кнопки
#     img = load_image(url)
#
#     if img:
#         label.config(image=img)
#         label.image = img

def open_new_window():     # функция для работы кнопки
    # tag = tag_entry.get()  # получаем, что ввёл в эту строчку пользователь (загрузка по тегам)
    tag = tag_combobox.get() # при созании кнопки выбора по тегу переписываем верхнюю команду на эту
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"  # такой будет url_если tag не заполнен
                # такой будет url_tag после ввода тега
    img = load_image(url_tag)

    if img:
        new_window = Toplevel() #создание нового окна с возможностью открытия нового изображения без закрытия раннее открытого
        new_window.title("Картинка с котиками")
        new_window.geometry('600x480')
        label = Label(new_window, image=img)
        label.pack()
        label.image = img





def exit():
    window.destroy()



window = Tk()
window.title('Cats')
window.geometry('600x520')

# tag_entry = Entry()   # создаём поле ввода загрузки по тегам
# tag_entry.pack()  # после создания поля ввода Combobox это окно ввода больше не нужно

load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()



# update_button = Button(text='Обновить', command=set_image)  # создаём кнопку для перезапуска программы,
# update_button.pack()                                       # чтобы не перезапускать в консоле

menu_bar = Menu(window)     # создаём меню вместо кнопки "Обновить" с использованием раннее созанной функции def set_image()
window.config(menu=menu_bar)  # в окне window появилась меню

file_menu = Menu(menu_bar, tearoff=0)               # чтобы меню не отклеивалась
menu_bar.add_cascade(label='Файл', menu=file_menu)  # последующие кнопки меню будут появляться каскадом при клике на Файл
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)


url = "https://cataas.com/cat"

tag_label = Label(text='Выбери тег')    # создаём метку с выпадающими тегами по списку
tag_label.pack()

tag_combobox = ttk.Combobox(values= Allowed_tags)  # присваиваем значение = зазрешённые теги,
tag_combobox.pack()         # Combobox виджет        которое создадим в начале программы


# img = load_image(url)    # эти строчки переносим в функцию для работы кнопки def set_image()
#
#
# if img:
#     label.config(image=img)  # устанавливаем картинку на метку
#     label.image = img    # это нужно для того, чтобы сборщика нашу картинку не удалил



window.mainloop()