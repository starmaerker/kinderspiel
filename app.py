from flask import Flask, render_template
import random_datetime

app = Flask(__name__)


@app.route('/')
def index():
    first = f'{random_datetime.hours_one}:{random_datetime.minutes_one}'
    second = f'{random_datetime.hours_two}:{random_datetime.minutes_two}'
    delta = random_datetime.delta

    return render_template('index.html', first=first, second=second, delta=delta)


if __name__ == '__main__':
    app.debug = True
    app.run()
