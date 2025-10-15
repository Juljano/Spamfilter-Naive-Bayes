import threading
from model import *
import subprocess

def run_streamlit_app():
    try:
        python_path = r"C:\Users\JML\AppData\Local\Programs\Python\Python312\python.exe"
        script_path = r"C:\Users\JML\KI - Projekte\Spamfilter-Naive-Bayes\gui.py"
        result = subprocess.Popen([python_path, "-m", "streamlit", "run", script_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        if result:
            for line in result.stdout:
                if line.strip().startswith("User-input:"):
                    print(line.strip())
                    rating_message(line.strip())
    except Exception as error:
        print(F"Something went wrong {error}")

def rating_message(user_input):
    x, y = read_trainings_data('Training/spam.csv')
    resampled_x, resampled_y = oversample_trainings_data(x, y)
    model, vectorizer = train_model(resampled_x, resampled_y)
    if model and vectorizer:
        ask_model(vectorizer, model, user_input)


if __name__ == "__main__":
    streamlit_thread = threading.Thread(target=run_streamlit_app())
    streamlit_thread.start()

