# Neural networks.
import tensorflow.keras as kr

# to split data into training and testing sets
from sklearn.model_selection import train_test_split

# for evaluating models
from sklearn import metrics

# Numerical arrays
import numpy as np

# Data frames.
import pandas as pd

class PowerPredictor:

    def __init__(self):
        df = pd.read_csv('https://raw.githubusercontent.com/ianmcloughlin/2020A-machstat-project/master/dataset/powerproduction.csv')
        columns = df.columns
        # Create a neural network with one neuron.
        model = kr.models.Sequential()
        model.add(kr.layers.Dense(50, input_shape=(1,), activation="sigmoid", kernel_initializer='ones', bias_initializer='zeros'))
        model.add(kr.layers.Dense(1, input_shape=(1,), activation="linear", kernel_initializer='ones', bias_initializer='zeros'))
        model.compile(kr.optimizers.Adam(lr=0.0095), loss='mean_squared_error')
        # Train the neural network.
        model.fit(df[columns[0]][:490], df[columns[1]][:490], epochs=500)
        self.model = model
    
    def predictPower(self, speed):
        try:
            speed = float(speed)
            if speed < 0:
                return "Speed cannot have a negative value."
            elif speed > 24.399:
                return "0"
            else:
                speed = np.array([speed])
                result = self.model.predict(speed)
                print(result[0][0])
                return str(result[0][0])
        except:
            return "Speed must be a number."

powerPredictor = PowerPredictor()