from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd


application = Flask(__name__)
app=application

model = pickle.load(open("Model\modelForPrediction.pkl", "rb"))

## Route for homepage

@app.route('/')
def index():
    return render_template('home.html')

## Route for Single data point prediction
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        Hour=int(request.form.get("Hour"))
        Scores = float(request.form.get('Scores'))
        Extracurricular = float(request.form.get('Extracurricular'))
        Sleep = float(request.form.get('Sleep'))
        SampleQuestionPapers = float(request.form.get('SampleQuestionPapers'))

        new_data = [[Hour,Scores,Extracurricular,Sleep,SampleQuestionPapers]]
        result =model.predict(new_data)
        
        Result = round(result[0])

        return render_template('home.html',result = Result)

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")
