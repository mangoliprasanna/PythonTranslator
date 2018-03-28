import os
import json
from flask import Flask, render_template, jsonify, Response
from googletrans import Translator

app = Flask(__name__)
translator = Translator()
LANGUAGES = {
    'en': 'english',
    'fr': 'french',
    'de': 'german',
    'el': 'greek',
    'mr': 'marathi',
    'kn': 'kannada',
    'hi': 'hindi',
    'bn': 'bengali',
    'ta': 'tamil',
    'te': 'telugu',
    'gu': 'gujarati',
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
    
    return json.dumps(makeTranslation(word), ensure_ascii=False).encode('utf8')
def makeTranslation(word):
    a = {}
    for key, value in LANGUAGES.items():
        res = translator.translate(word, dest=key)
        a[value] = res.text
    return a
if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
