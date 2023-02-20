#!/usr/bin/python

import time
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

START = time.time()



def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

@app.route('/')
def root():
    return "Hello World (Python)! (up %s)\n" % elapsed()

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hello %s' % escape(username)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
