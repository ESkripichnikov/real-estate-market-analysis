from enum import Enum


# studio apartment, 1-room, 2-room, 3-room, 4-room, 5-room, 6+-room, other
secondary = [1000, 9000, 13000, 12000, 4500, 2000, 1000, 500]  # number of apartments of each type for secondary housing
primary = [4200, 10500, 14000, 8000, 2000, 180, 220]  # number of apartments of each type for primary housing
number_to_parse = 10000
cian_url = "https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&" \
           "object_type[0]={category}&offer_type=flat&region=-1&room{rooms_number}=1"


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
