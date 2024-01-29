import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

##importing ridge regression and StandardScaler Pickle
ridge_model = pickle.load(open("Models/ridge.pkl","rb"))
Scaler_model = pickle.load(open("Models/scaler.pkl","rb"))

##Route for Home page
@app.route("/")
def index():
    return render_template("index.html") ## It sees where is the template folder

##prediction
@app.route("/Predict Data",methods=["GET","POST"])
def predict_datapoint():
    if request.method=="POST": ## if we give values then it will move in this part but if we dont give values then it will go to the else part
        Temperature=float(request.form.get("Temperature"))
        RH=float(request.form.get("RH"))
        Ws=float(request.form.get("Ws"))
        Rain=float(request.form.get("Rain"))
        FFMC=float(request.form.get("FFMC"))
        DMC=float(request.form.get("DMC"))
        ISI=float(request.form.get("ISI"))
        Classes=float(request.form.get("Classes"))
        Region=float(request.form.get("Region"))

        new_data_scaled = Scaler_model.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_data_scaled)

        return render_template("home.html",result=result[0])
    else:
        return render_template("home.html")



if __name__=="__main__":
    app.run(host="0.0.0.0") ## It will map with the local address