import sqlite3
from flask import Flask
import random
app = Flask(__name__)

@app.route("/read/<topicid>")
def read(topicid): 
    cnt = sqlite3.connect('topics.db')
    result = cnt.execute('SELECT * FROM topic')
    topics = result.fetchall()   

    nav = '<ul>'
    for topic in topics:
        nav = nav + '<li><a href="/read/'+str(topic[0])+'">'+topic[1]+'</a></li>'
    nav = nav + '</ul>'

    result = cnt.execute('SELECT * FROM topic WHERE id='+topicid)
    topic = result.fetchone()
    print('topic', topic)
    content = '<h2>'+topic[1]+'</h2>'+topic[2]
    
    content = '''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                '''+nav+'''
                '''+content+'''
                <p><a href="/create">create</a></p>
            </body>
        </html>
    '''
    return content

@app.route("/create")
def create():    
    cnt = sqlite3.connect('topics.db')
    result = cnt.execute('SELECT * FROM topic')
    topics = result.fetchall()
    print('topics', topics)

    nav = '<ul>'
    for topic in topics:
        nav = nav + '<li><a href="/read/'+str(topic[0])+'">'+topic[1]+'</a></li>'
    nav = nav + '</ul>'
    
    content = '''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                '''+nav+'''
                <h2>Welcome</h2>
                Hello, WEB!
                <p><a href="/create">create</a></p>
            </body>
        </html>
    '''
    return content

@app.route("/")
def home():
    cnt = sqlite3.connect('topics.db')
    result = cnt.execute('SELECT * FROM topic')
    topics = result.fetchall()
    print('topics', topics)

    nav = '<ul>'
    for topic in topics:
        nav = nav + '<li><a href="/read/'+str(topic[0])+'">'+topic[1]+'</a></li>'
    nav = nav + '</ul>'
    
    content = '''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                '''+nav+'''
                <h2>Welcome</h2>
                Hello, WEB!
                <p><a href="/create">create</a></p>
            </body>
        </html>
    '''
    return content


app.run(debug=True)