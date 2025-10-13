import numpy as np
import pandas as pd
from imblearn.over_sampling import RandomOverSampler

def read_trainings_data(path):
    try:
        read_csv =  pd.read_csv(path,  encoding='latin1') # Downloaded from Kaggle.com
        x = read_csv["v1"].tolist()
        y = read_csv["v2"].tolist()
        return x,y
    except FileNotFoundError:
        print("File not found - Please check the folder name")
        return None,None

def oversample_trainings_data(x,y):
    x_array = np.array(x).reshape(-1, 1) #Convert 1D-Array to 2D-Array
    X_res, y_res = RandomOverSampler(random_state=42).fit_resample(x_array, y)

    return X_res, y_res



if __name__ == "__main__":
    x, y = read_trainings_data('Training/spam.csv')
    resampled_x , resampled_y = oversample_trainings_data(x,y)
