import pandas as pd
import numpy as np
from sklearn import preprocessing

class DataInfo:
    def __init__(self, df):
        """
        df: pandas dataframe
        """
        self.df = df

    def _top(self, n=10):
        return self.df.head(n)

    def _data_statistics(self, include='all'):
        return self.df.describe(include=include)

    def _data_dtype(self):
        return self.df.info()
    
    def _percentage_of_null_val(self):
        return self.df.isna().sum()/len(self.df)*100