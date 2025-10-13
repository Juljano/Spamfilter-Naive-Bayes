import threading
from model import *
import subprocess

def run_streamlit_app():
    python_path = r"C:\Users\JML\AppData\Local\Programs\Python\Python312\python.exe"
    script_path = r"C:\Users\JML\KI - Projekte\Spamfilter-Naive-Bayes\gui.py"
    result = subprocess.run([python_path, "-m", "streamlit", "run", script_path],capture_output=True, text=True)

    #rating_message(user_input)

def rating_message(user_input):
    x, y = read_trainings_data('Training/spam.csv')
    resampled_x, resampled_y = oversample_trainings_data(x, y)
    model, vectorizer = train_model(resampled_x, resampled_y)

    if model and vectorizer:
        aks_model(vectorizer, model, user_input)


if __name__ == "__main__":
    run_streamlit_app()
    streamlit_thread = threading.Thread(target=run_streamlit_app())
    streamlit_thread.start()

