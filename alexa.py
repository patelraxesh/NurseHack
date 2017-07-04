from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/")

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, how are you Jennifer?'
    return question(welcome_message)

@ask.intent("BensweightBensbloodpressure")
def share_headlines():
    headlines = 187
    headline_msg = 'Bens last recorded weight was {} pound'.format(headlines)
    return statement(headline_msg)

@ask.intent("Bensbloodpressure")
def share_headlines():
    headlines = 120
    headline_msg = 'Bens last recorded blood pressure was {} which is normal'.format(headlines)
    return statement(headline_msg)

@ask.intent("Mymedication")
def no_intent():
    bye_text = 'You need to take 1 tablet of Bumetanide at 9 pm after eating today'
    return statement(bye_text)



if __name__ == '__main__':
    app.run(debug=True)

