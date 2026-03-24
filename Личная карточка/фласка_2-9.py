from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

s = json.load(open('templates/people.json', encoding='utf-8'))


@app.route('/member')
def f():
    member = random.choice(s)
    return render_template('index_9.html', name=member['name'], file=member['file'], prof=", ".join(sorted(member['prof'])))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
