# this file creates the model and saves it to a file
# this file is not run by the server

# Neural networks.
import tensorflow.keras as kr

# to split data into training and testing sets
from sklearn.model_selection import train_test_split

# Numerical arrays
import numpy as np

# Data frames.
import pandas as pd

# saving the model to a file
# import pickle

class PowerPredictor:

    def __init__(self):
        df = pd.read_csv('https://raw.githubusercontent.com/ianmcloughlin/2020A-machstat-project/master/dataset/powerproduction.csv')
        newDF = df.loc[(df['speed']<16) | (df['power']!=0)]
        columns = newDF.columns
        # Create a neural network with one neuron.
        model = kr.models.Sequential()
        model.add(kr.layers.Dense(50, input_shape=(1,), activation="sigmoid", kernel_initializer='ones', bias_initializer='zeros'))
        model.add(kr.layers.Dense(1, input_shape=(1,), activation="linear", kernel_initializer='ones', bias_initializer='zeros'))
        model.compile(kr.optimizers.Adam(lr=0.0095), loss='mean_squared_error')
        # Train the neural network.
        model.fit(newDF[columns[0]][:490], newDF[columns[1]][:490], epochs=350)
        self.model = model
    
powerPredictor = PowerPredictor()

model = powerPredictor.model


## Python's pickle and joblib modules were not used to save the
## model as an error resulted.

## https://dataaspirant.com/save-scikit-learn-models-with-python-pickle/
## Dump the model with Pickle
#modelFilename = 'model.pkl'
## Open the file to save as pkl file
#modelPkl = open(modelFilename, 'wb')
#pickle.dump(model, modelPkl)
## Close the pickle instances
#modelPkl.close()

#from sklearn.externals import joblib
## Save the model as a pickle in a file 
#joblib.dump(model, 'model.pkl') 

# keras' model.save method can be used
model.save('model.h5')