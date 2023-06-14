# Real Estate Market Analysis #

## Project Description ##

This project is a analysis of the residential real estate market in Moscow and consists of the following parts:

1. **Data Scraping from [CIAN](https://www.cian.ru) website**
   
   At this stage, information on 10,000 real estate sale listings was obtained. In order to obtain a representative sample, the structure of the obtained data (proportion of primary and secondary housing, proportion of 1, 2, 3-room apartments, etc.) was determined according to the structure of the entire residential real estate market in Moscow.

2. **Data Preprocessing**

   Handling missing values, transforming the raw data into a convenient format for further analysis, preliminary feature selection for future models.

3. **Exploratory Data Analysis**

   Visualization of the obtained data, calculation of various statistics and their analysis, creation of additional features.

4. **Building Apartment Price Prediction Models**

   This includes building Ridge regression, KNeighborsRegressor, and Support Vector Regression models. Tuning the hyperparameters for each model and selecting the best model among the presented ones. Also, analyzing the coefficients of the resulting Ridge regression model to identify the features that have the most positive and negative impact on the apartment price.

## Research Results ##

The main features selected for building apartment price prediction models are as follows:
- 12 administrative districts of Moscow
- Type of housing (newly built or secondary)
- Type of building (panel, monolithic, brick, monolithic-brick, and others)
- Total area of the apartment in square meters
- Categorical variable containing information about the nearest metro: mode of reaching the nearest metro (by walking or by transportation) and time to the nearest metro in minutes (time intervals 0-5, 5-10, 10-15, 15+).

In addition to the main features, the construction date of the building and the floor number of the apartment were used for building additional models.

*The following table shows the modeling results:*

| Model:        | Ridge              |                    |                 | KNN                 |                     |                     | SVR                                        |                                             |                                             |
|--------------|-------------------|-------------------|----------------|--------------------|--------------------|--------------------|-------------------------------------------|--------------------------------------------|--------------------------------------------|
| Features:     | standart features  | + house buld date  | + floor number  | standart features   | + house buld date   | + floor number      | standart features                          | + house buld date                           | + floor number                              |
| Optim params  | {'alpha': 1.0}     | {'alpha': 1.0}     | {'alpha': 1.0}  | {'n_neighbors': 3}  | {'n_neighbors': 3}  | {'n_neighbors': 5}  | {'C': 1, 'epsilon': 0.1, 'kernel': 'rbf'}  | {'C': 10, 'epsilon': 0.1, 'kernel': 'rbf'}  | {'C': 10, 'epsilon': 0.1, 'kernel': 'rbf'}  |
| LMSE          | 0.184053           | 0.178878           | 0.178739        | 0.098854            | 0.106193            | 0.146651            | 0.092428                                   | 0.086377                                    | 0.081788                                    |
| LRMSE         | 0.429014           | 0.422940           | 0.422776        | 0.314410            | 0.325873            | 0.382951            | 0.304020                                   | 0.293899                                    | 0.285986                                    |
| R-Squared     | 0.831380           | 0.836121           | 0.836248        | 0.909435            | 0.902711            | 0.865645            | 0.915322                                   | 0.920866                                    | 0.925070                                    |

**Thus, the best model is Support Vector Regression with an R-squared of 0.925**


*The following graph shows the coefficients of the Ridge Regression model:*

![ridge_coeff](ridge_coeff.png)

**Based on this graph, the following features have the strongest impact on the price:**
- Total area of the apartment (+)
- Location of the apartment within the Central Administrative District (+)
- Monolithic-brick type of building (+)
- Location of the apartment within a 5-15 minutes walking distance from the nearest metro (+)
- Location of the apartment within the Northwestern Administrative District or the Southeastern Administrative District (-)
- Location of the apartment more than 15 minutes away by transportation from the nearest metro (-)

**For more detailed results and analysis, please refer to the apartments_data_analysis.ipynb file.**

## Project Structure ##

*This project is structured into the following modules:*
- **parsers**
  - apartments_links_parser.py - main functions for collecting apartment links
  - apartments_info_parser.py - main functions for parsing apartment listings
  - data_collection.py - performs apartment link collection and parsing
- **apartments_data**
  - apartments_links.csv - contains the collected apartment links
  - apartments_database.csv - contains all the gathered information about the apartments
- **data_preprocessing**
  - preprocessing.py - main functions for preprocessing the parsed data
  - get_preprocessed_dataframes.py - generates preprocessed dataframes ready for exploratory analysis
- **preprocessed_dataframes**
  - apartments.csv - contains preprocessed data for all apartments
  - secondary_apartments.csv - contains preprocessed data only for secondary housing
- **modeling**
  - feature_extraction.py - functions for feature extraction
  - modeling_steps_functions.py - functions describing the steps of model building
  - models_creating.py - builds the models, records their results, and saves them
- **models_storage** - contains the modeling results in modeling_results.csv, as well as all the built models in .joblib format
- **tests**
  - parser_test.py - unit tests for data parsers
  - test_constants.py - contains constants used for testing
- **apartments_data_analysis.ipynb** - exploratory data analysis with necessary visualizations
