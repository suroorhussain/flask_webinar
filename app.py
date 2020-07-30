from flask import Flask, render_template, request, redirect, url_for
from utils import load_article, save_article

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/article/<title>/')
def view_article(title):
    content = load_article(title)
    return render_template('article.html', title=title, content=content)

@app.route('/write/', methods=['GET', 'POST'])
def write_article():
    if request.method == 'GET':
        return render_template('write.html')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        save_article(title, content)
        return redirect(url_for('view_article', title=title))

if __name__ == '__main__':
    app.run(debug=True)
