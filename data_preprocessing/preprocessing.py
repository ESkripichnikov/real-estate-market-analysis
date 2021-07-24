import pandas as pd
from constants import column_names


def read_initial_dataframe():
    df = pd.read_csv('../apartments_data/apartments_database.csv', index_col='id')
    df.rename(columns=column_names, inplace=True)
    return df


def adjust_housing_type(df):
    df_new = df.copy()
    df_new.housing_type = df_new.housing_type.apply(lambda x: 'Вторичка' if x.startswith('Вторичка')
                                                    else 'Новостройка')
    return df_new


def get_minutes(s):
    try:
        result = int(s)
    except ValueError:
        result = 0
    return result


def adjust_nearest_subway_time(df):
    df_new = df.copy()
    df_new['subway_type'] = df.nearest_subway_time.apply(lambda x:
                                                         'transport' if x.find('трансп') != -1
                                                         else 'on foot')
    df_new['subway_time'] = df.nearest_subway_time.apply(lambda x: (x
                                                                    .replace('⋅', '')
                                                                    .replace('<', '')
                                                                    .strip())[:2]).apply(get_minutes)
    return df_new


def adjust_districts(df):
    df_new = df.copy()
    df_new.district = df_new.district.apply(lambda x: 'НАО' if x.strip().startswith('НАО')
                                            else x)
    return df_new


def split_on_primary_secondary(df):
    df_primary = df.loc[df.housing_type == 'Новостройка', :].copy()
    df_secondary = df.loc[df.housing_type == 'Вторичка', :].copy()
    return df_primary, df_secondary


def drop_columns_with_many_nans(df, drop_ratio, exceptions=None):
    df_new = df.loc[:, df.isna().sum() / df.shape[0] < drop_ratio].copy()
    if exceptions:
        for exception in exceptions:
            df_new[exception] = df[exception].copy()
    return df_new


def adjust_areas(df, columns_to_adjust=None):
    if columns_to_adjust is None:
        columns_to_adjust = ['total_area', 'living_area', 'kitchen_area']
    df_new = df.copy()
    for column in columns_to_adjust:
        df_new.loc[:, column] = df_new[column].apply(lambda x: float(x
                                                                     .replace('м²', '')
                                                                     .replace(' ', '')
                                                                     .replace(',', '.')
                                                                     .strip()) if type(x) == str else x)
    return df_new


def fillna_areas(df):
    df_new = df.copy()
    living_ratio = (df_new.living_area / df_new.total_area).mean()
    kitchen_ratio = (df_new.kitchen_area / df_new.total_area).mean()
    df_new.living_area.fillna(round(df_new.total_area * living_ratio, 1), inplace=True)
    df_new.kitchen_area.fillna(round(df_new.total_area * kitchen_ratio, 1), inplace=True)
    return df_new


def adjust_completion_date(df):
    df_new = df.copy()
    df_new.loc[:, 'completion_date'] = df_new['completion_date'].apply(lambda x: (x
                                                                       .replace('1 кв.', '')
                                                                       .replace('2 кв.', '')
                                                                       .replace('3 кв.', '')
                                                                       .replace('4 кв.', '')
                                                                       .strip()) if type(x) == str else x)
    df_new.completion_date.astype(int, errors='ignore')
    return df_new


def adjust_floor_number(df):
    df_new = df.copy()
    df_new.floor_number = df_new.floor_number.apply(lambda x: int(x[:2]))
    return df_new


def adjust_ceiling_high(df):
    df_new = df.copy()
    df_new.ceiling_high = df_new.ceiling_high.apply(lambda x: float(x
                                                                    .replace('м', '')
                                                                    .replace(',', '.'))
                                                    if type(x) == str else x)
    return df_new


def adjust_house_type(df):
    df_new = df.copy()
    df_new.house_type = df_new.house_type.apply(get_house_type)
    return df_new


def get_house_type(house_type):
    if type(house_type) != str:
        return None

    if house_type.startswith("Монолитный"):
        return "Монолитный"
    elif house_type.startswith("Монолитно"):
        return "Монолитно-кирпичный"
    elif house_type.startswith("Панельный"):
        return "Панельный"
    elif house_type.startswith("Кирпичный"):
        return "Кирпичный"
    else:
        return house_type


def adjust_price(df):
    df_new = df.copy()
    df_new.price = df_new.price.apply(lambda x: int(x
                                                    .replace(' ', '')
                                                    .replace('₽', '')))
    return df_new
