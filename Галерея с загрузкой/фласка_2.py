from flask import Flask, render_template, request

app = Flask(__name__)

s = []


@app.route('/galery', methods=['POST', 'GET'])
def f():
    if request.method == 'GET':
        return render_template('carousel.html', s=s)
    elif request.method == 'POST':
        f = request.files['file']
        s.append(f.filename)
        return render_template('carousel.html', s=s)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')