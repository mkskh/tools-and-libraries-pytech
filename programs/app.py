from flask import Flask
import datetime

app = Flask(__name__)

# @app.route('/')
# def display_date_time():
#     current_date_time = datetime.datetime.now()
#     return f'The current date and time is: {current_date_time}'

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)