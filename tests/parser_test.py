import pytest
import parsers.apartments_info_parser as ap
from parsers.apartments_links_parser import get_apartments_links
from tests.test_constants import primary_soup, secondary_soup, page_soup,\
                                 expected_answers, expected_links


@pytest.mark.parametrize("apartment_soup", [primary_soup, secondary_soup])
def test_get_address(apartment_soup):
    assert ap.get_address(apartment_soup) == expected_answers[apartment_soup]['address']


@pytest.mark.parametrize("apartment_soup", [primary_soup, secondary_soup])
def test_get_info_block(apartment_soup):
    assert ap.get_info_block(apartment_soup) == expected_answers[apartment_soup]['info_block']


@pytest.mark.parametrize("apartment_soup", [primary_soup, secondary_soup])
def test_get_general_block(apartment_soup):
    assert ap.get_general_block(apartment_soup) == expected_answers[apartment_soup]['general_block']


@pytest.mark.parametrize("apartment_soup", [primary_soup, secondary_soup])
def test_get_house_block(apartment_soup):
    if apartment_soup == primary_soup:
        func = ap.get_primary_house_block
    else:
        func = ap.get_secondary_house_block
    assert func(apartment_soup) == expected_answers[apartment_soup]['house_block']


@pytest.mark.parametrize("apartment_soup", [primary_soup, secondary_soup])
def test_get_underground_info(apartment_soup):
    assert ap.get_underground_info(apartment_soup) == expected_answers[apartment_soup]['underground_info']


@pytest.mark.parametrize("apartment_soup", [primary_soup, secondary_soup])
def test_get_price(apartment_soup):
    assert ap.get_price(apartment_soup) == expected_answers[apartment_soup]['price']


@pytest.mark.parametrize("apartment_soup", [primary_soup, secondary_soup])
def test_get_features_dict(apartment_soup):
    expected_features_dict = {}
    for k, v in expected_answers[apartment_soup].items():
        if k == 'price':
            expected_features_dict['Цена'] = v
        else:
            expected_features_dict.update(v)
    if apartment_soup == primary_soup:
        expected_features_dict['Газоснабжение'] = None
        expected_features_dict['Год постройки'] = None
        expected_features_dict['Лифты'] = None
        expected_features_dict['Мусоропровод'] = None
        expected_features_dict['Отопление'] = None
        expected_features_dict['Подъезды'] = None
        expected_features_dict['Тип перекрытий'] = None
        expected_features_dict['Аварийность'] = None
    assert ap.get_features_dict(apartment_soup) == expected_features_dict


def test_get_get_apartments_links():
    assert get_apartments_links(page_soup) == expected_links
