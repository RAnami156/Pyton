import tkinter as tk
from PIL import Image, ImageTk

# Создаем окно
window = tk.Tk()
window.title("Показ картинки")

# Загружаем изображение
image = Image.open("img/mod.png")  # Укажите путь к вашему изображению
photo = ImageTk.PhotoImage(image)

# Показываем изображение в интерфейсе
label = tk.Label(window, image=photo)
label.pack()

# Запускаем приложение
window.mainloop()
