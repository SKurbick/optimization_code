# Задание: найти среднюю арифметическую цену всех квартир во всех районах
district_1 = {'flat_1': 10500, 'flat_2': 11000}
district_2 = {'flat_3': 15000}
district_3 = {'flat_4': 6500, 'flat_5': 7000, 'flat_6': 6000}


# *args все переданные значения упаковывает в кортеж
def average_price_args(*districts):  # значение *args позволяет вводить неопределеное колличество аргуменотов
    price = 0
    flats = 0
    for district in districts:
        price += sum(
            district.values())  # высчитывает ср. ар. в каждом районе и суммирует с предыдущий районом сохраненном в переменной price
        flats += len(district.values())  # высчитывает общее колличество значение (квартир)
    return price / flats


print(average_price_args(district_1, district_2,
                         district_3))  # с помощью *args программа пройдется циклом по каждому значению


# конструкция kwargs распаковывает именованные аргументы
def average_price_kwargs(districts):
    return sum(districts.values()) / len(districts.values())


print(average_price_kwargs({**district_1, **district_2, **district_3}))
#то есть, все заданные аргументы будут распакованы и перемещенны в один кортеж со значениями
#минус такого применения, что ключи обязательно не должны совпадать
