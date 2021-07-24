import csv
from bs4 import BeautifulSoup
from tqdm import tqdm
from constants import feature_names
from selenium import webdriver


def get_list_of_links():
    with open('apartments_data/apartments_links.csv', 'r') as links_file:
        reader = csv.reader(links_file)
        return list(reader)[-1]


def get_address(apartment_soup):
    address_dict = {'Город': None,
                    'Округ': None,
                    'Район': None,
                    'Улица': None,
                    'Дом': None}
    try:
        address = apartment_soup.findAll('a', {'class': "a10a3f92e9--link--1t8n1 a10a3f92e9--address-item--1clHr"})
        address = [i.text for i in address]
        address_dict = dict(zip([k for k in address_dict], address))
    except Exception:
        print("get_address failed")
    return address_dict


def get_info_block(apartment_soup):
    info_block = {'Общая': None,
                  'Жилая': None,
                  'Кухня': None,
                  'Этаж': None,
                  'Построен': None,
                  'Срок сдачи': None}
    try:
        features = apartment_soup.findAll('div', {"class": "a10a3f92e9--info-title--2bXM9"})
        values = apartment_soup.findAll('div', {"class": "a10a3f92e9--info-value--18c8R"})
        new_dict = dict(zip([i.text for i in features], [i.text for i in values]))
        info_block.update((k, v) for k, v in new_dict.items() if k in info_block)
    except Exception:
        print("get_info_block failed")
    return info_block


def get_general_block(apartment_soup):
    general_block = {'Тип жилья': None,
                     'Высота потолков': None,
                     'Санузел': None,
                     'Ванная комната': None,
                     'Балкон/лоджия': None,
                     'Ремонт': None,
                     'Вид из окон': None,
                     'Площадь комнат': None,
                     'Отделка': None}
    try:
        features = apartment_soup.findAll('span', {"class": "a10a3f92e9--name--3bt8k"})
        values = apartment_soup.findAll('span', {"class": "a10a3f92e9--value--3Ftu5"})
        new_dict = dict(zip([i.text for i in features], [i.text for i in values]))
        general_block.update((k, v) for k, v in new_dict.items() if k in general_block)
    except Exception:
        print("get_general_block failed")
    return general_block


def get_secondary_house_block(apartment_soup):
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
        new_dict = dict(zip([i.text for i in features], [i.text for i in values]))
        house_block.update((k, v) for k, v in new_dict.items() if k in house_block)
    except Exception:
        print("get_secondary_house_block failed")
    return house_block


def get_primary_house_block(apartment_soup):
    house_block = {'Сдача комплекса': None,
                   'Застройщик': None,
                   'Класс': None,
                   'Кол-во корпусов': None,
                   'Тип дома': None,
                   'Парковка': None,
                   'Отделка': None}
    try:
        block = apartment_soup.findAll('li', {"class": "a10a3f92e9--item--9Hw61"})
        features = [link.find('span', {"class": "a10a3f92e9--color_gray60_100--3VLtJ a10a3f92e9--"
                                                "lineHeight_22px--2Pr_0 a10a3f92e9--fontWeight_normal--"
                                                "2G6_P a10a3f92e9--fontSize_16px--1mDFP a10a3f92e9--"
                                                "display_inline--2gjyY a10a3f92e9--text--2_SER"}) for link in block]
        values = [link.find('span', {"class": "a10a3f92e9--color_black_100--A_xYw a10a3f92e9--"
                                              "lineHeight_22px--2Pr_0 a10a3f92e9--fontWeight_normal--"
                                              "2G6_P a10a3f92e9--fontSize_16px--1mDFP a10a3f92e9--"
                                              "display_inline--2gjyY a10a3f92e9--text--2_SER"}) for link in block]
        new_dict = dict(zip([i.text for i in features], [i.text if i else None for i in values]))
        house_block.update((k, v) for k, v in new_dict.items() if k in house_block)
        house_block["Застройщик"] = apartment_soup.find('a', {"class": "a10a3f92e9--element--2vdm4"}).text
    except Exception:
        print("get_primary_house_block failed")
    return house_block


def get_underground_info(apartment_soup):
    underground_dict = {
        'Ближайшее метро': None,
        'Время до ближайшего метро': None
    }
    try:
        underground = apartment_soup.find('a', {'class': "a10a3f92e9--underground_link--AzxRC"}).text
        try:
            time = apartment_soup.find('span', {'class': "a10a3f92e9--underground_time--1fKft"}).text
        except Exception:
            time = None
        underground_dict["Ближайшее метро"] = underground
        underground_dict["Время до ближайшего метро"] = time
    except Exception:
        print("get_underground_info failed")

    return underground_dict


def get_price(apartment_soup):
    try:
        price = apartment_soup.find('span', {"class": "a10a3f92e9--price_value--1iPpd"})
        price = price.span.get('content')
    except Exception:
        print("get_price failed")
        price = None
    return price


def get_features_dict(apartment_soup):
    features_dict = dict()
    features_dict.update(get_address(apartment_soup))
    features_dict.update(get_info_block(apartment_soup))
    features_dict.update(get_general_block(apartment_soup))
    features_dict.update(get_secondary_house_block(apartment_soup))
    if not (features_dict['Год постройки'] or features_dict['Тип дома']):
        features_dict.update(get_primary_house_block(apartment_soup))
    features_dict.update(get_underground_info(apartment_soup))
    features_dict[feature_names[-1]] = get_price(apartment_soup)
    return features_dict


def parse_apartments_data():
    driver = webdriver.Chrome("parsers/chromedriver")
    apartments_links = get_list_of_links()
    with open('apartments_data/apartments_database.csv', 'a+') as database_file:
        writer = csv.DictWriter(database_file, fieldnames=feature_names)
        # writer.writeheader()
        for apartment_link in tqdm(apartments_links[6041:]):
            driver.get(apartment_link)
            apartment_soup = BeautifulSoup(driver.page_source, 'html.parser')
            if apartment_soup.find('div', {'data-name': 'OfferUnpublished'}):
                print('Offer removed from publication')
                continue
            features_dict = get_features_dict(apartment_soup)
            features_dict[feature_names[0]] = apartment_link[apartment_link.find('flat') + 5:-1]
            writer.writerow(features_dict)

    driver.close()
