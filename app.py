# Importing necessary libraries
import numpy as np
import pandas as pd 
from pandas import Series, DataFrame
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
import pickle

# Reading the data
iris = pd.read_csv("Iris.csv")
print(iris.head())
iris.drop("Id", axis=1, inplace = True)
y = iris['Species']
iris.drop(columns='Species',inplace=True)
X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]

# Training the model
x_train,x_test,y_train,y_test = train_test_split(X,y, test_size=0.3)
model = LogisticRegression()
model.fit(x_train,y_train)

pickle.dump(model,open('model.pkl','wb'))

# importing necessary libraries and functions
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb')) # loading the trained model

@app.route('/') # Homepage
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    # retrieving values from form
    init_features = [float(x) for x in request.form.values()]
    final_features = [np.array(init_features)]

    prediction = model.predict(final_features) # making prediction


    return render_template('index.html', prediction_text='Predicted Class: {}'.format(prediction)) # rendering the predicted result

if __name__ == "__main__":
    app.run(debug=True)
