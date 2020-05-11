# essential libraries
import random
from datetime import timedelta  

# storing and anaysis
import numpy as np
import pandas as pd

# visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import calmap
import folium

# color pallette
cnf, dth, rec, act = '#393e46', '#ff2e63', '#21bf73', '#fe9801' 

# converter
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()   

# hide warnings
import warnings
warnings.filterwarnings('ignore')

# html embedding
from IPython.display import Javascript
from IPython.core.display import display
from IPython.core.display import HTML




def display_full_table(full_table):
    print(full_table.sample(6))

def  describe_confirmed_deaths_recovered(full_table): 
    full_table = pd.read_csv('2019_nC0v_20200121_20200126_cleaned.csv', parse_dates=['Date']) # to get into date format  
    #sample_table["month"].astype('datetime64[M]')
    #dataframe info
    full_table.info()
    print(full_table.describe()[full_table.columns[5:8]]) # describe confirmed deats and recovered 

def extract_year_maonth_day(full_table): 
    year_wanted=2020
    
    
    #sample_table=full_table.sample(3)
    
    sample_table=full_table
    
    #print(sample_table)
    
    #sample_table["month"]=sample_table["Date"].dt.to_period('M') # gives both month n year
    
    print(pd.DatetimeIndex(sample_table['Date']).year)
    
    # extract the year and month 
    sample_table["year"]=pd.DatetimeIndex(sample_table['Date']).year
    sample_table["month"]=pd.DatetimeIndex(sample_table['Date']).month 
    sample_table["day"]=pd.DatetimeIndex(sample_table['Date']).day
    
    # print(sample_table["year"].equals(year_wanted))
    
    
    sample_table.info()
    print(" \n\n")
    print(sample_table.loc[sample_table['year'] == year_wanted])
    sample_table.info()
    return sample_table


def daywise_plot_confirmed_cases(sample_table):
    #Perform Grouping by days
    grp=sample_table.groupby('day')
    
    print(grp["Confirmed"].sum())
    
    
    x = [21,22,23,24,25,26]
    labels = ["21",'22', '23', "24","25","26"]
    #plt.plot(x,y, 'r')
    plt.xticks(x, labels, rotation='vertical')
    
    plt.bar(sample_table["day"], sample_table["Confirmed"])
    #plt.text(8,3,'This text ends at point (8,3)',horizontalalignment='right')

    #plt.xticks(np.arange(1,4,1))
    
    #plt.set_xticklabels(["Jan","Feb","Mar"])
   
    
    

def daywise_plot_Death_cases(sample_table):
    grp=sample_table.groupby('day')

    x = [21,22,23,24,25,26]
    labels = ["21",'22', '23', "24","25","26"]
    #plt.plot(x,y, 'r')
    print(grp["Deaths"].sum())

    plt.xticks(x, labels, rotation='vertical')
    plt.bar(sample_table["day"], sample_table["Deaths"])
    
def daywise_plot_Recovered_cases(sample_table):
    grp=sample_table.groupby('day')

    x = [21,22,23,24,25,26]
    labels = ["21",'22', '23', "24","25","26"]
    print(grp["Recovered"].sum())

    #plt.plot(x,y, 'r')
    plt.xticks(x, labels, rotation='vertical')
    
    plt.bar(sample_table["day"], sample_table["Recovered"])
    

def analyze_active_cases_fill_missing_values(full_table):
    cases = ['Confirmed', 'Deaths', 'Recovered', 'Active']
    
    # Active Case = confirmed - deaths - recovered
    full_table['Active'] = full_table['Confirmed'] - full_table['Deaths'] - full_table['Recovered']
    
    # replacing Mainland china with just China
    full_table['Country'] = full_table['Country'].replace('Mainland China', 'China')
    
    # filling missing values 
    full_table[['Province/State']] = full_table[['Province/State']].fillna('-')
    full_table[cases] = full_table[cases].fillna(0)
    
    # fixing datatypes
    #print(full_table.info())
    #full_table['Recovered'] = full_table['Recovered'].astype(int)
    #print(full_table.info())
    
    print(full_table.sample(20))
    
def latest_data_as_per_Date(full_table):
    country='China'

    # cases in the ships
    ship = full_table[full_table['Province/State'].str.contains('Grand Princess')|full_table['Country'].str.contains('Diamond Princess')]
    
    # china and the row
    country_table = full_table[full_table['Country']==country]
    row = full_table[full_table['Country']!=country]
    
    # latest
    #print(full_table.head())
    full_latest = full_table[full_table['Date'] == max(full_table['Date'])].reset_index()   # last day in dataset 
    #print(full_latest.head())
    country_table_latest = full_latest[full_latest['Country']==country]
    #print(full_latest.head())
    row_latest = full_latest[full_latest['Country']!=country]
    
    # latest condensed
    print(full_latest)
    full_latest_grouped = full_latest.groupby('Country')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
    print(full_latest_grouped)
    #country_latest_grouped = country_table_latest.groupby('Province/State')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
    #row_latest_grouped = row_latest.groupby('Country')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()

 
    
