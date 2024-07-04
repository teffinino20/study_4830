import pandas as pd


def columns_df(df: pd.DataFrame):
    int_columns = list(df.select_dtypes(include='int').columns)
    float_columns = list(df.select_dtypes(include='float').columns)
    object_columns = list(df.select_dtypes(include='object').columns)
    numerical_columns = int_columns + float_columns

    print('Shape:', df.shape)
    print('Numerical features: ', len(numerical_columns))
    print('Categorical features: ', len(object_columns))

    return int_columns, float_columns, object_columns, numerical_columns


