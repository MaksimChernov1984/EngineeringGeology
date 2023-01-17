import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        f = '#fff'  # цвет текста
        b = '#002'  # цвет фона окна
        fnt = 10  # размер шрифта
        p_x = 3  # интервал по х
        p_y = 3  # интервал по у
        self.configure(bg='#002')

        lbl = tk.Label(self, font=fnt, fg=f, bg=b)
        lbl.configure(text='Вас приветствует компания "ПОЛЕТЕЛИ ПРИЛЕТЕЛИ"!')
        lbl.grid(column=0, columnspan=2, row=0, padx=p_x, pady=2*p_y)

        # цель назначения
        lbl = tk.Label(self, font=fnt, fg=f, bg=b)
        lbl.configure(text='Куда летим?')
        lbl.grid(column=0, row=1, padx=p_x, pady=p_y, stick="e")

        self.destination = ttk.Combobox(self, width=11)
        self.destination['values'] = ('(выберите)', 'Луна', 'Меркурий', 'Венера', 'Марс', 'Церера',
                                      'Ганимед', 'Ио', 'Калисто', 'Европа', 'Титан', 'Титания', 'Тритон', 'Плутон',
                                      'Эрида')
        self.destination.current(0)
        self.destination.grid(column=1, row=1, padx=p_x, pady=p_y)
        self.destination.focus()

        # количество пассажиров
        lbl = tk.Label(self, font=fnt, fg=f, bg=b)
        lbl.configure(text='Сколько человек? (максимум 20)')
        lbl.grid(column=0, row=2, padx=p_x, pady=p_y, stick="e")

        self.passengers = ttk.Spinbox(self, from_=1, to=20, width=10)
        self.passengers.grid(column=1, row=2, padx=p_x, pady=p_y)
        self.passengers.set('1')

        # количество тонн груза
        lbl = tk.Label(self, font=fnt, fg=f, bg=b)
        lbl.configure(text='Сколько тонн груза? (максимум 100)')
        lbl.grid(column=0, row=3, padx=p_x, pady=p_y, stick="e")

        self.cargo = ttk.Spinbox(self, from_=1, to=100, width=11)
        self.cargo.grid(column=1, row=3, padx=p_x, pady=p_y)
        self.cargo.set('1')

        # выбор тарифа
        lbl = tk.Label(self, font=fnt, fg=f, bg=b)
        lbl.configure(text='Тариф')
        lbl.grid(column=0, row=4, padx=p_x, pady=p_y, stick="e")

        self.tariff = ttk.Combobox(self, width=11)
        self.tariff['values'] = ('(выберите)', 'простой', 'быстрый', 'супербыстрый')
        self.tariff.current(0)
        self.tariff.grid(column=1, row=4, padx=p_x, pady=p_y)

        # проверка условий
        btn_check = tk.Button(self, text='Проверить условия', bg='#CD5C5C',
                              activebackground='#A52A2A', fg='#000', command=self.check)
        btn_check.grid(column=0, row=5, padx=p_x, pady=p_y)
        # btn_check.bind('<Return>', check)

        self.resume1 = tk.Label(self, text='Проверка условий.', font=fnt, fg=f, bg=b)
        self.resume1.grid(column=0, row=6, padx=p_x, pady=p_y)

        # стоимость
        btn_price = tk.Button(self, text='Рассчитать стоимость', bg='#CD5C5C',
                              activebackground='#A52A2A', fg='#000', command=self.priced)
        btn_price.grid(column=0, row=7, padx=p_x, pady=p_y)
        # self.btn_price.bind('<Return>', priced)

        self.resume2 = tk.Label(self, text='Проверка стоимости.', font='16', fg=f, bg=b)
        self.resume2.grid(column=0, row=8, padx=p_x, pady=p_y)

        # кнопка Ракета
        btn_open_rocket = tk.Button(self, text='Ракета', command=self.open_rocket,
                                    bg='#CD5C5C', activebackground='#A52A2A')
        btn_open_rocket.grid(column=0, row=9, padx=p_x, pady=2*p_y)

    def check(self):
        self.resume1.config(text='Цель назначения - ' +
                            self.destination.get() + '\nКоличество человек - ' +
                            self.passengers.get() + '\nКоличество груза в тоннах - ' +
                            self.cargo.get() + '\nТариф - ' + self.tariff.get())

    def priced(self):
        # коэффициенты
        p = int(self.passengers.get())  # количество пассажиров
        c = int(self.cargo.get())  # масса груза в тоннах
        rub = 100_000  # рублей за единичный коэффициент

        # коэффициенты цели назначения
        if self.destination.get() == 'Луна':
            d = 1
        elif self.destination.get() == 'Марс':
            d = 2
        elif self.destination.get() == 'Церера':
            d = 2.5
        elif self.destination.get() == ('Ганимед') or ('Ио') or ('Калисто') or ('Европа'):
            d = 3
        elif self.destination.get() == ('Меркурий') or ('Венера') or ('Титан'):
            d = 4
        elif self.destination.get() == 'Титания':
            d = 5
        elif self.destination.get() == 'Тритон':
            d = 6
        elif self.destination.get() == 'Плутон':
            d = 7
        elif self.destination.get() == 'Эрида':
            d = 8

            # коэффициенты тарифа
        if self.tariff.get() == 'простой':
            t = 1
        elif self.tariff.get() == 'быстрый':
            t = 2
        elif self.tariff.get() == 'супербыстрый':
            t = 3

        price = d * p * c * t * rub

        if p <= 20:
            if c <= 100:
                price2 = '{0:,}'.format(price).replace(',', ' ')
            else:
                price2 = 'Слишком много груза.'
        else:
            price2 = 'Слишком много пассажиров.'

        self.resume2.config(text=price2)

    def open_rocket(self):
        Rocket()


class Rocket(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_rocket()
        self.view = app

    def init_rocket(self):
        self.title('Ракета')
        self.geometry('900x600+20+20')
        self.configure(bg='#002')
        self.resizable(False, False)

        f = '#fff'  # цвет текста
        b = '#002'  # цвет фона окна
        fnt = 10  # размер шрифта
        p_x = 3  # интервал по х
        p_y = 3  # интервал по у

        lbl = tk.Label(self, text='Давайте нарисуем ракету!', font=fnt, fg=f, bg=b).place(x=50, y=10)

        # высота конуса
        lbl = tk.Label(self, text='Высота конуса', font=fnt, fg=f, bg=b).place(x=10, y=40)

        self.hh0 = ttk.Entry(self, width=10)
        self.hh0.place(x=250, y=40)
        self.hh0.focus()

        # ширина конуса
        lbl = tk.Label(self, text='Ширина конуса', font=fnt, fg=f, bg=b).place(x=10, y=70)

        self.ww0 = ttk.Entry(self, width=10)
        self.ww0.place(x=250, y=70)

        # высота ступени 4
        lbl = tk.Label(self, text='Высота четвёртой ступени', font=fnt, fg=f, bg=b).place(x=10, y=100)

        self.hh4 = ttk.Entry(self, width=10)
        self.hh4.place(x=250, y=100)

        # высота ступени 3
        lbl = tk.Label(self, text='Высота третьей ступени', font=fnt, fg=f, bg=b).place(x=10, y=130)

        self.hh3 = ttk.Entry(self, width=10)
        self.hh3.place(x=250, y=130)

        # высота ступени 2
        lbl = tk.Label(self, text='Высота второй ступени', font=fnt, fg=f, bg=b).place(x=10, y=160)

        self.hh2 = ttk.Entry(self, width=10)
        self.hh2.place(x=250, y=160)

        # высота ступени 1
        lbl = tk.Label(self, text='Высота первой ступени', font=fnt, fg=f, bg=b).place(x=10, y=190)

        self.hh1 = ttk.Entry(self, width=10)
        self.hh1.place(x=250, y=190)

        # высота боковых ускорителей
        lbl = tk.Label(self, text='Высота боковых ускорителей', font=fnt, fg=f, bg=b).place(x=10, y=220)

        self.hh_jet1 = ttk.Entry(self, width=10)
        self.hh_jet1.place(x=250, y=220)

        # ширина боковых ускорителей
        lbl = tk.Label(self, text='Ширина боковых ускорителей', font=fnt, fg=f, bg=b).place(x=10, y=250)

        self.ww_jet1 = ttk.Entry(self, width=10)
        self.ww_jet1.place(x=250, y=250)

        # цвет ракеты
        lbl = tk.Label(self, text='Цвет ракеты', font=fnt, fg=f, bg=b).place(x=10, y=280)

        self.c_rocket = ttk.Entry(self, width=10)
        self.c_rocket.place(x=250, y=280)

        # цвет космоса
        lbl = tk.Label(self, text='Цвет космоса', font=fnt, fg=f, bg=b).place(x=10, y=310)

        self.c_space = ttk.Entry(self, width=10)
        self.c_space.place(x=250, y=310)

        # надпись
        lbl = tk.Label(self, text='Бортовая надпись', font=fnt, fg=f, bg=b).place(x=10, y=340)

        self.rocket_text = ttk.Entry(self, width=10)
        self.rocket_text.place(x=250, y=340)

        btn = tk.Button(self, text='Рисуем ракету', bg='#CD5C5C', activebackground='#A52A2A',
                        fg='#000', command=self.rocket)
        btn.place(x=20, y=450)

        btn_cancel_rocket = tk.Button(self, text='Вернуться к полёту', command=self.destroy,
                                      bg='#CD5C5C', activebackground='#A52A2A')
        btn_cancel_rocket.place(x=20, y=500)

    def rocket(self):
        # Rocket()
        h0 = int(self.hh0.get())  # высота конуса
        w0 = int(self.ww0.get())  # ширина конуса
        h4 = int(self.hh4.get())  # высота ступени 3
        h3 = int(self.hh3.get())  # высота ступени 2
        h2 = int(self.hh2.get())  # высота ступени 2
        h1 = int(self.hh1.get())  # высота ступени 1
        h_jet1 = int(self.hh_jet1.get())  # высота боковых ускорителей
        w_jet1 = int(self.ww_jet1.get())  # ширина боковых ускорителей
        cr = str(self.c_rocket.get())  # цвет ракеты
        color_rocket = '#' + cr + ''
        cs = str(self.c_space.get())  # цвет космоса
        color_space = '#' + cs + ''
        w_canvas = 700    # ширина холста
        h_canvas = 600  # высота холста
        x = 250  # координата вершины конуса по Х
        y = 50  # координата вершины конуса по У

        # лист
        cv = tk.Canvas(self, width=w_canvas, height=h_canvas, bg=color_space)
        cv.place(x=400, y=0)

        # конус
        cv.create_polygon(x, y,
                          x + 0.5 * w0, y + h0,
                          x - 0.5 * w0, y + h0,
                          fill=color_rocket, width=1, outline='#000')

        # иллюминатор
        cv.create_oval(x - 0.05 * w0, y + 0.6 * h0,
                       x + 0.05 * w0, y + 0.6 * h0 + 0.1 * w0,
                       fill=color_space, width=1, outline='#000')

        # ступень 4
        cv.create_polygon(x + 0.5 * w0, y + h0,
                          x + 0.5 * w0, y + h0 + 0.3 * h4,
                          x + 0.6 * w0, y + h0 + 0.4 * h4,
                          x + 0.6 * w0, y + h0 + 0.5 * h4,
                          x + 0.5 * w0, y + h0 + 0.5 * h4,
                          x + 0.5 * w0, y + h0 + h4,
                          x - 0.5 * w0, y + h0 + h4,
                          x - 0.5 * w0, y + h0 + 0.5 * h4,
                          x - 0.6 * w0, y + h0 + 0.5 * h4,
                          x - 0.6 * w0, y + h0 + 0.4 * h4,
                          x - 0.5 * w0, y + h0 + 0.3 * h4,
                          x - 0.5 * w0, y + h0,
                          x - 0.5 * w0, y + h0,
                          fill=color_rocket, width=1, outline='#000')

        # ступень 3
        cv.create_polygon(x + 0.5 * w0, y + h0 + h4,
                          x + 0.6 * w0, y + h0 + h4 + 0.1 * h3,
                          x + 0.6 * w0, y + h0 + h4 + h3,
                          x - 0.6 * w0, y + h0 + h4 + h3,
                          x - 0.6 * w0, y + h0 + h4 + 0.1 * h3,
                          x - 0.5 * w0, y + h0 + h4,
                          fill=color_rocket, width=1, outline='#000')

        # ступень 2
        cv.create_polygon(x + 0.6 * w0, y + h0 + h4 + h3,
                          x + 0.7 * w0, y + h0 + h4 + h3 + 0.1 * h2,
                          x + 0.7 * w0, y + h0 + h4 + h3 + h2,
                          x - 0.7 * w0, y + h0 + h4 + h3 + h2,
                          x - 0.7 * w0, y + h0 + h4 + h3 + 0.1 * h2,
                          x - 0.6 * w0, y + h0 + h4 + h3,
                          fill=color_rocket, width=1, outline='#000')

        # ступень 1
        cv.create_polygon(x + 0.7 * w0, y + h0 + h4 + h3 + h2,
                          x + 0.8 * w0, y + h0 + h4 + h3 + h2 + 0.1 * h1,
                          x + 0.8 * w0, y + h0 + h4 + h3 + h2 + h1,
                          x + 0.6 * w0, y + h0 + h4 + h3 + h2 + h1,

                          x + 0.7 * w0, y + h0 + h4 + h3 + h2 + 1.1 * h1,
                          x + 0.75 * w0, y + h0 + h4 + h3 + h2 + 1.2 * h1,
                          x + 0.3 * w0, y + h0 + h4 + h3 + h2 + 1.2 * h1,
                          x + 0.35 * w0, y + h0 + h4 + h3 + h2 + 1.1 * h1,

                          x + 0.45 * w0, y + h0 + h4 + h3 + h2 + h1,
                          x - 0.45 * w0, y + h0 + h4 + h3 + h2 + h1,

                          x - 0.35 * w0, y + h0 + h4 + h3 + h2 + 1.1 * h1,
                          x - 0.3 * w0, y + h0 + h4 + h3 + h2 + 1.2 * h1,
                          x - 0.75 * w0, y + h0 + h4 + h3 + h2 + 1.2 * h1,
                          x - 0.7 * w0, y + h0 + h4 + h3 + h2 + 1.1 * h1,

                          x - 0.6 * w0, y + h0 + h4 + h3 + h2 + h1,
                          x - 0.8 * w0, y + h0 + h4 + h3 + h2 + h1,
                          x - 0.8 * w0, y + h0 + h4 + h3 + h2 + 0.1 * h1,
                          x - 0.7 * w0, y + h0 + h4 + h3 + h2,
                          fill=color_rocket, width=1, outline='#000')

        # боковой ускоритель левый
        cv.create_polygon(x - 0.8 * w0 - 0.5 * w_jet1, y + h0 + h4 + h3 + h2 + h1 - h_jet1,
                          x - 0.8 * w0, y + h0 + h4 + h3 + h2 + h1 - h_jet1 + 0.5 * w_jet1,
                          x - 0.8 * w0, y + h0 + h4 + h3 + h2 + h1,
                          x - 0.8 * w0 - 0.4 * w_jet1, y + h0 + h4 + h3 + h2 + h1,
                          x - 0.8 * w0 - 0.25 * w_jet1, y + h0 + h4 + h3 + h2 + 1.1*h1,
                          x - 0.8 * w0 - 0.2 * w_jet1, y + h0 + h4 + h3 + h2 + 1.2 * h1,
                          x - 0.8 * w0 - 0.8 * w_jet1, y + h0 + h4 + h3 + h2 + 1.2 * h1,
                          x - 0.8 * w0 - 0.75 * w_jet1, y + h0 + h4 + h3 + h2 + 1.1 * h1,
                          x - 0.8 * w0 - 0.6 * w_jet1, y + h0 + h4 + h3 + h2 + h1,
                          x - 0.8 * w0 - w_jet1, y + h0 + h4 + h3 + h2 + h1,
                          x - 0.8 * w0 - w_jet1, y + h0 + h4 + h3 + h2 + h1 - h_jet1 + 0.5 * w_jet1,
                          fill=color_rocket, width=1, outline='#000')

        # боковой ускоритель правый
        cv.create_polygon(x + 0.8 * w0 + 0.5 * w_jet1, y + h0 + h4 + h3 + h2 + h1 - h_jet1,
                          x + 0.8 * w0, y + h0 + h4 + h3 + h2 + h1 - h_jet1 + 0.5 * w_jet1,
                          x + 0.8 * w0, y + h0 + h4 + h3 + h2 + h1,
                          x + 0.8 * w0 + 0.4 * w_jet1, y + h0 + h4 + h3 + h2 + h1,
                          x + 0.8 * w0 + 0.25 * w_jet1, y + h0 + h4 + h3 + h2 + 1.1*h1,
                          x + 0.8 * w0 + 0.2 * w_jet1, y + h0 + h4 + h3 + h2 + 1.2 * h1,
                          x + 0.8 * w0 + 0.8 * w_jet1, y + h0 + h4 + h3 + h2 + 1.2 * h1,
                          x + 0.8 * w0 + 0.75 * w_jet1, y + h0 + h4 + h3 + h2 + 1.1 * h1,
                          x + 0.8 * w0 + 0.6 * w_jet1, y + h0 + h4 + h3 + h2 + h1,
                          x + 0.8 * w0 + w_jet1, y + h0 + h4 + h3 + h2 + h1,
                          x + 0.8 * w0 + w_jet1, y + h0 + h4 + h3 + h2 + h1 - h_jet1 + 0.5 * w_jet1,
                          fill=color_rocket, width=1, outline='#000')

        cv.create_text(x, y + h0 + 0.5 * h4, text=self.rocket_text.get(), fill=color_space)


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Полетели Прилетели')
    root.geometry('900x600+20+20')
    root['bg'] = '#002'
    root.resizable(False, False)
    root.mainloop()
