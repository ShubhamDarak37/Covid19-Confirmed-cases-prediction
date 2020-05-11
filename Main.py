import numpy as np 
import pandas as pd 
import os

from preprocessing import *
from analysis import *
from model import *
#analysis of global dataset
full_table = pd.read_csv('2019_nC0v_20200121_20200126_cleaned.csv')
display_full_table(full_table)

"""
display_full_table(full_table)
     Unnamed: 0  Province/State         Country  ... Suspected  Recovered  Deaths
241         241        Shanghai  Mainland China  ...        72          1       0
52           52        Shanghai  Mainland China  ...        10          0       0
346         346  Inner Mongolia  Mainland China  ...         0          0       0
184         184               0           Japan  ...         0          0       0
91           91          Shanxi  Mainland China  ...         0          0       0
267         267      Washington   United States  ...         0          0       0

[6 rows x 8 columns]

"""

describe_confirmed_deaths_recovered(full_table)

"""
describe_confirmed_deaths_recovered(full_table)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 368 entries, 0 to 367
Data columns (total 8 columns):
Unnamed: 0        368 non-null int64
Province/State    368 non-null object
Country           368 non-null object
Date              368 non-null datetime64[ns]
Confirmed         368 non-null int64
Suspected         368 non-null int64
Recovered         368 non-null int64
Deaths            368 non-null int64
dtypes: datetime64[ns](1), int64(5), object(2)
memory usage: 23.1+ KB

        Suspected   Recovered      Deaths
count  368.000000  368.000000  368.000000
mean     5.407609    0.755435    0.720109
std     25.367858    4.707808    5.166485
min      0.000000    0.000000    0.000000
25%      0.000000    0.000000    0.000000
50%      0.000000    0.000000    0.000000
75%      0.000000    0.000000    0.000000
max    244.000000   42.000000   52.000000
"""

sample_table = extract_year_maonth_day(full_table)

"""
sampl_table = extract_year_maonth_day(full_table)
Int64Index([2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020,
            ...
            2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020],
           dtype='int64', name='Date', length=368)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 368 entries, 0 to 367
Data columns (total 11 columns):
Unnamed: 0        368 non-null int64
Province/State    368 non-null object
Country           368 non-null object
Date              368 non-null object
Confirmed         368 non-null int64
Suspected         368 non-null int64
Recovered         368 non-null int64
Deaths            368 non-null int64
year              368 non-null int64
month             368 non-null int64
day               368 non-null int64
dtypes: int64(8), object(3)
memory usage: 31.8+ KB
 


     Unnamed: 0 Province/State         Country  ...  year  month  day
0             0       Shanghai  Mainland China  ...  2020      1   21
1             1         Yunnan  Mainland China  ...  2020      1   21
2             2        Beijing  Mainland China  ...  2020      1   21
3             3         Taiwan          Taiwan  ...  2020      1   21
4             4          Jilin  Mainland China  ...  2020      1   21
..          ...            ...             ...  ...   ...    ...  ...
363         363              0          France  ...  2020      1   26
364         364              0       Australia  ...  2020      1   26
365         365              0           Nepal  ...  2020      1   26
366         366              0        Malaysia  ...  2020      1   26
367         367        Ontario          Canada  ...  2020      1   26

[368 rows x 11 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 368 entries, 0 to 367
Data columns (total 11 columns):
Unnamed: 0        368 non-null int64
Province/State    368 non-null object
Country           368 non-null object
Date              368 non-null object
Confirmed         368 non-null int64
Suspected         368 non-null int64
Recovered         368 non-null int64
Deaths            368 non-null int64
year              368 non-null int64
month             368 non-null int64
day               368 non-null int64
dtypes: int64(8), object(3)
memory usage: 31.8+ KB


"""

daywise_plot_confirmed_cases(sample_table)
"""
daywise_plot_confirmed_cases(sample_table)
day
21     332
22     555
23     653
24    1822
25    4811
26    2116
Name: Confirmed, dtype: int64
"""

daywise_plot_Death_cases(sample_table)

"""
daywise_plot_Death_cases(sample_table)
day
21      0
22      0
23     18
24     52
25    139
26     56
Name: Deaths, dtype: int64
"""
daywise_plot_Recovered_cases(sample_table)
"""
daywise_plot_Recovered_cases(sample_table)
day
21      0
22      0
23     30
24     70
25    126
26     52
Name: Recovered, dtype: int64
"""
analyze_active_cases_fill_missing_values(full_table)
"""
analyze_active_cases_fill_missing_values(full_table)
     Unnamed: 0  Province/State    Country  ... month  day  Active
261         261           Gansu      China  ...     1   25       4
9             9        Shandong      China  ...     1   21       1
314         314               0   Thailand  ...     1   25       7
303         303         Guizhou      China  ...     1   25       5
141         141         Ningxia      China  ...     1   24       1
176         176           Hebei      China  ...     1   24       1
12           12         Jiangxi      China  ...     1   21       2
157         157         Jiangxi      China  ...     1   24      18
140         140           Hebei      China  ...     1   24       1
336         336         Jiangsu      China  ...     1   26      32
243         243         Sichuan      China  ...     1   25      28
180         180  Inner Mongolia      China  ...     1   24       1
265         265           Macau      Macau  ...     1   25       2
272         272               0  Singapore  ...     1   25       3
156         156        Shanghai      China  ...     1   24      19
13           13           Henan      China  ...     1   21       1
128         128         Shaanxi      China  ...     1   24       3
178         178        Xinjiang      China  ...     1   24       2
238         238           Hunan      China  ...     1   25      43
350         350         Ningxia      China  ...     1   26       4

[20 rows x 12 columns]
"""
latest_data_as_per_Date(full_table)
"""

latest_data_as_per_Date(full_table)
    index  Unnamed: 0  Province/State        Country  ...  year  month  day  Active
0     322         322           Hubei          China  ...  2020      1   26     964
1     323         323       Guangdong          China  ...  2020      1   26     109
2     324         324        Zhejiang          China  ...  2020      1   26     103
3     325         325           Henan          China  ...  2020      1   26      82
4     326         326       Chongqing          China  ...  2020      1   26      75
5     327         327           Hunan          China  ...  2020      1   26      69
6     328         328         Beijing          China  ...  2020      1   26      66
7     329         329           Anhui          China  ...  2020      1   26      60
8     330         330        Shandong          China  ...  2020      1   26      46
9     331         331         Sichuan          China  ...  2020      1   26      44
10    332         332        Shanghai          China  ...  2020      1   26      38
11    333         333         Guangxi          China  ...  2020      1   26      36
12    334         334         Jiangxi          China  ...  2020      1   26      36
13    335         335          Fujian          China  ...  2020      1   26      35
14    336         336         Jiangsu          China  ...  2020      1   26      32
15    337         337          Hainan          China  ...  2020      1   26      22
16    338         338         Shaanxi          China  ...  2020      1   26      22
17    339         339        Liaoning          China  ...  2020      1   26      21
18    340         340          Yunnan          China  ...  2020      1   26      16
19    341         341    Heilongjiang          China  ...  2020      1   26      14
20    342         342         Tianjin          China  ...  2020      1   26      14
21    343         343           Hebei          China  ...  2020      1   26      12
22    344         344          Shanxi          China  ...  2020      1   26       9
23    345         345       Hong Kong      Hong Kong  ...  2020      1   26       8
24    346         346  Inner Mongolia          China  ...  2020      1   26       7
25    347         347           Gansu          China  ...  2020      1   26       7
26    348         348         Guizhou          China  ...  2020      1   26       5
27    349         349           Macau          Macau  ...  2020      1   26       5
28    350         350         Ningxia          China  ...  2020      1   26       4
29    351         351           Jilin          China  ...  2020      1   26       4
30    352         352          Taiwan         Taiwan  ...  2020      1   26       4
31    353         353        Xinjiang          China  ...  2020      1   26       4
32    354         354         Qinghai          China  ...  2020      1   26       1
33    355         355      Washington  United States  ...  2020      1   26       1
34    356         356        Illinois  United States  ...  2020      1   26       1
35    357         357      California  United States  ...  2020      1   26       1
36    358         358               0          Japan  ...  2020      1   26       3
37    359         359               0       Thailand  ...  2020      1   26       6
38    360         360               0    South Korea  ...  2020      1   26       3
39    361         361               0      Singapore  ...  2020      1   26       4
40    362         362               0        Vietnam  ...  2020      1   26       2
41    363         363               0         France  ...  2020      1   26       3
42    364         364               0      Australia  ...  2020      1   26       4
43    365         365               0          Nepal  ...  2020      1   26       1
44    366         366               0       Malaysia  ...  2020      1   26       4
45    367         367         Ontario         Canada  ...  2020      1   26       1

[46 rows x 13 columns]
          Country  Confirmed  Deaths  Recovered  Active
0       Australia          4       0          0       4
1          Canada          1       0          0       1
2           China       2062      56         49    1957
3          France          3       0          0       3
4       Hong Kong          8       0          0       8
5           Japan          4       0          1       3
6           Macau          5       0          0       5
7        Malaysia          4       0          0       4
8           Nepal          1       0          0       1
9       Singapore          4       0          0       4
10    South Korea          3       0          0       3
11         Taiwan          4       0          0       4
12       Thailand          8       0          2       6
13  United States          3       0          0       3
14        Vietnam          2       0          0       2

"""


#analysis of timeseries dataset

df_confirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')
df_conf1 = df_confirmed.copy()
# recovered 
df_recovered = pd.read_csv('time_series_covid19_recovered_global.csv')
df_recov1 = df_recovered.copy()
# deaths 
df_deaths    = pd.read_csv('time_series_covid19_deaths_global.csv')
df_deaths1 = df_deaths.copy()

display_time_series_dataset(df_confirmed,df_recovered,df_deaths)

"""
display_time_series_dataset(df_confirmed,df_recovered,df_deaths)
  Province/State Country/Region      Lat  ...  4/2/20  4/3/20  4/4/20
0            NaN    Afghanistan  33.0000  ...     273     281     299
1            NaN        Albania  41.1533  ...     277     304     333
2            NaN        Algeria  28.0339  ...     986    1171    1251
3            NaN        Andorra  42.5063  ...     428     439     466
4            NaN         Angola -11.2027  ...       8       8      10

[5 rows x 78 columns]
  Province/State Country/Region      Lat  ...  4/2/20  4/3/20  4/4/20
0            NaN    Afghanistan  33.0000  ...      10      10      10
1            NaN        Albania  41.1533  ...      76      89      99
2            NaN        Algeria  28.0339  ...      61      62      90
3            NaN        Andorra  42.5063  ...      10      16      21
4            NaN         Angola -11.2027  ...       1       1       2

[5 rows x 78 columns]
  Province/State Country/Region      Lat  ...  4/2/20  4/3/20  4/4/20
0            NaN    Afghanistan  33.0000  ...       6       6       7
1            NaN        Albania  41.1533  ...      16      17      20
2            NaN        Algeria  28.0339  ...      86     105     130
3            NaN        Andorra  42.5063  ...      15      16      17
4            NaN         Angola -11.2027  ...       2       2       2

[5 rows x 78 columns]
"""
df_conf_plot_T = country_wise_processing_of_dataset(df_confirmed)

"""
df_conf_plot_T = country_wise_processing_of_dataset(df_confirmed)
Index(['Region', '1/22/20', '1/23/20', '1/24/20', '1/25/20', '1/26/20',
       '1/27/20', '1/28/20', '1/29/20', '1/30/20', '1/31/20', '2/1/20',
       '2/2/20', '2/3/20', '2/4/20', '2/5/20', '2/6/20', '2/7/20', '2/8/20',
       '2/9/20', '2/10/20', '2/11/20', '2/12/20', '2/13/20', '2/14/20',
       '2/15/20', '2/16/20', '2/17/20', '2/18/20', '2/19/20', '2/20/20',
       '2/21/20', '2/22/20', '2/23/20', '2/24/20', '2/25/20', '2/26/20',
       '2/27/20', '2/28/20', '2/29/20', '3/1/20', '3/2/20', '3/3/20', '3/4/20',
       '3/5/20', '3/6/20', '3/7/20', '3/8/20', '3/9/20', '3/10/20', '3/11/20',
       '3/12/20', '3/13/20', '3/14/20', '3/15/20', '3/16/20', '3/17/20',
       '3/18/20', '3/19/20', '3/20/20', '3/21/20', '3/22/20', '3/23/20',
       '3/24/20', '3/25/20', '3/26/20', '3/27/20', '3/28/20', '3/29/20',
       '3/30/20', '3/31/20', '4/1/20', '4/2/20', '4/3/20', '4/4/20'],
      dtype='object')
           131   133    137           143    201
Region   India  Iran  Italy  Korea, South  Spain
1/22/20      0     0      0             1      0
1/23/20      0     0      0             1      0
1/24/20      0     0      0             2      0
1/25/20      0     0      0             2      0

"""
df_conf_plot_T = Set_Date_Index(df_conf_plot_T)
"""
df_conf_plot_T = Set_Date_Index(df_conf_plot_T)
        India Iran Italy Korea, South Spain
DATE                                       
1/22/20     0    0     0            1     0
1/23/20     0    0     0            1     0
1/24/20     0    0     0            2     0
1/25/20     0    0     0            2     0
1/26/20     0    0     0            3     0

"""
s_India_GE100,India_DT_s = Assign_Date_Index_For_each_Country(df_conf_plot_T)
"""
s_India_GE100 = Assign_Date_Index_For_each_Country(df_conf_plot_T)
DATE
3/31/20    1397
4/1/20     1998
4/2/20     2543
4/3/20     2567
4/4/20     3082
Name: India, dtype: object
DATE
3/10/20     56
3/11/20     62
3/12/20     73
3/13/20     82
3/14/20    102
Name: India, dtype: int64

graph is present in pdf
"""
India_model(s_India_GE100,India_DT_s)

"""
          Predicted_Cases
Date                       
2020-04-04             3044
2020-04-05             3494
2020-04-06             3991
2020-04-07             4536
2020-04-08             5132 [on 8th april actual confirmed cases were 5312 , actual data recorded from https://www.covid19india.org/]
2020-04-09             5781
2020-04-10             6486
2020-04-11             7248

"""