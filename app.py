from flask import Flask, render_template
from utils import load_article

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/article/test/')
def view_article():
    title = 'test'
    content = load_article(title)
    return render_template('article.html', title=title, content=content)

if __name__ == '__main__':
    app.run(debug=True)
