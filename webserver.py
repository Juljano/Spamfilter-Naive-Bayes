import threading
from flask import Flask, request, render_template
from model import ask_model

class Webserver:
    def __init__(self):
        self.app = Flask(__name__)
        self.user_input = None
        self.start()


    def start(self):
        @self.app.route('/',methods=['POST', 'GET'])
        def get_user_input():
            self.user_input = request.form.get('messageBox')
            if request.method == "POST":
                if self.user_input:
                 response = ask_model(self.user_input)
                 print(f"User: {self.user_input}")
                 if response == "ham":
                     return render_template("index.html", generateResponse=f"{response} - This message is trustworthy! Keep up the great work, colleague!", color="green") #green
                 elif response == "spam":
                     return render_template("index.html", generateResponse=f"{response} - This message has been identified as spam—please delete it immediately!", color="red") #red

            return render_template("index.html")

    def starting_webserver(self):
        thread = threading.Thread(target=self.app.run, kwargs={"debug": True, "use_reloader": False, "host": "0.0.0.0"})
        thread.start()
        thread.join()

