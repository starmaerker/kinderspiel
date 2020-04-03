from flask import Flask, render_template, request, url_for, redirect, make_response
import random_datetime

app = Flask(__name__)


@app.route('/')
def index():
    first, second, delta = random_datetime.calc()

    return render_template('index.html', first=first, second=second, delta=delta)


if __name__ == '__main__':
    app.run(debug=True)
