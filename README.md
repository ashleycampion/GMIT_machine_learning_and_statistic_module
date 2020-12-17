# GMIT_machine_learning_and_statistic_module
Contains the (continuous) assessment tasks for the machine learning and statistics module.


## Technologies Used

Python 3.7.4 was the only programming language used.
The tasks are contained in a Jupyter Notebook, and explanation / introductions / context is given in that Notebook.

The project is spread across a Jupyter Notebook and the Project folder. The Notebook contains the code to create the machine learning model that can predict power based on speed, as well as explanations of the code. The folder contains a web app and a Dockerfile that can be used to run the web app in a docker container. More information on the web app and how to run it can be found in the readme of the project folder.

A number of Python packages were used for both the tasks and projects:

* Numpy
* Numpy.random
* Matplotlib.pyplot
* Sklearn
* Tensorflow
* Keras

## Project Prompt
In this project you must create a web service that uses machine learning to make predictions based on the data set powerproduction available on Moodle. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. You must then develop a web service that will respond with predicted power values based on speed values sent as HTTP requests. Your submission must be in the form of a git repository containing, at a minimum, the following items:

Jupyter notebook that trains a model using the data set. In the notebook you should explain your model and give an analysis of its accuracy.
Python script that runs a web service based on the model, as above.
Dockerfile to build and run the web service in a container.
Standard items in a git repository such as a README. To enhance your submission, you might consider developing and comparing more than one model. Rest assured, all the above concepts will be explored in lecture videos and other materials in the coming semester.




## Task Prompts


### Task 1 - October 5th, 2020
Write a Python function called sqrt2 that calculates and prints to the screen the square root of 2 to 100 decimal places. Your code should not depend on any module from the standard library or otherwise. You should research the task first and include references and a description of your algorithm.


### Task 2 November 2nd, 2020:
The Chi-squared test for independence is a statistical hypothesis test like a t-test. It is used to analyse whether two categorical variables are independent. The Wikipedia article gives the table below as an example [4], stating the Chi-squared value based on it is approximately 24.6. Use scipy.stats to verify this value and calculate the associated p value. You should include a short note with references justifying your analysis in a markdown cell.


### Task 3 November 16th, 2020
The standard deviation of an array of numbers x is calculated using numpy as np.sqrt(np.sum((x - np.mean(x))**2)/len(x)) . However, Microsoft Excel has two different versions of the standard deviation calculation, STDDEV.P and STDDEV.S . The STDDEV.P function performs the above calculation but in the STDDEV.S calculation the division is by len(x)-1 rather than len(x) . Research these Excel functions, writing a note in a Markdown cell about the difference between them. Then use numpy to perform a simulation demonstrating that the STDDEV.S calculation is a better estimate for the standard deviation of a population when performed on a sample. Note that part of this task is to figure out the terminology in the previous sentence.



### Task 4 November 30th, 2020
Use scikit-learn to apply k-means clustering to Fisher’s famous Iris data set. You will easily obtain a copy of the data set online. Explain in a Markdown cell how your code works and how accurate it might be, and then explain how your model could be used to make predictions of species of iris.




