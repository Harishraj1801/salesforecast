#imports for fileupload
#imports for fileupload
from flask import Flask, jsonify, request, redirect, json, url_for
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
#imports for ml purpose
import json
import pandas as pd
import pymongo

from datetime import datetime
import matplotlib.pyplot as plt
#plt.switch_backend('agg')

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["newdb"]
collection = db["newc"]


#rcparams for trend, seasonality, noise graph
import statsmodels.api as sm
from statsmodels.tsa.statespace.sarimax import SARIMAX

import warnings
warnings.filterwarnings("ignore")


#created a flask application
app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'])

global stepCount
#file upload - getting post request from angular-flask
app.config['UPLOAD_FOLDER'] = 'C:/Users/harish raj/Downloads/Backend/Backend'
@app.route('/upload',methods = ['GET', 'POST'])
def upload_File():

    if request.method == 'POST':
        #check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        global fname
        fname = secure_filename(file.filename) 
          
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
        print(fname) 
        return redirect(request.url)

    return 'File Uploaded'


tag ='=====================>'
@app.route('/forecast', methods = ['POST','GET'])
def forecast():
    info = request.data
    #print(tag,info)
    dict_str = str(info, 'UTF-8')
    #print(tag,dict_str)
    data = json.loads(dict_str)
    steps = data['selectedItem']
    # print(tag,dict)
    # print(dict.keys())

    # steps = dict.get('period')
    # print(steps)
    global stepCount
    stepCount =int(steps)
    print(stepCount)
    
    return 'success!'
#def matplotlib_pyplot_savefig():
    #plt.savefig('plot.png')



#create a parser to modify the stepCount format
def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')

#show the final graph required
length = 14
breadth = 7
@app.route('/plot',methods = ['GET', 'POST'])
def plot():
    # Load the data from CSV
    plt.clf()
    data = pd.read_csv(fname, index_col='Date', parse_dates=['Date'])
    filename = "Prediction.xlsx"

# construct the file path using the current working directory
    file_path = os.path.join(os.getcwd(), filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"The file '{filename}' has been deleted.")
    else:
        print(f"The file '{filename}' does not exist.")
    # os.remove(file_path)

    # Select the endogenous variable
    endog = data['Sales']

    # Define the SARIMAX model
    model = SARIMAX(endog, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))

    # Fit the model
    results = model.fit()
    # first_column = data.iloc[:, 0]
    # print(first_column)
    # data.columns = ['Date']
    # Generate a forecast for the specified number of steps
    forecast = results.forecast(steps=stepCount)
    fore=forecast.to_frame()
    fore.reset_index(inplace=True)
    fore.rename(columns={'index': 'date'}, inplace=True)

# Convert date column to datetime format
    fore['date'] = pd.to_datetime(fore['date'], unit='s')
    fore['date'] = fore['date'].dt.strftime('%d-%m-%Y')
    # fore.columns = ['Date']
    fore.columns = ['Date','Prediction']
    print(type(forecast))
    print("Forecast")
    print(fore)   
    # forecast_df = forecast.tolist()
    # print(forecast_df)
    
    # Save the forecast dataframe to Excel
    
    fore.to_excel('Prediction.xlsx')

# Save the DataFrame to Excel
    
    plt.rcParams['figure.figsize'] = [14, 7]
    plt.plot(endog.index, endog, label='Actual Sales')
    plt.plot(forecast.index, forecast, label='Forecast')
    if(stepCount!=60):
        for i, j in zip(endog.index, endog):
            plt.text(i, j, str(j))
    # for k, l in zip(forecast.index, forecast):
    #     plt.text(k, l, str(k))
    
    plt.legend()
    plt.savefig('my_plot.png', bbox_inches='tight')
   # data.to_excel('Prediction.xlsx')
    plt.show()
    forecast = forecast.tolist()
    
    

    # Return the forecast as a JSON response
    return redirect("http://localhost:4200/login")



# A simple function to calculate the square of a number
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
    return jsonify({'data': num**2})
@app.route("/verify", methods=['GET', 'POST'])
def verify_user():
    # Get the email and password from the request body
    email = request.json.get("email")
    password = request.json.get("password")
    string=str(email)
    print(string)
    string2=str(password)
    print(string2)
# Define the query to verify data
    query = {"username": string,"password": string2}

# Verify if the data exists in the collection
    result = collection.find(query)
    print(result)
    for x in collection.find({},{ "username" }):
        print(x)

    if len(list(result)) > 0:
        print("Data exists in the collection.")
        exists = True  # Replace with database query result
        return jsonify({'exists': exists})
        
    else:
        print("Data does not exist in the collection.")
        exists = False  # Replace with database query result
        return jsonify({'exists': exists})
    # Look for the user in the list of users
    # for user in users:
    #     if user["email"] == email and user["password"] == password:
    #         # If the email and password match, return a token
    #         return jsonify({"token": user["id"]})

    # # If no matching user is found, return a 401 Unauthorized status code
    # return jsonify({"error": "Incorrect email or password."}), 401

# driver function
if __name__ == '__main__':
    app.run(debug = True)