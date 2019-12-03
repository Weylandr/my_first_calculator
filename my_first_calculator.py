#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Program: Мой первый примитивный калькулятор
# v.0

from tkinter import *


class PrimitiveCalculator(Frame):
    """ GUI-калькулятор с миннимумом функций """
    def __init__(self, master):
        """ Инициирует рамку """
        super(PrimitiveCalculator, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """
        Создаёт элементы управления, с помощью которых
        пользователь будет вводить исходные данные.
        """
        # Область ввода
        self.entry_area = Entry(self, borderwidth=5, width=15)
        self.entry_area.grid(row=0, column=0, columnspan=5, pady=15, padx=5, sticky=W+E)

        # Кнопки
        # [Delete]
        self.del_bttn = Button(self,
                               text="        del        ",
                               command=lambda: self.calculator_logic('C'),
                               height=2, font='bold')
        self.del_bttn.grid(row=1, column=0, columnspan=2)
        # [Backspace]
        self.backspace_bttn = Button(self,
                                     text="backspace",
                                     command=lambda: self.calculator_logic('B'),
                                     height=2, font='bold')
        self.backspace_bttn.grid(row=1, column=2, columnspan=2, sticky=W+E)
        # [=] Равно
        self.equally_bttn = Button(self,
                                   text="=",
                                   command=lambda: self.calculator_logic('='),
                                   width=4, height=2, font='bold')
        self.equally_bttn.grid(row=1, column=5, padx=2, pady=1)

        # [÷] Деление
        self.division_bttn = Button(self,
                                    text="÷",
                                    command=lambda: self.calculator_logic('/'),
                                    width=4, height=2, font='bold')
        self.division_bttn.grid(row=2, column=5, columnspan=2)
        # [x] Умножение
        self.multiplication_bttn = Button(self,
                                          text="x",
                                          command=lambda: self.calculator_logic('*'),
                                          width=4, height=2, font='bold')
        self.multiplication_bttn.grid(row=3, column=5)
        # [-]
        self.subtraction_bttn = Button(self,
                                       text="-",
                                       command=lambda: self.calculator_logic('-'),
                                       width=4, height=2, font='bold')
        self.subtraction_bttn.grid(row=4, column=5)
        # [+]
        self.addition_bttn = Button(self,
                                    text="+",
                                    command=lambda: self.calculator_logic('+'),
                                    width=4, height=2, font='bold')
        self.addition_bttn.grid(row=5, column=5, padx=2, pady=1)

        # Другие символы
        # [+/-]
        self.plusminus_bttn = Button(self, text="+/-",
                                     command=lambda: self.calculator_logic('+/-'),
                                     width=4, height=2, font='bold')
        self.plusminus_bttn.grid(row=5, column=0)
        # [,]
        self.comma_bttn = Button(self, text=".",
                                 command=lambda: self.calculator_logic('.'),
                                 width=4, height=2, font='bold')
        self.comma_bttn.grid(row=5, column=2, sticky=W)

        # Кнопки-цифры
        # 7
        self.seven_bttn = Button(self, text="7",
                                 command=lambda: self.calculator_logic('7'),
                                 width=4, height=2, font='bold')
        self.seven_bttn.grid(row=2, column=0)
        # 8
        self.eight_bttn = Button(self, text="8",
                                 command=lambda: self.calculator_logic('8'),
                                 width=4, height=2, font='bold')
        self.eight_bttn.grid(row=2, column=1)
        # 9
        self.nine_bttn = Button(self, text="9",
                                command=lambda: self.calculator_logic('9'),
                                width=4, height=2, font='bold')
        self.nine_bttn.grid(row=2, column=2, sticky=W)
        # 4
        self.four_bttn = Button(self, text="4",
                                command=lambda: self.calculator_logic('4'),
                                width=4, height=2, font='bold')
        self.four_bttn.grid(row=3, column=0)
        # 5
        self.five_bttn = Button(self, text="5",
                                command=lambda: self.calculator_logic('5'),
                                width=4, height=2, font='bold')
        self.five_bttn.grid(row=3, column=1)
        # 6
        self.six_bttn = Button(self, text="6",
                               command=lambda: self.calculator_logic('6'),
                               width=4, height=2, font='bold')
        self.six_bttn.grid(row=3, column=2, sticky=W)
        # 1
        self.one_bttn = Button(self, text="1",
                               command=lambda: self.calculator_logic('1'),
                               width=4, height=2, font='bold')
        self.one_bttn.grid(row=4, column=0)
        # 2
        self.two_bttn = Button(self, text="2",
                               command=lambda: self.calculator_logic('2'),
                               width=4, height=2, font='bold')
        self.two_bttn.grid(row=4, column=1)
        # 3
        self.three_bttn = Button(self, text="3",
                                 command=lambda: self.calculator_logic('3'),
                                 width=4, height=2, font='bold')
        self.three_bttn.grid(row=4, column=2, sticky=W)
        # 0
        self.zero_bttn = Button(self, text="0",
                                command=lambda: self.calculator_logic('0'),
                                width=4, height=2, font='bold')
        self.zero_bttn.grid(row=5, column=1)

    def calculator_logic(self, fragment):
        """ Работа математических операций. Логика самого калькулятора. """
        global memory
        if fragment == '=':
            in_string = '/*-+.0123456789'  # Исключение иных симоволов
            if self.entry_area.get()[0] not in in_string:
                # self.entry_area.insert(END, 'Это нужно удалить')
                self.entry_area.delete(0, END)

            # Сам счёт:
            try:
                calculation_result = eval(self.entry_area.get())
                self.entry_area.insert(END, '=' + str(calculation_result))  # Происходит вывод результатов на экран
            except:
                # self.entry_area.insert(END, "Ошибка 2")
                pass


        # Очистка поля ввода:
        elif fragment == 'C':  # DEL
            self.entry_area.delete(0, END)  # Очищает поле; Смещает всё на 0; Вставляет это в конец.

        elif fragment == 'B':  # Backspace
            # self.entry_display.delete(len(self.entry_display.get()) - 1)       - предолженные способы реализации
            # self.entry_display.delete(self.entry_display.index("insert") - 1)  - удаления из конца строки Entry
            self.entry_area.delete(self.entry_area.index("insert") - 1)

        # Меняет +/-
        elif fragment == '+/-':
            if '=' in self.entry_area.get():
                self.entry_area.delete(0, END)  # Неудовлетворительный элемент кода. Изменить.
            try:
                if self.entry_area.get()[0] == "-":
                    self.entry_area.delete(0)
                else:
                    self.entry_area.insert(0, '-')
            except IndexError:
                pass
        else:
            if '=' in self.entry_area.get():
                self.entry_area.delete(0, END)
            self.entry_area.insert(END, fragment)


# Main:
root = Tk()
root.title('Примитивный калькулятор')
root.geometry('240x312')
app = PrimitiveCalculator(root)
root.mainloop()
