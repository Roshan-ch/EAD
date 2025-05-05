from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('users.json')
User = Query()

@app.route('/')
def index():
    return render_template('index.html', users=db.all(), search_results=[])

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    roll_no = request.form['roll_no']
    age = request.form['age']
    db.insert({'name': name, 'roll_no': roll_no, 'age': int(age)})
    return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    name = request.form['name']
    results = db.search(User.name == name)
    return render_template('index.html', users=db.all(), search_results=results)

@app.route('/delete', methods=['POST'])
def delete():
    name = request.form['name']
    db.remove(User.name == name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
