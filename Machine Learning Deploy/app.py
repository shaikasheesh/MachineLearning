import pickle
loaded_model = pickle.load(open('model.pkl, 'rb'))
from flask import Flask,jsonify,render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('web_index.html')

