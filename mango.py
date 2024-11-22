import tkinter as tk

# Создаем главное окно
window = tk.Tk()
window.title("Калькулятор")

# Поле ввода
entry = tk.Entry(window, width=20, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Функция для обработки кнопок
def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Кнопки калькулятора
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Создание кнопок
row = 1
col = 0
for button_text in buttons:
    btn = tk.Button(
        window, text=button_text, width=5, height=2, 
        font=("Arial", 14), command=lambda text=button_text: on_click(text)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Запуск приложения
window.mainloop()
