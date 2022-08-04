import pickle
from flask import Flask, request, jsonify, render_template, url_for
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from logger import log
from mongo import MongodbConnection
from utils import RandomBatchModeling
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

# Import Scaling, Classification and Regression Pickle Files
scaler = pickle.load(open("Features_Scaled.pkl", "rb"))
reg_model = pickle.load(open("Regression.pkl", "rb"))
class_model = pickle.load(open("Classification.pkl", "rb"))
log.info("Scaling and Models are loaded from Pickle")


# Data retrieved from DB using mongodbconnection Module
dbconn = MongodbConnection(username='root', password='root')
list_cursor = dbconn.getData(dbName='Algerian_Forest-Fires', collectionName='Forest-Fires')
log.info("Database connected successfully")
    # Removing "_id" from list_cursor
list_dict = []
for i in list_cursor:
    del i['_id']
    list_dict.append(i)
log.info("Loaded datas after removing '_id' key" )


# Route for Home Page
@app.route('/')
def index():
    log.info('Home page loaded successfully')
    return render_template('index.html')

# Route for Single Prediction Page
@app.route('/single_prediction')
def single_prediction():
    log.info('Single_prediction page loaded successfully')
    return render_template('single_prediction.html')

# Route for Batch Prediction Page
@app.route('/batch_prediction')
def batch_prediction():
    log.info('Batch_prediction page loaded successfully')
    return render_template('batch_prediction.html')


# Route for Regression Model
@app.route('/single_reg_predict', methods=['POST'])
def single_reg_predict():
    try:
        data = [float(x) for x in request.form.values()]
        data = [np.array(data)]
        data_scaled = scaler.transform(data)
        output = reg_model.predict(data_scaled)[0]
        log.info('Single_Prediction done for Regression model')
        if output > 12:
            return render_template('single_prediction.html', reg_prediction="Fire Weather Index is {:.4f} ---- Forest is in Danger !".format(output))
        else:
            return render_template('single_prediction.html', reg_prediction="Fire Weather Index is {:.4f} ---- Forest is Safe !".format(output))
    except Exception as e:
        log.error('Input error, check input', e)
        return render_template('single_prediction.html', reg_prediction="Check the Input again!!!")


# # Route for Classification Model
@app.route('/single_class_predict', methods=['POST'])
def single_class_predict():
    try:
        data = [float(x) for x in request.form.values()]
        data = [np.array(data)]
        data_scaled = scaler.transform(data)
        output = class_model.predict(data_scaled)[0]
        log.info('Single_Prediction done for Classification model')
        if output == 0:
            text = 'Forest is Safe!'
        else:
            text = 'Forest is in Danger!'
        return render_template('single_prediction.html', class_prediction=text)
    except Exception as e:
        log.error('Input error, check input', e)
        return render_template('single_prediction.html', class_prediction="Check the Input again!!!")


# Route for BATCH Regression Model
@app.route('/batch_reg_predict', methods=['POST'])
def batch_reg_predict():
    try:
        # Getting data from Form actions
        input_value = [int(x) for x in request.form.values()][0]
        # Retrieves the dataframe with complete prediction details
        frame = RandomBatchModeling.outframe(list_dict, input_value, scaler, reg_model)
        log.info("Regression dataframe created with random batch predicted output")
        with open("templates/batch_reg.html", "wb") as f:
            tags = frame.encode('utf-8')
            f.write(tags)
        return render_template('batch_reg.html')
    except Exception as e:
        log.error('Input error, check input', e)



# Route for BATCH Classification Model
@app.route('/batch_class_predict', methods=['POST'])
def batch_class_predict(): 
    try:
        # Getting data from Form actions
        input_value = [int(x) for x in request.form.values()][0]
        # Retrieves the dataframe with complete prediction details
        frame = RandomBatchModeling.outframe(list_dict, input_value, scaler, class_model)
        log.info("Classification dataframe created with random batch predicted output")
        with open("templates/batch_class.html", "wb") as f:
            tags = frame.encode('utf-8')
            f.write(tags)
        return render_template('batch_class.html')
    except Exception as e:
        log.error('Input error, check input', e)



# Run APP in Debug mode
if __name__ == "__main__":
    app.run(debug=True)
