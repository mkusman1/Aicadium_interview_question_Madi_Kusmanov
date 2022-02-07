
# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Customer_data import Customer_id
import numpy as np
import pickle
import pandas as pd

# Create the app object
app = FastAPI()

# Import random forest classifier
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Pass JSON data and return the predicted revenue class 
@app.post('/')
# obtain customer data from user input
def predict_purchase(data:Customer_id):
    data = data.dict()
    BounceRates = data['BounceRates'] 
    ExitRates = data['ExitRates']
    PageValues = data['PageValues']
    SpecialDay = data['SpecialDay']
    Month = data['Month']
    OperatingSystems = data['OperatingSystems']
    Browser = data['Browser']
    Region = data['Region']
    TrafficType = data['TrafficType']
    VisitorType = data['VisitorType']
    Weekend = data['Weekend']
    ProductRelated_rate = data['ProductRelated_rate']
    Administrative_rate = data['Administrative_rate']
    Informational_rate = data['Informational_rate']

    # make a prediciton based on input data
    prediction = classifier.predict([[BounceRates, ExitRates, PageValues,
                                     SpecialDay, Month, OperatingSystems,
                                     Browser, Region, TrafficType,
                                     VisitorType, Weekend,
                                     ProductRelated_rate, Administrative_rate,
                                     Informational_rate]])
    if(prediction[0]>0.5):
        prediction="Revenue = 1: customer is predicted to make a purchase"
    else:
        prediction="Revenue = 1: customer is predicted to make a purchase"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload