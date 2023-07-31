from src.item import Item


class MixinLog:
    change_ln = ('EN', 'RU')
    __slots__ = "__language"

    def __init__(self):
        self.__language = self.change_ln[0]

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language == 'EN':
            self.__language = 'RU'
        elif self.language == 'RU':
            self.__language = 'EN'

        return self


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
