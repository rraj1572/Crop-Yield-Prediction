import pickle
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash

model = pickle.load(open('model.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')
def member():
    return render_template('Home.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['Area']
    data2 = request.form['Production']
    arr = np.array([[data1, data2]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)



if __name__ == '__main__':
    app.run(debug=True)

 

