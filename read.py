import sqlite3
cnt = sqlite3.connect('topics.db')
result = cnt.execute('SELECT * FROM topic')
topics = result.fetchall()
print('topics', result, topics)
