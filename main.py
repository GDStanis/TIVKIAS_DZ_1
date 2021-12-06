from text_to_num import text2num
from langdetect import detect, detect_langs, LangDetectException
from langdetect import DetectorFactory

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

DetectorFactory.seed = 0

Window.size = (500, 250)
Window.title = 'Task №1'


class Converter(App):

    def __init__(self):
        super().__init__()
        self.description = Label(text='Введите число на английском по шаблону'
                                      ' \n[one-nine] hundred [twenty-ninety] [one-nine]. '
                                      '\nПри наличии чисел 11-19 - [eleven-nineteen]')
        self.min = Label(text='')
        self.err = Label(text='')
        self.arab_num = Label(text='Арабские цифры: ')
        self.roman_num = Label(text='Римские цифры: ')
        self.input_num = TextInput(text='', multiline=False)
        self.btn = Button(text='Перевести')
        self.btn.bind(on_press=self.pressed)

    def build(self):
        box = BoxLayout(orientation='vertical', padding=15)
        box.add_widget(self.description)
        box.add_widget(self.min)
        box.add_widget(self.err)
        box.add_widget(self.input_num)
        box.add_widget(self.arab_num)
        box.add_widget(self.roman_num)
        box.add_widget(self.btn)
        return box

    def pressed(self, instance):
        arr = []
        data = self.input_num.text
        arr = self.input_num.text.split()
        print(arr)
        print(data)
        self.err.text = ''

        if not (type(data) is float) or (type(data) is int) or data.isdigit():
            try:
                lang = detect(data)
                print(lang)
            except LangDetectException:
                self.err.text = 'Ошибка ввода. Введено числовое значение.'
                return
            try:
                self.err.text = ''
                self.arab_num.text = 'Арабские цифры: ' + str(text2num(data, "en"))
                data_roman = text2num(data, "en")
                self.roman_num.text = 'Римские цифры: ' + str(int_to_roman(data_roman))
            except ValueError:
                if (type(data) is float) or (type(data) is int) or data.isdigit():
                    self.err.text = 'Ошибка. Введено числовое значение.'
                # elif lang != "en":
                #     self.err.text = 'Ошибка. Неправильный язык ввода.'
                else:
                    self.err.text = 'Ошибка ввода. Проверьте и повторите ввод.'
            print('Done.')


def int_to_roman(input):
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)


if __name__ == "__main__":
    Converter().run()
