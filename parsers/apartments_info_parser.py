import csv
from itertools import zip_longest
from parsers.apartments_links_parser import get_page_soup


def get_list_of_links():
    with open('../apartments_data/apartments_links.csv', 'r') as links_file:
        reader = csv.reader(links_file)
        return list(reader)[-1]


def get_address(apartment_soup):
    try:
        address = apartment_soup.findAll('a', {'class': "a10a3f92e9--link--1t8n1 a10a3f92e9--address-item--1clHr"})
        address = [i.text for i in address]
    except Exception:
        print("get_address failed")
        address = None
    return address


def get_price(apartment_soup):
    try:
        price = apartment_soup.find('span', {"class": "a10a3f92e9--price_value--1iPpd"})
        price = price.span.get('content')
    except Exception:
        print("get_price failed")
        price = None
    return price


def get_info_block(apartment_soup):
    info_block = {'Общая': None,
                  'Жилая': None,
                  'Кухня': None,
                  'Этаж': None,
                  'Построен': None}
    try:
        features = apartment_soup.findAll('div', {"class": "a10a3f92e9--info-title--2bXM9"})
        values = apartment_soup.findAll('div', {"class": "a10a3f92e9--info-value--18c8R"})
        info_block.update(dict(zip([i.text for i in features], [i.text for i in values])))
    except Exception:
        print("get_info_block failed")
    return info_block


def get_general_block(apartment_soup):
    general_block = {'Высота потолков': None,
                     'Санузел': None,
                     'Ванная комната': None,
                     'Балкон/лоджия': None,
                     'Ремонт': None,
                     'Вид из окон': None}
    try:
        features = apartment_soup.findAll('span', {"class": "a10a3f92e9--name--3bt8k"})
        values = apartment_soup.findAll('span', {"class": "a10a3f92e9--value--3Ftu5"})
        general_block.update(dict(zip([i.text for i in features], [i.text for i in values])))
    except Exception:
        print("get_general_block failed")
    return general_block


def get_house_block(apartment_soup):
    house_block = {'Год постройки': None,
                   'Тип дома': None,
                   'Тип перекрытий': None,
                   'Подъезды': None,
                   'Лифты': None,
                   'Отопление': None,
                   'Аварийность': None,
                   'Парковка': None,
                   'Мусоропровод': None,
                   'Газоснабжение': None}
    try:
        features = apartment_soup.findAll('div', {"class": "a10a3f92e9--name--22FM0"})
        values = apartment_soup.findAll('div', {"class": "a10a3f92e9--value--38caj"})
        house_block.update(dict(zip([i.text for i in features], [i.text for i in values])))
    except Exception:
        print("get_house_block failed")
    return house_block


def get_underground_info(apartment_soup):
    try:
        underground = apartment_soup.findAll('a', {'class': "a10a3f92e9--underground_link--AzxRC"})
        time = apartment_soup.findAll('span', {'class': "a10a3f92e9--underground_time--1fKft"})

        underground = [i.text for i in underground]
        time = [i.text for i in time]
        return dict(zip_longest(underground, time))
    except Exception:
        print("get_underground_info failed")
        return None


def add_features(apartment_soup):
    features = list()
    features.append(get_price(apartment_soup))

    with open('../apartments_data/apartments_database.csv', 'a+') as database_file:
        apartment_writer = csv.writer(database_file)
        apartment_writer.writerow(features)



apartments_links = get_list_of_links()
for apartment_link in apartments_links:
    apartment_soup = get_page_soup(apartment_link)
    add_features(apartment_soup)
