from flask import Flask, render_template
from utils import load_article

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/article/<title>/')
def view_article(title):
    content = load_article(title)
    return render_template('article.html', title=title, content=content)

@app.route('/write/')
def write_article():
    return render_template('write.html')

if __name__ == '__main__':
    app.run(debug=True)
