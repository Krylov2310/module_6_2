print('\033[30m\033[47mДомашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств.\033[0m')
print('\033[30m\033[47mЗадача "Изменять нельзя получать":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


class Vehicle:
    __COLOR_VARIANTS = ['Wrhite', 'Orange', 'Black', 'ReD']

    def __init__(self, owner: str, __model: str, __color: str, __endine_power: int):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__endine_power = __endine_power

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__endine_power}')

    def get_color(self):
        print(f'Цвет: \033[32m{self.__color}\033[0m')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: \033[34m{self.owner}\033[0m')

    def set_color(self, new_color: str):
        set_veriant = [i.lower() for i in self.__COLOR_VARIANTS]
        if new_color.lower() in set_veriant:
            self.__color = new_color
        else:
            print(f'\033[35mНельзя сменить цвет на {new_color}\033[0m')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Исходный код:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
print()
print(thanks)
