from enum import Enum


# studio apartment, 1-room, 2-room, 3-room, 4-room, 5-room, 6+-room, other
secondary = [1000, 9000, 13000, 12000, 4500, 2000, 1000, 500]  # number of apartments of each type for secondary housing
primary = [4200, 10500, 14000, 8000, 2000, 180, 220]  # number of apartments of each type for primary housing
number_to_parse = 10000
cian_url = "https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&" \
           "object_type[0]={category}&offer_type=flat&region=1&room{rooms_number}=1"


class Category(Enum):
    secondary = 1
    primary = 2


class Rooms(Enum):
    __order__ = 'one two three four five six studio other'
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    studio = 9
    other = 7


feature_names = ['id', 'Город', 'Округ', 'Район', 'Улица', 'Дом',
                 'Общая', 'Жилая', 'Кухня', 'Этаж', 'Построен', 'Срок сдачи',
                 'Тип жилья', 'Высота потолков', 'Санузел', 'Ванная комната', 'Балкон/лоджия',
                 'Ремонт', 'Вид из окон', 'Площадь комнат', 'Отделка',
                 'Год постройки', 'Тип дома', 'Тип перекрытий', 'Подъезды', 'Лифты', 'Отопление',
                 'Аварийность', 'Парковка', 'Мусоропровод', 'Газоснабжение',
                 'Сдача комплекса', 'Застройщик', 'Класс', 'Кол-во корпусов',
                 'Ближайшее метро', 'Время до ближайшего метро', 'Цена'
                 ]

column_names = {'Город': 'city', 'Округ': 'district', 'Район': 'region', 'Улица': 'street', 'Дом': 'house',
                'Общая': 'total_area', 'Жилая': 'living_area', 'Кухня': 'kitchen_area', 'Этаж': 'floor_number',
                'Построен': 'build_date', 'Срок сдачи': 'completion_date', 'Тип жилья': 'housing_type',
                'Высота потолков': 'ceiling_high', 'Санузел': 'bathroom_type', 'Ванная комната': 'bathroom',
                'Балкон/лоджия': 'balcony', 'Ремонт': 'apartment_renovation', 'Вид из окон': 'window_view',
                'Площадь комнат': 'rooms_area', 'Отделка': 'apartment_finishing', 'Год постройки': 'house_build_date',
                'Тип дома': 'house_type', 'Тип перекрытий': 'overlap_type', 'Подъезды': 'entrances', 'Лифты': 'elevators',
                'Отопление': 'heating', 'Аварийность': 'emergency', 'Парковка': 'parking', 'Мусоропровод': 'garbage chute',
                'Газоснабжение': 'gass_supply', 'Сдача комплекса': 'complex_completion_date', 'Застройщик': 'developer',
                'Класс': 'housing_class', 'Кол-во корпусов': 'buldings_number', 'Ближайшее метро': 'nearest_subway',
                'Время до ближайшего метро': 'nearest_subway_time', 'Цена': 'price'}
