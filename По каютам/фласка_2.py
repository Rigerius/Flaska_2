from flask import Flask, render_template

app = Flask(__name__)

s = ['Алексей', "Михаил", "Александр", "Андрей", "Николай", "Максим", "Аркадий"]

@app.route('/distribution')
def f():
    return render_template('index_6.html', sp=s)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')