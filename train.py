import pandas as pd
import pickle # joblib

from helper.data_check_preparation import read_and_check_data
from helper.feature_engineering import feature_engineering
from helper.constant import TRAIN_COLUMN, PATH, COLUMN_CHANGE
from helper.data_info import DataInfo


def train_data():
    # pembacaan dan pengecekan data
    df = read_and_check_data(PATH, TRAIN_COLUMN)
    # print(df)

    data_info = DataInfo(df)
    # top 10
    print("Head of Dataframe")
    print(data_info._top(10))
    print("")
    # describe
    print("Statistics of Columns")
    print(data_info._data_statistics())
    print("")
    # data info
    print("Dataframe Info")
    print(data_info._data_dtype())
    print("")
    # percentage of null
    print("Percentage of Null Values")
    print(data_info._percentage_of_null_val())
    print("")

    
    # feature engineering
    df_transformed = feature_engineering(df, COLUMN_CHANGE)
    print("Start Saving Result Feature Engineering!")
    df_transformed.to_csv("artifacts/df_transformed.csv")
    
if __name__ == "__main__":
    print("START RUNNING PIPELINE!")
    train_data()
    print("FINISH RUNNING PIPELINE!")