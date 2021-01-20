from tkinter import *
from tkinter import filedialog
from tkinter.font import Font


class word_editor:
    current_open_file = 'no_file'

    def open_file(self):
        open_return = filedialog.askopenfile(initialdir='/', title='Выберите файл для открытия', filetypes=(('Текстовые файлы', '*.txt'), ('Файлы разметки', '*.md'), ('Все файлы', '*.*')))
        if (open_return != None):
            self.text_area.delete(1.0)
            for line in open_return:
                self.text_area.insert(END,line)
            self.current_open_file = open_return.name
            open_return.close()

    def save_as_file(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension='.md', title='Сохранить как')
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
        master.title('Редактор файлов разметки')

        ################Шрифты###################
        italic_font = Font(family='Helvetica', size=12, slant='italic')
        bold_font = Font(family='Helvetica', size=12, weight='bold')
        underlined_font = Font(family='Helvetica', size=12, underline=1)
        overstrike_font = Font(family='Helvetica', size=12, overstrike=1)
        ###################################

        self.text_area = Text(master, undo=True)
        self.text_area.grid(row=2, column=0, columnspan=20)
        self.main_menu = Menu()
        master.config(menu=self.main_menu)
        # Создаем изображения
        self.paste_img = PhotoImage(file='images/ms_dos_pasteimg.PNG')
        self.copy_img = PhotoImage(file='images/ms_dos_copyimg.PNG')
        self.empty_checkbtn = PhotoImage(file='images/empty_checkbtn.png')
        self.full_checkbtn = PhotoImage(file='images/full_checkbtn.png')

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

        # Создаем кнопки
        # Кнопки копирования и вставления
        self.paste_btn = Button(master, image=self.paste_img, command=lambda: self.paste_text())
        self.paste_btn.grid(row=0, column=0)
        self.copy_btn = Button(master, image=self.copy_img, command=lambda: self.copy_text())
        self.copy_btn.grid(row=0, column=1)

        # Кнопки шрифтов
        self.italic_btn = Button(master, text='Н', font=italic_font, command=lambda: self.text_area.insert(END, '__'))
        self.italic_btn.grid(row=0, column=2)
        self.bold_btn = Button(master, text='Ж', font=bold_font, command=lambda: self.text_area.insert(END, '****'))
        self.bold_btn.grid(row=0, column=3)
        self.underline_btn = Button(master, text='П', font=underlined_font, command=lambda: self.text_area.insert(END, '<u></u>'))
        self.underline_btn.grid(row=0, column=4)
        self.overstrike_btn = Button(master, text='З', font=overstrike_font, command=lambda: self.text_area.insert(END, '~~~~'))
        self.overstrike_btn.grid(row=0, column=5)
        self.code_btn = Button(master, text='<>', command=lambda: self.text_area.insert(END, '``'))
        self.code_btn.grid(row=1, column=2)
        self.empty_btn = Button(master, image=self.empty_checkbtn, command=lambda: self.text_area.insert(END, '- [ ]'))
        self.empty_btn.grid(row=1, column=3)
        self.full_btn = Button(master, image=self.full_checkbtn, command=lambda: self.text_area.insert(END, '- [x]'))
        self.full_btn.grid(row=1, column=4)
        self.title1 = Button(master, text='З1', command=lambda: self.text_area.insert(END, '#'))
        self.title1.grid(row=0, column=6)
        self.title2 = Button(master, text='З2', command=lambda: self.text_area.insert(END, '##'))
        self.title2.grid(row=0, column=7)
        self.title3 = Button(master, text='З3', command=lambda: self.text_area.insert(END, '###'))
        self.title3.grid(row=0, column=8)
        self.title4 = Button(master, text='З4', command=lambda: self.text_area.insert(END, '####'))
        self.title4.grid(row=0, column=9)
        self.title5 = Button(master, text='З5', command=lambda: self.text_area.insert(END, '#####'))
        self.title5.grid(row=1, column=5)
        self.title6 = Button(master, text='З6', command=lambda: self.text_area.insert(END, '######'))
        self.title6.grid(row=1, column=6)
        self.quote = Button(master, text='Ц', command=lambda: self.text_area.insert(END, '>'))
        self.quote.grid(row=1, column=7)
        self.notenumlist = Button(master, text='НПС', command=lambda: self.text_area.insert(END, '* '))
        self.notenumlist.grid(row=1, column=8)
        self.enumlist = Button(master, text='ПС', command=lambda: self.text_area.insert(END, 'Номер. '))
        self.enumlist.grid(row=1, column=9)
        self.separator = Button(master, text='Рздл', command=lambda: self.text_area.insert(END, '***'))
        self.separator.grid(row=0, column=10)
        self.hyperlink = Button(master, text='ГС', command=lambda: self.text_area.insert(END, '[текст ссылки](ссылка "необязательая подсказка")'))
        self.hyperlink.grid(row=0, column=11)
        self.passable_hyperlink = Button(master, text='СГС', command=lambda: self.text_area.insert(END, '[айди ссылки]: ссылка "необязательая подсказка"'))
        self.passable_hyperlink.grid(row=1, column=11)
        self.picture = Button(master, text='Изоб.', command=lambda: self.text_area.insert(END, '![текст](/путь/к/изображению "Подсказка")'))
        self.picture.grid(row=1, column=10)
