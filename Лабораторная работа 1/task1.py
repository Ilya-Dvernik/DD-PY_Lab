import doctest
# TODO Написать 3 класса с документацией и аннотацией типов

class Cup:
    def __init__(self, liquid:str,volume: int, occupied_volume: int,place:str):
        """
        Создание и подготовка к работе обьекта "Кружка"

        :param liquid: Жидкость в кружке
        :param volume: Объём кружки в мл
        :param occupied_volume: Объем занимаемой жидкости в мл
        :param place: Место где находится кружка

        Пример:
        >>> cup_1 = Cup("Вода",250,100, "Верхний шкаф") #инициализация экземпляра класса
        """
        if not isinstance(liquid, str):
            raise TypeError
        self.liquid=liquid

        if not isinstance(place, str):
            raise TypeError
        self.place = place

        if not isinstance(volume, int):
            raise TypeError("Объем кружки должен быть типа int ")
        if volume <= 0:
            raise ValueError("Объем кружки должен быть положительным числом")
        self.volume = volume

        if not isinstance(occupied_volume, int):
            raise TypeError("Количество жидкости должно быть int")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

        if occupied_volume > volume:
            raise ValueError("Количество жидкости не должно превышать обьёма кружки")
        pass

    def move_the_mug(self,new_pos: str)->str:
        """
        Функция меняет позицию стакана на новую

        :param new_pos: Новое место кружки
        :raise TypeError: Если новое место кружки не пренадлежит типу str, то вызывает ошибку

        :return: Новое место кружки

        Пример:
        >>> cuppp = Cup("Вода", 100,100, "Тумбочка")
        >>> cuppp.move_the_mug("Стол")
        """
        if not isinstance(new_pos,str):
            raise TypeError("Новое место кружки должно быть типа str")
        ...

    def add_liquid(self,plus_volume:int)->None:
        """
        Функция добавляет жидкости в стакан

        :param plus_volume: Объем добавляемой жидкости
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в кружке, то вызывает ошибку

        Пример:
        >>> cup_2 = Cup("Вода", 100,40, "Тумбочка")
        >>> cup_2.add_liquid(50)
        """
        if not isinstance(plus_volume, int):
            raise TypeError("Добавляемая жидкость должна быть типа int")
        if plus_volume < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")
        ...


class Garland:
    def __init__(self,color :str,mode: int,length: int):
        """
        Создание оздание и подготовка к работе обьекта "Гирлянда"
        :param color: Цвет гирлянды
        :param mode: Режим работы гирлянды(1-свечение, 2-мерцание, 3-"волна")
        :param length: Длина гирлянды в метрах

        Пример:
        >>> gerlanda_1 = Garland("Красный",1,6)
        """
        if not isinstance(color, str):
            raise TypeError("Цвет Гирлянды должен быть типа str")
        self.color = color

        if mode > 3 and mode <1 :
            raise ValueError("Режим работы должен принимать значения 1, 2 или 3")
        self.mode = mode

        if length < 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

    def change_mode(self)-> str:
        """
        Функция меняет режим работы гирлянды (1->2, 2->3, 3->1)

        :return: Новый режим гирлянды

        Пример:
        >>> ger_1 = Garland("Синий",1,6)
        >>> ger_1.change_mode()
        """
        ...

    def change_color(self,new_color: str)-> str:
        """
        Функция меняет цвет гирлянды

        :param new_color: Новый цвет гирлянды
        :raise TypeError: Если новый цвет не пренадлежит типу str, то вызывает ошибку

        :return: Новый цвет гирлянды

        Пример:
        >>> garla = Garland("Синий",1,6)
        >>> garla.change_color("Красный")
        """
        if not isinstance(new_color,str):
            raise TypeError("Новый цвет должен быть типа str")
        ...



class Monitor:
    def __init__(self, diagonal: int,screen_resolution: str,condition: bool):
        """
        Создание и подготовка к работе обьекта "Монитор"

        :param diagonal: Размер диогонали экрана в дюймах
        :param condition: Состояние экрана (включен=True / выключен=Fasle)
        :param screen_resolution: Разрешение экрана (Например:SXGA, WXGA, Full HD,...)

        Пример:
        >>> monitor_1 = Monitor(27,"SXGA",True) #инициализация экземпляра класса
        """
        if not isinstance(diagonal, int):
            raise TypeError("Диогональ экрана должно быть типа ште")
        if diagonal < 0:
            raise ValueError("Диогональ экрана должена быть положительным числом")
        self.diagonal = diagonal

        if not isinstance(screen_resolution, str):
            raise TypeError("Разрешение экрана должно быть типа str")
        self.screen_resolution = screen_resolution

        if not isinstance(condition, bool):
            raise TypeError("Состояние экрана долно быть типа bool ")
        self.condition = condition

    def change_monitor_condition(self) -> None:
        """
        Функция меняет режим экрана

        Пример:
        >>> monik = Monitor(27,"Full HD",True)
        >>> monik.change_monitor_condition()
        """
        ...

    def change_screen_resolution(self, new_rash:str)-> str:
        """
        Функция меняет разрешение экрана

        :param new_rash: Новое расширение экрана
        :raise TypeError: Если новое расщирение экрана не пренадлежит типу str, то вызывает ошибку

        :return: Новое расширение экрана

        Пример:
        >>> monik_2 = Monitor(21,"SXGA", True)
        >>> monik_2.change_screen_resolution("Full HD")
        """
        if not isinstance(new_rash,str):
            raise TypeError("Новое расщирение экрана должно быть типа str")
        ...


if __name__ == "__main__":
    monitorchik = Monitor(21,"Full HD",False)
    print(monitorchik.diagonal, monitorchik.condition)
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass