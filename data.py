import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("dataset.csv") #Read data from CSV datafile
plt.title("Heart Rate Signal") #The title of our plot
plt.plot(dataset.hart) #Draw the plot object
plt.show() #Display the plot