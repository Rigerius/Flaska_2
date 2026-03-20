from flask import Flask, render_template

app = Flask(__name__)

s = ['Алексей', "Михаил", "Александр", "Андрей", "Николай", "Максим", "Аркадий"]

@app.route('/table/<pol>/<int:age>')
def f(pol, age):
    return render_template('index_7.html', pol=pol, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')