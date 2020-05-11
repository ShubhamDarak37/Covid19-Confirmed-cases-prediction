import numpy as np 
import pandas as pd 
from sklearn import metrics

import os
# import the necessary Core  libraries
from sklearn.metrics import accuracy_score
# Import Visualisation libraries
import matplotlib.pyplot as plt
import plotly
import seaborn as sns
sns.set()
import pycountry
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot 
import plotly.graph_objs as go
import plotly.offline as py

from pywaffle import Waffle

py.init_notebook_mode(connected=True)
import folium 
from folium import plugins
plt.style.use("fivethirtyeight")# for pretty graphs

# Increase the default plot size and set the color scheme
plt.rcParams['figure.figsize'] = 8, 5
#plt.rcParams['image.cmap'] = 'viridis'
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

#Day by day data All countries 
#--------------------------------
# confirmed cases



def display_time_series_dataset(df_confirmed,df_recovered,df_deaths):
    # Check data 
    print(df_confirmed.head())
    print(df_recovered.head())
    print(df_deaths.head())



def country_wise_processing_of_dataset(df_confirmed):
    # Drop columns not needed for this Analysis  
    df_confirmed.drop(['Province/State','Lat','Long'],axis=1,inplace=True)
    # Rename to shorter column names 
    df_confirmed.rename(columns= {'Country/Region':'Region'},inplace= True)
    print(df_confirmed.columns)    
    # Create Listof countries to Analyse
    plot_countries = ['India','Iran','Italy','Korea, South','Spain']
    
    # subset by countries to plot 
    df_conf_plot= df_confirmed[df_confirmed.Region.isin(plot_countries)]
    
    # Transpose df
    df_conf_plot_T = df_conf_plot.T
    
    # Check Actual Col Names 
    print(df_conf_plot_T.head())
    return df_conf_plot_T

def Set_Date_Index(df_conf_plot_T):
    # Rename Columns 
    df_conf_plot_T.rename(columns= {131:'India',137:'Italy',133:'Iran',143:'Korea, South',201:'Spain'},inplace= True)
    
    # drop first row 
    df_conf_plot_T.drop(df_conf_plot_T.index[0],inplace=True)
    
    # name Index 
    df_conf_plot_T.index.name='DATE'
    
    # Check 
    print(df_conf_plot_T.head())
    return df_conf_plot_T



def Assign_Date_Index_For_each_Country(df_conf_plot_T):
    
    df_confirmed_All = df_conf_plot_T.copy()
    df_confirmed_All.plot();
    
    #output graph is shown in pdf
    
    # Extract date DF for All countries 
    df_confirmed_1 = df_confirmed_All.copy()
    # Create date column 
    df_confirmed_All['DATE'] = df_confirmed_All.index
    df_confirmed_All.head()

    

    
    # Create date DF 
    DT_df = df_confirmed_All[['DATE']]
    DT_df  = DT_df.set_index('DATE')
    DT_df.head()
    
    # Extract Series for All countries
    s_India   = df_confirmed_All['India']
    s_Iran    = df_confirmed_All['Iran']
    s_Italy   = df_confirmed_All['Italy']
    s_Korea   = df_confirmed_All['Korea, South']
    s_Spain   = df_confirmed_All['Spain']
    
    
    print(s_India.tail())
    len(s_India)
   
    
    
    
    # Extract date DF   for All countries
    #--------------------------------------
    n = 50  # cutoff case count for fitting model 
    #------------------
    India_DT_df     = DT_df[s_India >n]
    Iran_DT_df       = DT_df[s_Iran >n]
    Italy_DT_df      = DT_df[s_Italy >n]
    Korea_DT_df      = DT_df[s_Korea >n]
    Spain_DT_df      = DT_df[s_Spain >n]
    
    # Create a Date column 
    India_DT_df['Date']      = India_DT_df.index
    Iran_DT_df['Date']       = Iran_DT_df.index
    Italy_DT_df['Date']      = Italy_DT_df.index
    Korea_DT_df['Date']      = Korea_DT_df.index
    Spain_DT_df['Date']      = Spain_DT_df.index
    
    # Get Series of All date DFs
    India_DT_s  = India_DT_df['Date']      
    Iran_DT_s   = Iran_DT_df['Date']     
    Italy_DT_s  = Italy_DT_df['Date']      
    Korea_DT_s  = Korea_DT_df['Date']      
    Spain_DT_s  = Spain_DT_df['Date']
    
    # subset each series for numbers > 100
    n = 50
    #-------------------------------------------------
    # India
    s_India_GE100 = s_India[s_India > n] 
    s_India_GE100 = pd.to_numeric(s_India_GE100, errors='coerce').fillna(0, downcast='infer')
    #----------------------------------------------
    # Iran
    s_Iran_GE100 = s_Iran[s_Iran > n] 
    s_Iran_GE100 = pd.to_numeric(s_Iran_GE100, errors='coerce').fillna(0, downcast='infer')
    #-------------------------------------------------
    # Italy
    s_Italy_GE100 = s_Italy[s_Italy > n] 
    s_Italy_GE100 = pd.to_numeric(s_Italy_GE100, errors='coerce').fillna(0, downcast='infer')
    #-------------------------------------------------
    # Korea
    s_Korea_GE100 = s_Korea[s_Korea > n] 
    s_Korea_GE100 = pd.to_numeric(s_Korea_GE100, errors='coerce').fillna(0, downcast='infer')
    #--------------------------------------------------
    # Spain
    s_Spain_GE100 = s_Spain[s_Spain > n] 
    s_Spain_GE100 = pd.to_numeric(s_Spain_GE100, errors='coerce').fillna(0, downcast='infer')
    
    print(s_India_GE100.head())
    len(s_India_GE100)
    return s_India_GE100,India_DT_s


# Model India 
    
def India_model(s_India_GE100,India_DT_s):
    import numpy as np
    #--------------------------------------
    # Y data 
    Y = s_India_GE100
    # X data 
    X = np.arange(1,len(Y)+1)
    Xdate = India_DT_s
    # Fit 3rd Degree polynomial capture coefficients 
    Z = np.polyfit(X, Y, 3)
    # Generate polynomial function with these coefficients 
    P = np.poly1d(Z)
    # Generate X data for forecast 
    XP = np.arange(1,len(Y)+8)
    # Generate forecast 
    YP = P(XP)
    # Fit Curve
    Yfit = P(X)
    
    import datetime
    start = Xdate[0]
    #start
    end_dt = datetime.datetime.strptime(Xdate[len(Xdate)-1], "%m/%d/%y")
    
    end_date = datetime.datetime.strptime(str(end_dt),'%Y-%m-%d %H:%M:%S').date()
    
    end_forecast_dt= end_dt + datetime.timedelta(days=7)
    
    end_forecast =  datetime.datetime.strptime(str(end_forecast_dt),'%Y-%m-%d %H:%M:%S').date()
    end_forecast
    #
    mydates = pd.date_range(start, end_forecast).to_list()
    mydates_df = pd.DataFrame(mydates,columns =['Date']) 
    mydates_df  = mydates_df.set_index('Date')
    mydates_df['Date'] = mydates_df.index
    X_FC = mydates_df['Date']

    fig = plt.figure(figsize=(20,10))
    ax = plt.subplot(111)
    ax.plot(X, Y, '--',label='Actual Confirmed')
    ax.plot(XP, YP, 'o',label='Predicted Fit using 3rd degree polynomial')
    plt.title('COVID RISE IN India Current Vs Predictions till 10th May 2020')
    ax.legend()
    ax.set_ylim(0,150000)
    ax.grid(True)
    plt.show()

    #output
    #graph is present in pdf
    
    # Define new figure 
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(Xdate,Y,'b-')
    ax.tick_params(direction='out', length=10, width=10, colors='r')
    ax.set_xlabel('Date',fontsize=25)
    ax.set_ylabel('Confirmed Cases',fontsize=25)
    ax.set_title('COVID 19 Spread in India as of 10th May 2020',fontsize=25)
    ax.set_ylim(0,150000)
    fig.autofmt_xdate()
    
    ax.grid(True)
    fig.tight_layout()
    
    plt.show()
    #output
    #graph is present in pdf
    
    # Define new figure 
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(X_FC,YP,'--')
    ax.tick_params(direction='out', length=10, width=10, colors='r')
    ax.set_xlabel('Date',fontsize=25)
    ax.set_ylabel('Predicted Cases',fontsize=25)
    ax.set_ylim(0,15000)
    ax.set_title('COVID 19 PREDICTION for India till 17th May 2020',fontsize=25)
    fig.autofmt_xdate()
    
    ax.grid(True)
    fig.tight_layout()
    
    plt.show()
    #output
    #graph is present in pdf
    
    # Create a dataframe from Predicted data 
    dict1 = {'Date':X_FC,'Predicted_Cases':YP}
    pred_df = pd.DataFrame.from_dict(dict1)
    pred_df = pred_df[['Predicted_Cases']]
    pred_df.Predicted_Cases = pred_df.Predicted_Cases.astype(int)
    print(pred_df.tail(n=8))
"""
            Predicted_Cases
Date                       
2020-05-10            65496
2020-05-11            69034
2020-05-12            72699
2020-05-13            76494
2020-05-14            80420
2020-05-15            84480
2020-05-16            88675
2020-05-17            93009

 """




































