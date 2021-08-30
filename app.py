import sqlite3
from flask import Flask
import random
app = Flask(__name__)

@app.route("/read/<topicid>")
def read(topicid): 
    cnt = sqlite3.connect('topics.db')
    result = cnt.execute('SELECT * FROM topic')
    topics = result.fetchall()
    print('topics', topics)

    nav = '<ol>'
    for topic in topics:
        nav = nav + '<li><a href="/read/'+str(topic[0])+'">'+topic[1]+'</a></li>'
    nav = nav + '</ol>'
    
    content = '''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                '''+nav+'''
                <h2>Welcome</h2>
                Hello, WEB!
            </body>
        </html>
    '''
    return content

@app.route("/create")
def create():    
    return "<h1>Create</h1>"

@app.route("/")
def home():
    cnt = sqlite3.connect('topics.db')
    result = cnt.execute('SELECT * FROM topic')
    topics = result.fetchall()
    print('topics', topics)

    nav = '<ol>'
    for topic in topics:
        nav = nav + '<li><a href="/read/'+str(topic[0])+'">'+topic[1]+'</a></li>'
    nav = nav + '</ol>'
    
    content = '''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                '''+nav+'''
                <h2>Welcome</h2>
                Hello, WEB!
            </body>
        </html>
    '''
    return content


app.run(debug=True)