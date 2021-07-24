import numpy as np
import pandas as pd
from constants import selection_threshold


def create_features_and_target1(df):
    ds_district = get_district_feature(df, selection_threshold)
    ds_house_type = get_house_type_feature(df, selection_threshold)
    ds_subway_summary = get_subway_summary(df)

    X = pd.concat(
        [
            ds_district,
            df.housing_type,
            ds_house_type,
            df.total_area,
            ds_subway_summary
        ],
        axis=1
    )
    X.reset_index(drop=True, inplace=True)
    return X, df.price.apply(np.log1p)


def create_features_and_target2(df):
    ds_district = get_district_feature(df, selection_threshold)
    ds_house_type = get_house_type_feature(df, selection_threshold)
    ds_subway_summary = get_subway_summary(df)
    ds_build_date_1995_2010 = df.house_build_date.apply(lambda x: x if (1995 <= x < 2010) else 0).rename(
        'build_date_1995_2010')
    ds_build_date_2010_2022 = df.house_build_date.apply(lambda x: x if (2010 <= x < 2022) else 0).rename(
        'build_date_2010_2022')
    ds_build_date_2022_plus = df.house_build_date.apply(lambda x: x if 2022 <= x else 0).rename(
        'build_date_2022_plus')

    X = pd.concat(
        [
            ds_district,
            df.housing_type,
            ds_house_type,
            df.total_area,
            ds_build_date_1995_2010,
            ds_build_date_2010_2022,
            ds_build_date_2022_plus,
            ds_subway_summary
        ],
        axis=1
    )
    X.reset_index(drop=True, inplace=True)
    return X, df.price.apply(np.log1p)


def create_features_and_target3(df):
    ds_district = get_district_feature(df, selection_threshold)
    ds_house_type = get_house_type_feature(df, selection_threshold)
    ds_subway_summary = get_subway_summary(df)
    ds_build_date_1995_2010 = df.house_build_date.apply(lambda x: x if (1995 <= x < 2010) else 0).rename(
        'build_date_1995_2010')
    ds_build_date_2010_2022 = df.house_build_date.apply(lambda x: x if (2010 <= x < 2022) else 0).rename(
        'build_date_2010_2022')
    ds_build_date_2022_plus = df.house_build_date.apply(lambda x: x if 2022 <= x else 0).rename('build_date_2022_plus')
    ds_floor_number_1_5 = df.floor_number.apply(lambda x: x if x <= 5 else 0).rename('floor_number_1_5')
    ds_floor_number_5_12 = df.floor_number.apply(lambda x: x if (5 < x <= 12) else 0).rename('floor_number_5_12')

    X = pd.concat(
        [
            ds_district,
            df.housing_type,
            ds_house_type,
            df.total_area,
            ds_build_date_1995_2010,
            ds_build_date_2010_2022,
            ds_build_date_2022_plus,
            ds_floor_number_1_5,
            ds_floor_number_5_12,
            ds_subway_summary
        ],
        axis=1
    )
    X.reset_index(drop=True, inplace=True)
    return X, df.price.apply(np.log1p)


def get_district_feature(df, threshold):
    big_districts = df.district.value_counts()[df.district.value_counts() > threshold].index
    ds_district = df.district.apply(lambda x: x if x in big_districts else "another")
    return ds_district


def get_house_type_feature(df, threshold):
    big_types = df.house_type.value_counts()[df.house_type.value_counts() > threshold].index
    ds_house_type = df.house_type.apply(lambda x: x if x in big_types else "another")
    return ds_house_type


def get_subway_summary(df):
    subway_type = df.subway_type.apply(lambda x: 'f' if x == 'on foot' else 't')
    subway_time = df.subway_time.apply(get_subway_time)
    return pd.Series(subway_type + ':' + subway_time, name='subway_summary')


def get_subway_time(x):
    if 0 <= x < 5:
        return '0-5'
    elif x < 10:
        return '5-10'
    elif x < 15:
        return '10-15'
    else:
        return '15+'
