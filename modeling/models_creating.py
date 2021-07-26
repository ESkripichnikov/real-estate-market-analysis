import csv
from tqdm import tqdm
import pandas as pd
from modeling.feature_extraction import create_features_and_target1,\
    create_features_and_target2, create_features_and_target3
from constants import models, categorical_columns,\
    numerical_columns, model_params, modeling_results_fields
from modeling_steps_functions import get_model_with_metrics
from joblib import dump

features_sets = {'standard_features': create_features_and_target1,
                 'house_build_date_included': create_features_and_target2,
                 'floor_number_included': create_features_and_target3}

df = pd.read_csv('../preprocessed_dataframes/apartments.csv', index_col='id')

with open('../models_storage/modeling_results.csv', 'a+', newline='') as results_file:
    writer = csv.DictWriter(results_file, fieldnames=modeling_results_fields)
    writer.writeheader()

    for model in tqdm(models):
        for feature_type, create_features_func in features_sets.items():
            X, y = create_features_func(df)

            best_estimator, best_params, LMSE, LRMSE, R2 = get_model_with_metrics(X, y,
                                                                                  numerical_columns[feature_type],
                                                                                  categorical_columns[feature_type],
                                                                                  model, model_params[model])

            model_name = str(model) + '_' + str(feature_type)
            dump(best_estimator, f'../models_storage/{model_name}.joblib')

            modeling_results = {
                'model_type': model,
                'feature_type': feature_type,
                'optimal_params': best_params,
                'LMSE': LMSE,
                'LRMSE': LRMSE,
                'R-Squared': R2
            }

            writer.writerow(modeling_results)
