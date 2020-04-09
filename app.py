from flask import Flask, render_template, request, url_for, redirect, make_response
import random_datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Results

app = Flask(__name__)

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    first, second, delta_hours, delta_minutes = random_datetime.calc()

    delta = f"{delta_hours}:{delta_minutes}"

    result = Results(solution=delta, guess=delta)
    session.add(result)
    session.commit()

    return render_template('index.html', first=first, second=second, delta_hours=delta_hours, delta_minutes=delta_minutes)


if __name__ == '__main__':
    app.run(debug=True)
