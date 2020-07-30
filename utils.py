import os

WIKI_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wiki')

def save_article(title, content):
    filename = '{}.txt'.format(title)
    with open(os.path.join(WIKI_DIR, filename), 'w') as f:
        f.write(content)

def load_article(title):
    filename = '{}.txt'.format(title)
    with open(os.path.join(WIKI_DIR, filename), 'r') as f:
        content = f.read()
    return content

def list_articles():
    return os.listdir(WIKI_DIR)
