import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVR


def get_model_with_metrics(X, y, numerical_columns, categorical_columns, model, model_params):
    X_train, X_test, y_train, y_test = transform_and_split(X, y,
                                                           numerical_columns, categorical_columns)

    grid_searcher = train_model(X_train, y_train, model, model_params)

    MSE, RMSE = evaluate_metrics(grid_searcher.best_estimator_, X_test, y_test)

    return grid_searcher.best_estimator_, grid_searcher.best_params_, MSE, RMSE


def transform_and_split(X, y, numerical_columns, categorical_columns, test_size=0.2):
    transformer = ColumnTransformer([("StandardScaler", StandardScaler(), numerical_columns),
                                     ("One hot", OneHotEncoder(sparse=False), categorical_columns)],
                                    remainder="passthrough")

    X = transformer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=test_size,
                                                        random_state=13)
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train, model, model_params):
    if model == 'Ridge':
        model = Ridge(random_state=13)
    elif model == 'KNN':
        model = KNeighborsRegressor()
    elif model == 'SVR':
        model = SVR()
    else:
        raise AttributeError("choose one of the following models: 'Ridge', 'KNN' or 'SVR'")

    grid_searcher = GridSearchCV(model, param_grid=model_params, cv=5)
    grid_searcher.fit(X_train, y_train)

    return grid_searcher


def evaluate_metrics(estimator, X_test, y_test):
    MSE = mean_squared_error(y_test, estimator.predict(X_test))
    RMSE = np.sqrt(MSE)
    return round(MSE, 3), round(RMSE, 3)
