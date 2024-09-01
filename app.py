from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Lista de letras
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pick_letter')
def pick_letter():
    if letters:
        letter = random.choice(letters)
        letters.remove(letter)
    else:
        letter = "No more letters!"
    return jsonify({'letter': letter})

@app.route('/reset_list')
def reset_list():
    global letters
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return jsonify({'status': 'List reset'})

if __name__ == '__main__':
    app.run(debug=True)