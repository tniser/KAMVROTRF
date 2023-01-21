from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLACHEMY_DATABES_URI'] = ''

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/features')
def features():
    return render_template('features.html')


@app.route('/prices')
def prices():
    return render_template('prices.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)