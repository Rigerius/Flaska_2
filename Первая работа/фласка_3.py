from flask import Flask
from data import db_session
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/flask_3-3.db")
    db_sess = db_session.create_session()
    work = Jobs()
    work.team_leader = 1
    work.job = "Развертывание модулей 1, 5 и 6"
    work.work_size = 21
    work.collaborators = '2, 3'
    work.start_date = datetime.datetime.now()
    work.is_finished = False
    db_sess.add(work)
    db_sess.commit()
    # app.run()

if __name__ == '__main__':
    main()
