from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/flask_3-3.db")
db_sess = db_session.create_session()
tables = []
for job in db_sess.query(Jobs).all():
    a = f"{db_sess.query(User).filter(User.id == job.team_leader).first().name} {db_sess.query(User).filter(User.id == job.team_leader).first().surname}"
    tables.append([job.job, a, job.work_size, job.collaborators, job.is_finished])
    print(job.is_finished)

@app.route('/')
def main():
    return render_template('flask_3-7.html', tables=tables)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
