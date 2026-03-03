from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index_0.html')

@app.route('/training/<prof>')
def profile(prof):
    return render_template('index_2.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')