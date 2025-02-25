from src.item import Item

class Phone(Item):
    '''Класс потомок - телефоны
    param number_of_sim - кол-во сим кард
    '''

    def __init__(self,name_: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name_, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
            print("ошибка")
        else:
            self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
