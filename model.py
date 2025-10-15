import numpy as np
import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

def read_trainings_data(path):
    try:
        read_csv =  pd.read_csv(path,  encoding='latin1') # Downloaded from Kaggle.com
        x = read_csv["v2"].tolist()
        y = read_csv["v1"].tolist()
        return x,y
    except FileNotFoundError:
        print("File not found - Please check the folder name")
        return None,None

def oversample_trainings_data(x,y):
    x_array = np.array(x).reshape(-1, 1) #Convert 1D-Array to 2D-Array
    X_res, y_res = RandomOverSampler(random_state=42).fit_resample(x_array, y) #duplicate spam-messages (x)
    return X_res.flatten().tolist(), y_res


def train_model(x, y):
    vectorizer = CountVectorizer()
    x_vector = vectorizer.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_vector, y, test_size=0.2, random_state=42)

    model = MultinomialNB()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(f"Genauigkeit: {accuracy:.2f}")
    print(classification_report(y_test, y_pred))

    return model, vectorizer


def ask_model(vectorizer, model, user_input):
    new_input = [user_input]
    new_vector = vectorizer.transform(new_input)
    prediction = model.predict(new_vector)

    print(f"Vorhersage für '{new_input[0]}': {prediction[0]}")

    if prediction[0] == "spam":
        print("Diese Nachricht ist leider Spam - Bitte sofort Löschen!")
    elif prediction[0] == "ham":
        print("Diese Nachricht ist Vertrauenswürdig - Weitermachen Kollege!")



