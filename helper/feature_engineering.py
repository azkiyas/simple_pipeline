import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize
from helper.preprocessing import CategoricalFeatures

def feature_engineering(df, column):
    # rename column
    df = df.rename(columns=column)
    print("Dataframe after rename columns")
    print(df)
    print("")

    # astype ad_created and date_crawled and last_seen
    df['ad_created'] = pd.to_datetime(df['ad_created'])
    df['date_crawled'] = pd.to_datetime(df['date_crawled'])
    df['last_seen'] = pd.to_datetime(df['last_seen'])

    print("info change type of ad_created and date_crawled and last_seen to datetime")
    print(df[["ad_created", "date_crawled", "last_seen"]].info())
    print("")

    # string manipulation price
    df["price"] = df["price"].str.replace("$","", regex=False)
    df["price"] = df["price"].str.replace(",","")
    
    # string manipulation odometer
    df["odometer"] = df["odometer"].str.replace("km","")
    df["odometer"] = df["odometer"].str.replace(",","")

    # astype to int64
    df["price"] = df["price"].astype('int64')
    df["odometer"] = df["odometer"].astype('int64')

    print("dataframe after manipulation")
    print(df[["price", "odometer"]].info())
    print(df[["price", "odometer"]])
    print("")

    # get value counts of columns
    for column in df:
        if df[column].dtype == object:
            value_column = df[column].value_counts()
            print("value count of ", column)
            print(value_column)
            print("")
    
    # drop columns
    df = df.drop(['seller', 'offer_type', 'num_of_pictures', 'name', 'postal_code'], axis=1)
    print("dataframe after drop seller and offer_type and num_of_pictures and name and postal_code")
    print(df.info())
    print("")

    # checking outlier price
    print("dataframe check outlier of price")
    print(df['price'].sort_values())
    print("")

    # filtering price
    print("filtering price range 500 until 40000")
    df = df[(df['price']>=500) & (df['price']<=40000)]
    print(df['price'].sort_values())
    print("")

    # fill null values
    for column in df:
        if df[column].dtype == object:
            df[column] = df[column].fillna(df[column].mode()[0])
        if df[column].dtype == 'int64':
            df[column] = df[column].fillna(df[column].median())
    print("info total value per column after replace null value")
    print(df.info())
    print("")

    # normalization
    col_tobe_normalize = ['power_ps', 'odometer']

    df[col_tobe_normalize] = normalize(X=df[col_tobe_normalize], norm="l2", axis=1)
    print("dataframe after normalize numerical data")
    print(df.head())
    print("")

    # encoding nominal values
    cols = [c for c in df.columns if (df[c].dtype == object)]
    cat_feats = CategoricalFeatures(df, categorical_features=cols, encoding_type="get_dum", handle_na=True)
    print(cat_feats.fit_transform())
    df_transform = cat_feats.fit_transform()

    return df_transform