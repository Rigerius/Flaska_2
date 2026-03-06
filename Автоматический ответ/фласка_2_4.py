from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def profile():
    return render_template('index_4.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    
