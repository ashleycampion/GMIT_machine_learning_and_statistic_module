# to load our model
from tensorflow.keras.models import load_model

# Neural networks.
import tensorflow.keras as kr

# using arrays
import numpy as np

class PowerPredictor:

    def __init__(self):
        self.model = load_model('model.h5')

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
