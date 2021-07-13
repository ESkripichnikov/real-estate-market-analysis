import csv
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from tqdm import tqdm
from constants import secondary, primary, number_to_parse, cian_url, Category, Rooms
import time

ratio = number_to_parse / sum(primary + secondary)
primary_count = [int(i * ratio) for i in primary]  # how many flats of each apartment type to parse
secondary_count = [int(i * ratio) for i in secondary]  # how many flats of each apartment type to parse

primary_pages = [int(i / 28 + 1) for i in primary_count]  # how many pages of each apartment type to parse
secondary_pages = [int(i / 28 + 1) for i in secondary_count]  # how many pages of each apartment type to parse

primary_pages = dict(zip(Rooms, primary_pages))
secondary_pages = dict(zip(Rooms, secondary_pages))


def get_url(category, rooms):
    return cian_url.format(category=category, rooms_number=rooms) + "&p={page_number}"


def get_page_soup(url_link):
    response = requests.get(url_link, headers={'User-Agent': UserAgent().chrome})
    if not response.ok:
        return None
    html = response.content
    return BeautifulSoup(html, 'html.parser')


def get_apartments_links(page_soup) -> list[str]:
    try:
        apartments_links = page_soup.findAll('a', {"class": "_93444fe79c--link--39cNw"})
        apartments_links = [link.attrs["href"] for link in apartments_links]
        if not apartments_links:
            print("get no links!")
    except Exception:
        print("get no links!")
        apartments_links = []

    return apartments_links


def parse_apartments_links():
    apartments_links = []

    for rooms, pages in tqdm(primary_pages.items()):
        url = get_url(Category.primary.value, rooms.value)
        for page in tqdm(range(pages)):
            page_soup = get_page_soup(url.format(page_number=page))
            apartments_links += get_apartments_links(page_soup)
            time.sleep(5)
        with open('apartments_data/apartments_links.csv', 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([f'Primary: {rooms} is complete'])
            writer.writerow(apartments_links)

    for rooms, pages in tqdm(secondary_pages.items()):
        url = get_url(Category.secondary.value, rooms.value)
        for page in tqdm(range(pages)):
            page_soup = get_page_soup(url.format(page_number=page))
            apartments_links += get_apartments_links(page_soup)
            time.sleep(5)
        with open('apartments_data/apartments_links.csv', 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([f'Secondary: {rooms} is complete'])
            writer.writerow(apartments_links)
