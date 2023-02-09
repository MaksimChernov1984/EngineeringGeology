import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()


    def init_main(self):
        toolbar = tk.Frame(bg='#FFE4C4')
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_log = tk.Button(toolbar, text='Добавить', command=self.open_log,
                                 bg='#F4A460', activebackground='#FF6347', bd=0)
        btn_open_log.pack(side=tk.LEFT)

        btn_update_log = tk.Button(toolbar, text='Редактировать', command=self.update_log,
                                 bg='#F4A460', activebackground='#FF6347', bd=0)
        btn_update_log.pack(side=tk.LEFT)

        btn_delete_log = tk.Button(toolbar, text='Удалить', command=self.delete_records,
                                   bg='#F4A460', activebackground='#FF6347', bd=0)
        btn_delete_log.pack(side=tk.LEFT)

        btn_search = tk.Button(toolbar, text='Поиск', command=self.open_search,
                                  bg='#F4A460', activebackground='#FF6347', bd=0)
        btn_search.pack(side=tk.LEFT)

        btn_refresh = tk.Button(toolbar, text='Обновить', command=self.view_records,
                               bg='#F4A460', activebackground='#FF6347', bd=0)
        btn_refresh.pack(side=tk.LEFT)

        # позже добавлю кнопку с чертежём

        self.tree = ttk.Treeview(self, columns=('ID', 'obj_nm', 'bore_nm', 'bore_date', 'bore_abs', 'bore_depth', 'layer_roof', 
                                'layer_descr', 'sample_type', 'sample_depth', 'layer_base'), height=15, show='headings')
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('obj_nm', width=65, anchor=tk.CENTER)
        self.tree.column('bore_nm', width=65, anchor=tk.CENTER)
        self.tree.column('bore_date', width=85, anchor=tk.CENTER)
        self.tree.column('bore_abs', width=65, anchor=tk.CENTER)
        self.tree.column('bore_depth', width=70, anchor=tk.CENTER)
        self.tree.column('layer_roof', width=60, anchor=tk.CENTER)
        self.tree.column('layer_descr', width=345, anchor=tk.W)
        self.tree.column('sample_type', width=105, anchor=tk.CENTER)
        self.tree.column('sample_depth', width=110, anchor=tk.CENTER)
        self.tree.column('layer_base', width=75, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('obj_nm', text='N объек.')
        self.tree.heading('bore_nm', text='N скв.')
        self.tree.heading('bore_date', text='Дата')
        self.tree.heading('bore_abs', text='Абс.отм.')
        self.tree.heading('bore_depth', text='Глуб.скв.')
        self.tree.heading('layer_roof', text='Кровля ИГЭ')
        self.tree.heading('layer_descr', text='Описание ИГЭ')
        self.tree.heading('sample_type', text='Вид образца')
        self.tree.heading('sample_depth', text='Глуб.обр.')
        self.tree.heading('layer_base', text='Подошва ИГЭ')

        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)


    # добавить записи
    def records(self, obj_nm, bore_nm, bore_date, bore_abs, bore_depth, layer_roof, layer_descr, sample_type, sample_depth, 
                layer_base):
        self.db.insert_data(obj_nm, bore_nm, bore_date, bore_abs, bore_depth, layer_roof, layer_descr, sample_type, sample_depth, 
                            layer_base)
        self.view_records()


    # редактировать записи
    def update_records(self, obj_nm, bore_nm, bore_date, bore_abs, bore_depth, layer_roof, layer_descr, sample_type, sample_depth, 
                       layer_base):
        self.db.c.execute(
            '''UPDATE borelog SET obj_nm=?, bore_nm=?, bore_date=?, bore_abs=?, bore_depth=?, layer_roof=?, 
            layer_descr=?, sample_type=?, sample_depth=?, layer_base=? WHERE ID=?''', 
            (obj_nm, bore_nm, bore_date, bore_abs, bore_depth, layer_roof, layer_descr, sample_type, sample_depth, layer_base,
            self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()


    # смотреть все записи
    def view_records(self):
        self.db.c.execute('''SELECT * FROM borelog''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]


    # удалить записи
    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM borelog WHERE id=?''',
                                  (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()


    def search_records(self, bore_nm):
        bore_nm = (bore_nm,)  # если надо поиск из любой позиции (напр., в центре слова), то (%+bore+%,)
        self.db.c.execute('''SELECT * FROM borelog WHERE bore_nm LIKE ? ORDER BY layer_roof''', bore_nm)
        [self.tree.delete(i) for i in self.tree.get_children()]  # проходим циклом всю таблицу и очищаем её
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]  # добавляем данные


    # открыть журнал
    def open_log(self):
        Log()


    # редактировать записи
    def update_log(self):
        Update()


    # удалить записи
    def delete_log(self):
        Update()


    # поиск
    def open_search(self):
        Search()

    # позже будет чертёж


# окно Добавление
class Log(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_log()
        self.view = app


    def init_log(self):
        self.title('Добавление элемента')
        self.geometry('800x400+150+150')
        self.configure(bg='#FFE4C4')
        self.resizable(False, False)

        toolbar = tk.Frame(bg='#FFE4C4')
        toolbar.pack(side=tk.TOP, fill=tk.X)

        label_obj_nm = tk.Label(self, text='№ объекта', bg='#FFE4C4').place(x=5, y=5)
        label_bore_nm = tk.Label(self, text='№ скв.', bg='#FFE4C4').place(x=5, y=35)
        label_bore_date = tk.Label(self, text='Дата проходки', bg='#FFE4C4').place(x=5, y=65)
        label_bore_abs = tk.Label(self, text='Абс.отметка', bg='#FFE4C4').place(x=5, y=95)
        label_bore_depth = tk.Label(self, text='Глуб.скв.', bg='#FFE4C4').place(x=5, y=125)
        label_layer_base = tk.Label(self, text='Кровля ИГЭ', bg='#FFE4C4').place(x=5, y=155)
        label_layer_descr = tk.Label(self, text='Описание ИГЭ', bg='#FFE4C4').place(x=5, y=185)
        label_sample_type = tk.Label(self, text='Вид образца', bg='#FFE4C4').place(x=5, y=215)
        label_sample_depth = tk.Label(self, text='глубина образца', bg='#FFE4C4').place(x=5, y=245)
        label_layer_base = tk.Label(self, text='Подошва ИГЭ', bg='#FFE4C4').place(x=5, y=275)

        self.entry_obj_nm = ttk.Entry(self, width=15)
        self.entry_obj_nm.place(x=150, y=5)
        
        self.entry_bore_nm = ttk.Entry(self, width=15)
        self.entry_bore_nm.place(x=150, y=35)

        self.entry_bore_date = ttk.Entry(self, width=15)
        self.entry_bore_date.place(x=150, y=65)

        self.entry_bore_abs = ttk.Entry(self, width=15)
        self.entry_bore_abs.place(x=150, y=95)

        self.entry_bore_depth = ttk.Entry(self, width=15)
        self.entry_bore_depth.place(x=150, y=125)

        self.entry_layer_roof = ttk.Entry(self, width=15)
        self.entry_layer_roof.place(x=150, y=155)

        self.entry_layer_descr = ttk.Entry(self, width=80)
        self.entry_layer_descr.place(x=150, y=185)

        self.combobox_sample_type = ttk.Combobox(self, width=15, values=[u'Монолит', u'Нарушенный', u'Коррозия', u'Вода'])
        self.combobox_sample_type.place(x=150, y=215)
        self.combobox_sample_type.current(0)

        self.entry_sample_depth = ttk.Entry(self, width=15)
        self.entry_sample_depth.place(x=150, y=245)

        self.entry_layer_base = ttk.Entry(self, width=15)
        self.entry_layer_base.place(x=150, y=275)


        self.btn_ok_log = tk.Button(self, text='Добавить',bg='#F4A460', activebackground='#FF6347', bd=0)
        self.btn_ok_log.bind('<Button-1>', lambda event: self.view.records(self.entry_obj_nm.get(),
                                                                           self.entry_bore_nm.get(),
                                                                           self.entry_bore_date.get(),
                                                                           self.entry_bore_abs.get(),
                                                                           self.entry_bore_depth.get(),
                                                                           self.entry_layer_roof.get(),
                                                                           self.entry_layer_descr.get(),
                                                                           self.combobox_sample_type.get(),
                                                                           self.entry_sample_depth.get(),
                                                                           self.entry_layer_base.get()))
        self.btn_ok_log.bind('<Return>', lambda event: self.view.records(self.entry_obj_nm.get(),      
                                                                         self.entry_bore_nm.get(),
                                                                         self.entry_bore_date.get(),
                                                                         self.entry_bore_abs.get(),
                                                                         self.entry_bore_depth.get(),
                                                                         self.entry_layer_roof.get(),
                                                                         self.entry_layer_descr.get(),
                                                                         self.combobox_sample_type.get(),
                                                                         self.entry_sample_depth.get(),
                                                                         self.entry_layer_base.get()))
        self.btn_ok_log.place(x=50, y=305)


        btn_cancel_log = tk.Button(self, text='Завершить', command=self.destroy,
                                   bg='#F4A460', activebackground='#FF6347', bd=0)
        btn_cancel_log.place(x=50, y=345)

        self.grab_set()
        self.focus_set()


# редактирование
class Update(Log):
    def __init__(self):
        super().__init__()
        self.init_edit()  # чтобы отображалось
        self.view = app
        self.db = db
        self.default_data()


    def init_edit(self):
        self.title('Редактировать')
        self.btn_edit = tk.Button(self, text='Редактировать', bg='#F4A460', activebackground='#FF6347', bd=0)
        self.btn_edit.place(x=50, y=305)
        self.btn_edit.bind('<Button-1>', lambda event: self.view.update_records(self.entry_obj_nm.get(),      
                                                                                self.entry_bore_nm.get(),
                                                                                self.entry_bore_date.get(),
                                                                                self.entry_bore_abs.get(),
                                                                                self.entry_bore_depth.get(),
                                                                                self.entry_layer_roof.get(),
                                                                                self.entry_layer_descr.get(),
                                                                                self.combobox_sample_type.get(),
                                                                                self.entry_sample_depth.get(),
                                                                                self.entry_layer_base.get()))
        self.btn_edit.bind('<Button-1>', lambda event: self.destroy(), add='+')
        self.btn_edit.bind('<Return>', lambda event: self.view.update_records(self.entry_obj_nm.get(),      
                                                                              self.entry_bore_nm.get(),
                                                                              self.entry_bore_date.get(),
                                                                              self.entry_bore_abs.get(),
                                                                              self.entry_bore_depth.get(),
                                                                              self.entry_layer_roof.get(),
                                                                              self.entry_layer_descr.get(),
                                                                              self.combobox_sample_type.get(),
                                                                              self.entry_sample_depth.get(),
                                                                              self.entry_layer_base.get()))
        self.btn_edit.bind('<Return>', lambda event: self.destroy(), add='+')
        self.btn_ok_log.destroy()


    def default_data(self):
        self.db.c.execute('''SELECT * FROM borelog WHERE id=?''',
                          (self.view.tree.set(self.view.tree.selection()[0],'#1')))
        row = self.db.c.fetchone()  # fetchone возвращает кортеж
        self.entry_obj_nm.insert(0, row[1])
        self.entry_bore_nm.insert(0, row[2])
        self.entry_bore_date.insert(0, row[3])
        self.entry_bore_abs.insert(0, row[4])
        self.entry_bore_depth.insert(0, row[5])
        self.entry_layer_roof.insert(0, row[6])
        self.entry_layer_descr.insert(0, row[7])
        if row[8] == 'Монолит':
            self.combobox_sample_type.current(0)
        elif row[8] == 'Нарушенный':
            self.combobox_sample_type.current(1)
        elif row[8] == 'Коррозия':
            self.combobox_sample_type.current(2)
        elif row[8] == 'Вода':
            self.combobox_sample_type.current(3)
        self.entry_sample_depth.insert(0, row[9])
        self.entry_layer_base.insert(0, row[10])


# окно Поиск
class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app


    def init_search(self):
        self.title('Поиск')
        self.geometry('400x150+300+200')
        self.configure(bg='#FFE4C4')
        self.resizable(False, False)

        lbl_search = tk.Label(self, text='Поиск скважины', bg='#FFE4C4')
        lbl_search.place(x=10, y=10)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=150, y=10, width=170)

        btn_search = tk.Button(self, text='Поиск', bg='#F4A460', activebackground='#FF6347', bd=0)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')
        btn_search.bind('<Return>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Return>', lambda event: self.destroy(), add='+')
        btn_search.place(x=10, y=70)

        btn_cancel = tk.Button(self, text='Закрыть', bg='#F4A460', activebackground='#FF6347', bd=0,
                               command=self.destroy)
        btn_cancel.place(x=10, y=100)


# база данных
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('geology.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS borelog
            (id integer primary key, obj_nm text, bore_nm text, bore_date date, bore_abs real, bore_depth real, layer_roof real, 
            layer_descr text, sample_type text, sample_depth real, layer_base real)'''
        )
        self.conn.commit()


    def insert_data(self, obj_nm, bore_nm, bore_date, bore_abs, bore_depth, layer_roof, layer_descr, sample_type, sample_depth, 
                    layer_base):
        self.c.execute('''INSERT INTO borelog (obj_nm, bore_nm, bore_date, bore_abs, bore_depth, layer_roof, 
                       layer_descr, sample_type, sample_depth, layer_base) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                       (obj_nm, bore_nm, bore_date, bore_abs, bore_depth, layer_roof, layer_descr, sample_type, sample_depth, 
                       layer_base))
        self.conn.commit()


# позже будет окно с чертежём


if __name__=='__main__':
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title('Электронный журнал ')
    root.geometry('1110x600+20+20')
    root.configure(bg='#FFE4C4')
    root.resizable(False, False)
    root.mainloop()