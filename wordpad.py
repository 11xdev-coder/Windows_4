from tkinter import *
from tkinter import filedialog


class text_editor:
    current_open_file = 'no_file'

    def open_file(self):
        open_return = filedialog.askopenfile(initialdir='/',title='Выберите файл для открытия',filetypes=(('Text file','*.txt'),('All Files','*.*')))
        if (open_return != None):
            self.text_area.delete(1.0)
            for line in open_return:
                self.text_area.insert(END,line)
            self.current_open_file = open_return.name
            open_return.close()

    def save_as_file(self):
        f = filedialog.asksaveasfile(mode='w',defaultextension='.txt',title='Сохранить как')
        if f is None:
            return
        text2save = self.text_area.get(1.0,END)
        self.current_open_file = f.name
        f.write(text2save)
        f.close()

    def save_file(self):
        if self.current_open_file == 'no_file':
            self.save_as_file()
        else:
            f = open(self.current_open_file,'w+')
            f.write(self.text_area.get(1.0,END))
            f.close()

    def new_file(self):
        self.text_area.delete(1.0,END)
        self.current_open_file = 'no_file'

    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut_text(self):
        self.copy_text()
        self.text_area.delete('sel.first','sel.last')
        self.text_area.clipboard_append(self.text_area.selection_get())

    def paste_text(self):
        self.text_area.insert(END,self.text_area.clipboard_get())

    def __init__(self,master):
        master.title('Блокнот')
        self.text_area = Text(master,undo=True)
        self.text_area.pack(fill=BOTH,expand=1)
        self.main_menu = Menu()
        master.config(menu=self.main_menu)

        # Создаем меню File
        self.file_menu = Menu(self.main_menu,tearoff=0)
        self.main_menu.add_cascade(label='Файл',menu=self.file_menu)
        self.file_menu.add_command(label='Новый', command=self.new_file)
        self.file_menu.add_command(label='Открыть',command=self.open_file)
        self.file_menu.add_command(label='Сохранить', command=self.save_file)
        self.file_menu.add_command(label='Сохранить как', command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Выход', command=master.quit)

        # Создаем меню Edit
        self.edit_menu = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label='Редактировать', menu=self.edit_menu)
        self.edit_menu.add_command(label='Отменить', command=self.text_area.edit_undo)
        self.edit_menu.add_command(label='Повторить', command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Копировать', command=self.copy_text)
        self.edit_menu.add_command(label='Вырезать', command=self.cut_text)
        self.edit_menu.add_command(label='Вставить', command=self.paste_text)