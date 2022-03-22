import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import statistics
import csv

df=pd.read_csv('medium_data.csv')
data=df["temp"].to_list()
population_mean=statistics.mean(data)
population_std_deviation=statistics.stdev(data)
print("The population mean is ",population_mean)
print("The population's standard deviation is ",population_std_deviation)

#Function to get the mean of the given data samples
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
    #std_deviation=statistics.stdev(dataset)
    #print("The sample mean is ",mean)
    #print("The sample's standard deviation is ",std_deviation)

#Function to get the mean of 100 data points 1000 times and plot the graph
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

#Function to plot the mean on the graph
def show_fig(mean_list):
    mean=statistics.mean(mean_list)
    std_deviation=statistics.stdev(mean_list)
    print("The sample distribution mean is ",mean)
    print("The sample distribution's standard deviation is ",std_deviation)
    fig=ff.create_distplot([mean_list],["Temperature"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean"))
    fig.show()

setup()
