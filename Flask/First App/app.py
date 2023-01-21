from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    intro = db.Column(db.String(255), nullable = False)
    text = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


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


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/read-article')

        except:
            return 'Input Error'

    else:
        return render_template('create-article.html')


@app.route('/read-article')
def read_article():
    try:
        articles = Article.query.order_by(Article.date.desc()).all()
        return render_template('read-article.html', articles=articles)
    except:
        return 'DB Error'


@app.route('/read-article/<int:id>')
def read_article_detail(id):
    article = Article.query.get(id)
    return render_template('read-article-detail.html', article=article)


@app.route('/read-article/<int:id>/edit', methods=['POST', 'GET'])
def read_article_edit(id):
    article = Article.query.get(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/read-article')

        except:
            return 'Input Error'

    else:
        return render_template('read-article-edit.html', article=article)


@app.route('/read-article/<int:id>/delete')
def read_article_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/read-article')

    except:
        return 'Delete Error'


if __name__ == '__main__':
    app.run(debug=True)