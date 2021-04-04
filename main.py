from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    a = [db_sess.query(User).filter(User.id == i.team_leader)[0] for i in jobs]
    a = [f'{i.surname} {i.name}'for i in a]
    return render_template("index.html", jobs=jobs, a=a)


if __name__ == '__main__':
    app.run()