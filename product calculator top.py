import tkinter as tk
from tkinter import ttk, messagebox

# Определяем возможные материалы
material_dict = {
    "Скамейка": "Дерево",
    "Стул": "Дерево или Металл",
    "Кровать": "Дерево",
    "Тумбочка": "Дерево и Металл",
    "Стеллаж": "Металл и Дерево",
    "Стол": "Дерево"
}

def generate_specification(product_name, length, width, height, number_of_boards, number_of_screws):
    material = material_dict.get(product_name, "Неизвестный материал")  # Получаем материал из словаря
    
    specification = {
        'Название': product_name,
        'Длина (см)': length,
        'Ширина (см)': width,
        'Высота (см)': height,
        'Материал': material,
        'Количество досок спинки': number_of_boards,
        'Количество крепежей': number_of_screws
    }
    return specification

def count_materials(specification):
    """Подсчитать количество материалов в зависимости от типа мебели."""
    if specification["Название"] == 'Скамейка':
        return (f"Количество досок: 3(сиденье) + 4(ножки) + 4(спинка) = 11"
                f"Количество саморезов: 4(сиденье) + 2(ножки) + 3(спинка) = 15")
    elif specification["Название"] == 'Стол':
        return (f"Количество досок: 4(столешница) + 4(ножки) = 8"
                f"Количество саморезов: 6(столешница) + 8(ножки) = 14 \n")
    elif specification["Название"] == 'Кровать':
        return (f"Количество досок: 4(рама) + 4(ножки) + 10(поперечены) = 18"
                f"Количество поперечен: 10"
                f"Количество саморезов: 8(рама) + 8(ножки) + 20(поперечены) = 36")
    elif specification["Название"] == 'Тумбочка':
        return (f"Количество ящиков: 2"
                f"Количество досок: 2(поверхность) + 4(корпус) + 4(ящик) + 2(ножки) = 12"
                f"Количество саморезов: 6(верх) + 4(корпус) + 4(ящик) + 4(ножки) = 18")
    elif specification["Название"] == 'Стеллаж':
        return (f"Количество полок: 5"
                f"Количество досок: 2(боковые панели) + 5(полки) + 2(задняя крестовина) = 9"
                f"Количество саморезов: 6(полки) + 8(боковые панели) + 6(задняя крестовина) = 20")
    elif specification["Название"] == 'Стул':
        return (f"Количество ножек: 4"
                f"Количество досок: 2(сиденье) + 4(ножки) + 2(спинка) + 2(подлокотники) = 10"
                f"Количество саморезов: 6(сиденье) + 8(ножки) + 4(спинка) + 4(подлокотники) = 22")
    return ""

def save_to_file(specification, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"Создана мебель:\nТип: {specification['Название']}\n")
        f.write(f"Размеры: {specification['Длина (см)']} x {specification['Ширина (см)']} x {specification['Высота (см)']} см.\n")
        f.write(f"Материал: {specification['Материал']}\n")
        f.write(f"Количество досок: {specification['Количество досок спинки']}\n")
        f.write(f"Количество крепежей: {specification['Количество крепежей']}\n")
        f.write(count_materials(specification))

def submit():
    furniture_type = option_var.get()
    length = length_entry.get()
    width = width_entry.get()
    height = height_entry.get()
    seat_height = seat_height_entry.get() if furniture_type in ["Скамейка", "Стул"] else None

    if not all([length, width, height]) or (furniture_type in ["Скамейка", "Стул"] and not seat_height):
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
        return

    try:
        length = int(length)
        width = int(width)
        height = int(height)
        if furniture_type in ["Скамейка", "Стул"]:
            seat_height = int(seat_height)
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения.")
        return
    
    # Пример для определенных параметров (доски и крепеж)
    number_of_boards = 0
    number_of_screws = 0
    if furniture_type == "Скамейка":
        number_of_boards = 3
        number_of_screws = 12
    elif furniture_type == "Стол":
        number_of_boards = 4
        number_of_screws = 8
    elif furniture_type == "Кровать":
        number_of_boards = 4
        number_of_screws = 2
    elif furniture_type == "Тумбочка":
        number_of_boards = 2
        number_of_screws = 8
    elif furniture_type == "Стеллаж":
        number_of_boards = 5
        number_of_screws = 10

    specification = generate_specification(furniture_type, length, width, height, number_of_boards, number_of_screws)

    result_message = (f"Создана мебель:\nТип: {specification['Название']}\n" +
                      f"Размеры: {specification['Длина (см)']} x {specification['Ширина (см)']} x {specification['Высота (см)']} см.\n" +
                      f"Материал: {specification['Материал']}\n" +
                      f"Количество досок спинки: {specification['Количество досок спинки']}\n" +
                      f"Количество крепежей: \n" +
                      count_materials(specification))

    messagebox.showinfo("Результат", result_message)

    # Создаем чертеж в зависимости от типа мебели
    if furniture_type == 'Стол':
        FurnitureDrawer(tk.Tk(), "Стол")
    elif furniture_type == 'Стул':
        FurnitureDrawer(tk.Tk(), "Стул")
    elif furniture_type == 'Кровать':
        FurnitureDrawer(tk.Tk(), "Кровать")
    elif furniture_type == 'Тумбочка':
        FurnitureDrawer(tk.Tk(), "Тумбочка")

class FurnitureDrawer:
    def __init__(self, root, furniture_type):
        self.root = root
        self.root.title(f"2D Модель Изделия - {furniture_type}")

        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()

        if furniture_type == "Стол":
            self.draw_table()
        elif furniture_type == "Стул":
            self.draw_chair()
        elif furniture_type == "Кровать":
            self.draw_bed()
        elif furniture_type == "Тумбочка":
            self.draw_bedside()
        elif furniture_type == "Стеллаж":
            self.draw_rack()

    def draw_table(self):
        self.canvas.create_rectangle(200, 150, 600, 200, outline="black", fill="saddlebrown") # рисует столешницу стола
        self.canvas.create_rectangle(220, 200, 270, 350, outline="black", fill="saddlebrown") # рисует ножку стола №1
        self.canvas.create_rectangle(530, 200, 580, 350, outline="black", fill="saddlebrown") # рисует ножку стола №2
        self.canvas.create_line(200, 150, 600, 150, fill="black", width=3) # рисует верхнюю грань стола
        self.canvas.create_line(200, 200, 600, 200, fill="black", width=3) # рисует нижнюю грань стола

    def draw_chair(self):
        self.canvas.create_rectangle(200, 150, 600, 200, outline="black", fill="saddlebrown") # рисует основание стула
        self.canvas.create_rectangle(220, 200, 270, 350, outline="black", fill="saddlebrown") # рисует ножку стула №1
        self.canvas.create_rectangle(530, 200, 580, 350, outline="black", fill="saddlebrown") # рисует ножку стула №2
        self.canvas.create_line(300, 200, 500, 200, fill="black", width=3) # рисует спинку стула
        self.canvas.create_line(300, 120, 500, 120, fill="black", width=3) # рисует верхнюю часть спинки стула
        self.canvas.create_line(300, 200, 300, 120, fill="black", width=3) # рисует левую часть спинки стула
        self.canvas.create_line(500, 200, 500, 120, fill="black", width=3) # рисует правую сторону спинки стула

    def draw_bed(self):
        self.canvas.create_rectangle(200, 300, 600, 500, outline="black", fill="saddlebrown") # рисует основание кровати
        self.canvas.create_rectangle(200, 260, 600, 300, outline="black", fill="saddlebrown") # рисует верхнюю часть матраса
        self.canvas.create_rectangle(200, 220, 600, 260, outline="black", fill="saddlebrown") # рисует подушку на кровати
        self.canvas.create_rectangle(200, 500, 220, 580, outline="black", fill="saddlebrown") # рисует ножку кровати №1
        self.canvas.create_rectangle(580, 500, 600, 580, outline="black", fill="saddlebrown") # рисует ножку кровати №2

    def draw_bedside(self):
        self.canvas.create_rectangle(300, 250, 500, 400, outline="black", fill="saddlebrown") # рисует тумбочку
        self.canvas.create_rectangle(300, 270, 500, 330, outline="black", fill="saddlebrown") # рисует верхнюю часть тумбочки
        self.canvas.create_rectangle(300, 330, 500, 390, outline="black", fill="lightgray") # рисует ящик тумбочки
        self.canvas.create_rectangle(400, 360, 420, 310, outline="black", fill="darkgray") # рисует ручку ящика №1
        self.canvas.create_rectangle(400, 360, 420, 370, outline="black", fill="darkgray") # рисует ручку ящика №2
        self.canvas.create_rectangle(300, 400, 320, 440, outline="black", fill="saddlebrown") # рисует ножку №"1
        self.canvas.create_rectangle(480, 400, 500, 440, outline="black", fill="saddlebrown") # рисует ножку №2

    def draw_rack(self):
        self.canvas.create_rectangle(150, 100, 650, 500, outline="black", fill="saddlebrown") # рисование левого бока
        self.canvas.create_rectangle(640, 100, 650, 500, outline="black", fill="saddlebrown") # рисование правого бока
        self.canvas.create_rectangle(200, 250, 600, 300, outline="black", fill="saddlebrown") # рисование полки


# Основное окно
root = tk.Tk()
root.title("Калькулятор мебели")
root.geometry("700x500")

# Виджеты для выбора мебели
option_var = tk.StringVar()
option_menu = ttk.Combobox(root, textvariable=option_var, values=list(material_dict.keys()))
option_menu.pack(pady=10)

# Поля ввода для размеров
length_label = tk.Label(root, text="Длина (см):")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

width_label = tk.Label(root, text="Ширина (см):")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

height_label = tk.Label(root, text="Высота (см):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Поле ввода для высоты сиденья (опционально)
seat_height_label = tk.Label(root, text="Высота сиденья (см):")
seat_height_entry = tk.Entry(root)

# Обновляем видимость высоты сиденья в зависимости от выбранного типа мебели
def update_seat_height_entry(*args):
    furniture_type = option_var.get()
    if furniture_type in ["Скамейка", "Стул"]:
        seat_height_label.pack()
        seat_height_entry.pack()
    else:
        seat_height_label.pack_forget()
        seat_height_entry.pack_forget()

option_var.trace("w", update_seat_height_entry)

# Кнопка отправки
submit_button = tk.Button(root, text="Создать вариацию", command=submit)
submit_button.pack(pady=20)

# Запуск основного цикла
root.mainloop()
