from bs4 import BeautifulSoup

with open('tests/primary_apartment.html', 'r') as primary_apartment, \
     open('tests/secondary_apartment.html', 'r') as secondary_apartment, \
     open('tests/search_results_page.html', 'r') as search_results:
    primary_soup = BeautifulSoup(primary_apartment, 'html.parser')
    secondary_soup = BeautifulSoup(secondary_apartment, 'html.parser')
    page_soup = BeautifulSoup(search_results, 'html.parser')

expected_answers = {
    primary_soup: {
        'address': {
            'Город': 'Москва',
            'Округ': 'ЗАО',
            'Район': 'р-н Раменки',
        },
        'info_block': {
            'Общая': '45,8\xa0м²',
            'Жилая': '14,2\xa0м²',
            'Кухня': '20,9\xa0м²',
            'Этаж': '24 из 29',
            'Построен': None,
            'Срок сдачи': '4 кв. 2024'
        },
        'general_block': {
            'Тип жилья': 'Новостройка',
            'Высота потолков': '3,1 м',
            'Санузел': '1 совмещенный',
            'Ванная комната': None,
            'Балкон/лоджия': None,
            'Ремонт': None,
            'Вид из окон': 'Во двор',
            'Отделка': 'Нет'},
        'house_block': {
            'Сдача комплекса': 'Сдача в 2021—2024',
            'Застройщик': 'ДОНСТРОЙ',
            'Класс': 'Бизнес',
            'Кол-во корпусов': '5 корпусов',
            'Тип дома': 'Монолитный',
            'Парковка': 'Подземная, гостевая',
            'Отделка': 'Чистовая'},
        'underground_info': {
            'Ближайшее метро': 'Мичуринский проспект',
            'Время до ближайшего метро': ' ⋅  18 мин. пешком'
        },
        'price': '18 428 776 ₽'},
    secondary_soup: {
        'address': {
            'Город': 'Москва',
            'Округ': 'НАО (Новомосковский)',
            'Район': 'Сосенское поселение',
            'Улица': 'ул. Василия Ощепкова',
            'Дом': '1'
        },
        'info_block': {
            'Общая': '41,3\xa0м²',
            'Жилая': '22\xa0м²',
            'Кухня': '13,5\xa0м²',
            'Этаж': '14 из 15',
            'Построен': None,
            'Срок сдачи': None,
        },
        'general_block': {
            'Тип жилья': 'Вторичка',
            'Высота потолков': '2,8 м',
            'Санузел': '1 совмещенный',
            'Ванная комната': None,
            'Балкон/лоджия': None,
            'Ремонт': 'Евроремонт',
            'Вид из окон': 'Во двор',
            'Отделка': None},
        'house_block': {
            'Год постройки': '2020',
            'Тип дома': 'Монолитный',
            'Тип перекрытий': 'Железобетонные',
            'Подъезды': '9',
            'Лифты': '18 всего',
            'Отопление': 'Индивидуальный тепловой пункт',
            'Аварийность': 'Нет',
            'Парковка': None,
            'Мусоропровод': None,
            'Газоснабжение': None},
        'underground_info': {
            'Ближайшее метро': 'Коммунарка',
            'Время до ближайшего метро': ' ⋅  7 мин. пешком'
        },
        'price': '10 150 000 ₽'}
}

expected_links = ['https://www.cian.ru/sale/flat/258599783/', 'https://www.cian.ru/sale/flat/249486603/',
                  'https://www.cian.ru/sale/flat/244618835/', 'https://www.cian.ru/sale/flat/258065716/',
                  'https://www.cian.ru/sale/flat/259765303/', 'https://www.cian.ru/sale/flat/259605006/',
                  'https://www.cian.ru/sale/flat/259756402/', 'https://www.cian.ru/sale/flat/253550594/',
                  'https://www.cian.ru/sale/flat/256721975/', 'https://www.cian.ru/sale/flat/261477638/',
                  'https://www.cian.ru/sale/flat/260260785/', 'https://www.cian.ru/sale/flat/256410526/',
                  'https://www.cian.ru/sale/flat/239428028/', 'https://www.cian.ru/sale/flat/238115824/',
                  'https://www.cian.ru/sale/flat/257506100/', 'https://www.cian.ru/sale/flat/257669382/',
                  'https://www.cian.ru/sale/flat/260996684/', 'https://www.cian.ru/sale/flat/259427417/',
                  'https://www.cian.ru/sale/flat/260860157/', 'https://www.cian.ru/sale/flat/261429028/',
                  'https://www.cian.ru/sale/flat/260606202/', 'https://www.cian.ru/sale/flat/261050921/',
                  'https://www.cian.ru/sale/flat/260794264/', 'https://www.cian.ru/sale/flat/228936106/',
                  'https://www.cian.ru/sale/flat/260683165/', 'https://www.cian.ru/sale/flat/259277255/',
                  'https://www.cian.ru/sale/flat/230874177/', 'https://www.cian.ru/sale/flat/243440677/']

