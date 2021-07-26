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
                'Тип дома': 'house_type', 'Тип перекрытий': 'overlap_type', 'Подъезды': 'entrances',
                'Лифты': 'elevators', 'Отопление': 'heating', 'Аварийность': 'emergency', 'Парковка': 'parking',
                'Мусоропровод': 'garbage chute', 'Газоснабжение': 'gas_supply',
                'Сдача комплекса': 'complex_completion_date', 'Застройщик': 'developer',
                'Класс': 'housing_class', 'Кол-во корпусов': 'buildings_number', 'Ближайшее метро': 'nearest_subway',
                'Время до ближайшего метро': 'nearest_subway_time', 'Цена': 'price'}

selection_threshold = 100

numerical_columns = {
    'standard_features': ['total_area'],
    'house_build_date_included': ['total_area', 'build_date_1995_2010', 'build_date_2010_2022', 'build_date_2022_plus'],
    'floor_number_included': ['total_area', 'build_date_1995_2010', 'build_date_2010_2022',
                              'build_date_2022_plus', 'floor_number_1_5', 'floor_number_5_12']
}

categorical_columns = {
    'standard_features': ['district', 'housing_type', 'house_type', 'subway_summary'],
    'house_build_date_included': ['district', 'housing_type', 'house_type', 'subway_summary'],
    'floor_number_included': ['district', 'housing_type', 'house_type', 'subway_summary']
}

models = ['Ridge', 'KNN', 'SVR']

model_params = {
    'Ridge': {
        'alpha': [0.01, 0.1, 1.0, 10.0, 100.0]
    },
    'KNN': {
        'n_neighbors': [3, 5, 9, 15]
    },
    'SVR': {
        'kernel': ['linear', 'rbf'],
        'C': [0.01, 0.1, 1, 10],
        'epsilon': [0, 0.01, 0.1, 0.5, 1, 2, 4]
    }
}

modeling_results_fields = ['model_type', 'feature_type', 'optimal_params',
                           'LMSE', 'LRMSE', 'R-Squared']
