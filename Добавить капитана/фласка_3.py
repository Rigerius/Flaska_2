from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

team = [['Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org'],
        ['Остроухов', "Николай", 17, "Инженер", "Специалист по радиационной защите",
         "Модуль №6", "Nick.ostr@mars.com"],
        ["Мазуркевич", "Максимиллиан", 14, "Инженер", "Технический специалист по космическим станциям",
         "Модуль №6", "max.max@mars.com"],
        ["Фокша", "Влад", 17, "Программист", "Программист", "Модуль №6", "foksha_v@mars.com"]]

def main():
    db_session.global_init("db/flask_3-3.db")
    db_sess = db_session.create_session()
    for i in team:
        user = User()
        user.surname = i[0]
        user.name = i[1]
        user.age = i[2]
        user.position = i[3]
        user.speciality = i[4]
        user.address = i[5]
        user.email = i[6]
        db_sess.add(user)
        db_sess.commit()
    # app.run()

if __name__ == '__main__':
    main()
