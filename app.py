import os

from flask import Flask, render_template, jsonify
from translate import Translator

app = Flask(__name__)
LANGUAGES = {
    'en': 'english',
    'mr': 'marathi',
    'kn': 'kannada',
    'hi': 'hindi',
    'bn': 'bengali',
    'ta': 'tamil',
    'te': 'telugu',
    'ml': 'malayalam'
}

@app.route("/", methods=['GET'])
def HelloWorld():
    return render_template('index.html', items = makeTranslation("Hello"), word = "Hello") 

@app.route("/translate/<string:word>", methods=['GET'])
def web_traslate(word):
    return render_template('index.html', items =  makeTranslation(word),word = word) 

@app.route("/JSON/<string:word>", methods=['GET'])
def web_Json(word):
    return  jsonify(makeTranslation(word))

def makeTranslation(word):
    a = {}
    for key, value in LANGUAGES.items():
        translator = Translator(to_lang=key)
        res = translator.translate(word)
        a[value] = res
    return a
    
if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)