import sqlite3
from flask import Flask, redirect, request
import random
app = Flask(__name__)

@app.route("/create_process", methods=['POST'])
def create_process():    
    cnt = sqlite3.connect('topics.db')
    title = request.form['title']
    body = request.form['body']
    sql = "INSERT INTO topic (title, body) VALUES('"+title+"', '"+body+"')"
    cnt.execute(sql)
    cnt.commit()
    return redirect("/")

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
    
    html = '''
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
    return html

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
    
    html = '''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                '''+nav+'''
                <h2>Welcome</h2>
                <form method="post" action="/create_process">
                    <p><input type="text" name="title" placeholder="title" ></p>
                    <p><textarea name="body" placeholder="body" ></textarea></p>
                    <p><input type="submit" value="create"></p>
                </form> 
            </body>
        </html>
    '''
    return html

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