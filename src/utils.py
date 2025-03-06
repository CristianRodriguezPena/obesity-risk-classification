import pandas as pd
from typing import Literal



def standardize(series: pd.Series) -> pd.Series:
    '''
    Standardize a pandas Series by subtracting the mean and dividing by the standard deviation.

    Parameters
    ----------
    series : pd.Series
        The pandas Series to standardize.

    Returns
    -------
    pd.Series
        The standardized pandas Series.
    '''

    return (series - series.mean()) / series.std()
def get_outliers(series: pd.Series, method: Literal["iqr", "z-score", "percentile"]="iqr", custom_threshold: float=None) -> pd.Series:
    '''
    Function to detect outliers in a pandas Series using either the IQR or Z-score method.

    Parameters
    ----------
    series : pd.Series
        The pandas Series to detect outliers in.
    method : Literal["iqr", "z-score"]
        The method to use for outlier detection. Defaults to "iqr".
    custom_threshold : float
        If method is "iqr", this is the multiple of the IQR to use to detect outliers. 
        If method is "z-score", this is the multiple of the standard deviation to use to detect outliers. 
        Defaults to None, which means 1.5 for IQR and 3 for Z-score.
        If method is "percentile", this is the 99th percentile to use to detect outliers.

    Returns
    -------
    pd.Series
        A boolean Series of the same size as the input indicating which values are outliers.
    '''

    if method == "iqr":
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        if custom_threshold is None:
            outliers_mask = (series < (Q1 - 1.5 * IQR)) | (series > (Q3 + 1.5 * IQR))
        else:
            outliers_mask = (series < (Q1 - custom_threshold * IQR)) | (series > (Q3 + custom_threshold * IQR))
    elif method == "z-score":
        zscore = standardize(series)
        if custom_threshold is None:
            outliers_mask = (zscore < -3) | (zscore > 3)
        else:
            outliers_mask = (zscore < -custom_threshold) | (zscore > custom_threshold)
    elif method == "percentile":
        if custom_threshold is None:
            outliers_mask = series > series.quantile(0.99)
        else:
            outliers_mask = series > series.quantile(custom_threshold)
        
    return series[outliers_mask]