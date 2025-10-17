from model import *
from webserver import Webserver

def train_naives_bayes():
    x, y = read_trainings_data('Training/spam.csv')
    resampled_x, resampled_y = oversample_trainings_data(x, y)
    train_model(resampled_x, resampled_y)


if __name__ == "__main__":
    print("Model training started...")
    train_naives_bayes()
    print("Model training finished...")
    print("Starting webserver...")
    web_server = Webserver()
    web_server.starting_webserver()

