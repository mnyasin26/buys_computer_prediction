from flask import Flask, render_template, request
import os
import jsonify
import requests
import pickle
import numpy as np
from sklearn import *
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('buys_computer_pred.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['age'])
        Income = int(request.form['income'])
        Student = int(request.form['student'])
        Credit_rating = int(request.form['credit_rating'])
        prediction=model.predict([[Age,Income,Student,Credit_rating]])
        output=prediction[0]
        print(output)
        if output == 0:
            return render_template('index.html',prediction_text="No")
        else:
            return render_template('index.html',prediction_text="Yes")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)