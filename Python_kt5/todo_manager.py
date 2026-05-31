import tkinter as tk
from datetime import datetime, date, timedelta

# Создаём окно
window = tk.Tk()
window.title("Напоминалка")
window.geometry("600x450")
window.configure(bg='black')

# Заголовки
tk.Label(window, text="Лист роботяги", font=('Arial', 16, 'bold'), fg='white', bg='black').pack(anchor='w', padx=20, pady=(20, 10))
tk.Label(window, text="Задачи", font=('Arial', 13, 'bold'), fg='white', bg='black').pack(anchor='w', padx=20, pady=(0, 10))

# Читаем задачи из файла
today = date.today()

with open('tasks.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()

        if '|' not in line:
            continue

        if '67' in line:
            continue

        if line:
            name, date_str = line.split('|')
            task_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            
            # Определяем цвет и текст
            if task_date < today:
                color = '#ff4444'  # красный
                days = (today - task_date).days
                text = f"- Прошло {days} дней от {name}"
                    
            elif task_date == today:
                color = '#ff8800'  # оранжевый
                text = f"- Прямо щас происходит {name}"
                
            else:
                color = 'white'  # белый
                days = (task_date - today).days
                text = f"- Осталось {days} дней до {name}"
            
            # Показываем задачу
            tk.Label(window, text=text, font=('Arial', 11), fg=color, bg='black').pack(anchor='w', padx=20, pady=2)

# Запускаем
window.mainloop()