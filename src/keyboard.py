from src.item import Item


class MixinLang:
    '''Миксин -  замена раскладки
    param: language  - раскладка'''

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"


class Keyboard(Item, MixinLang):
    '''
    Класс потомок - клавиатуры
    '''

    def __init__(self, name_: str, price: float, quantity: int):
        super().__init__(name_, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value
