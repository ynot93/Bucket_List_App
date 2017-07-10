from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def Sign_Up():
    return


if __name__ == '__main__':
    app.run()


class User:
    def __init__(self, first_name, last_name, password):
        self.__firstName = first_name
        self.__lastName = last_name
        self.__Password = password


