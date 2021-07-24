import pandas as pd
import preprocessing as prc

df = prc.read_initial_dataframe()
# drop useless features
df.drop(columns=['city', 'region', 'street', 'house'], inplace=True)
# drop few apartments without target variable
df.dropna(subset=['price', 'nearest_subway', 'nearest_subway_time'], inplace=True)
df = prc.adjust_housing_type(df)

df = prc.adjust_nearest_subway_time(df)
df.drop(columns=['nearest_subway_time'], inplace=True)

df = prc.adjust_districts(df)

df_primary, df_secondary = prc.split_on_primary_secondary(df)
df_primary = prc.drop_columns_with_many_nans(df_primary, 0.35, ['house_type'])

df_primary = prc.adjust_areas(df_primary)
df_primary = prc.fillna_areas(df_primary)

df_primary = prc.adjust_completion_date(df_primary)
df_primary.completion_date.fillna(df_primary.completion_date.median(), inplace=True)

df_primary = prc.adjust_floor_number(df_primary)

df_primary = prc.adjust_house_type(df_primary)
df_primary.house_type.fillna('Панельный', inplace=True)

df_primary = prc.adjust_price(df_primary)

df_secondary = prc.drop_columns_with_many_nans(df_secondary, 0.4)

df_secondary.drop(columns=['bathroom_type', 'window_view', 'build_date',
                           'overlap_type', 'heating', 'elevators', 'emergency',
                           'apartment_renovation', 'entrances'], inplace=True)

df_secondary.house_build_date.fillna(int(df_secondary.house_build_date.mean()), inplace=True)

df_secondary = prc.adjust_house_type(df_secondary)
df_secondary.house_type.fillna('Панельный', inplace=True)

df_secondary = prc.adjust_areas(df_secondary)
df_secondary = prc.fillna_areas(df_secondary)

df_secondary = prc.adjust_floor_number(df_secondary)

df_secondary = prc.adjust_price(df_secondary)

apartments_df = pd.concat([df_primary.rename(columns={'completion_date': 'house_build_date'}), df_secondary])
apartments_df.house_build_date = apartments_df.house_build_date.astype(int)
apartments_df = apartments_df[['district', 'housing_type', 'house_type',
                               'house_build_date', 'floor_number', 'total_area',
                               'living_area', 'kitchen_area',
                               'nearest_subway', 'subway_type', 'subway_time', 'price']]
apartments_df.to_csv("../preprocessed_dataframes/apartments.csv")


# getting separate secondary apartments dataframe
_, df_secondary2 = prc.split_on_primary_secondary(df)
df_secondary2 = prc.drop_columns_with_many_nans(df_secondary2, 0.5)
# drop useless features
df_secondary2.drop(columns=['housing_type', 'overlap_type', 'emergency',
                            'bathroom_type', 'build_date', 'elevators'], inplace=True)

df_secondary2 = prc.adjust_areas(df_secondary2)
df_secondary2 = prc.fillna_areas(df_secondary2)

df_secondary2 = prc.adjust_floor_number(df_secondary2)

df_secondary2.apartment_renovation.fillna('Без ремонта', inplace=True)

df_secondary2.house_build_date.fillna(int(df_secondary2.house_build_date.mean()), inplace=True)

df_secondary2.house_type.fillna('Панельный', inplace=True)

df_secondary2 = prc.adjust_ceiling_high(df_secondary2)
df_secondary2.ceiling_high.fillna(df_secondary2.ceiling_high.median(), inplace=True)

df_secondary2.window_view.fillna(df_secondary2.window_view.value_counts().index[0], inplace=True)

df_secondary2.entrances.fillna(df_secondary2.entrances.median(), inplace=True)

df_secondary2.heating.fillna(df_secondary2.heating.value_counts().index[0], inplace=True)

df_secondary2 = prc.adjust_price(df_secondary2)

df_secondary2.house_build_date = df_secondary2.house_build_date.astype(int)
df_secondary2.entrances = df_secondary2.entrances.astype(int)
df_secondary2 = df_secondary2[['district', 'house_type', 'house_build_date', 'floor_number',
                               'entrances', 'heating', 'window_view', 'ceiling_high',
                               'apartment_renovation', 'total_area', 'living_area',
                               'kitchen_area', 'nearest_subway', 'subway_type', 'subway_time', 'price']]
df_secondary2.to_csv("../preprocessed_dataframes/secondary_apartments.csv")
