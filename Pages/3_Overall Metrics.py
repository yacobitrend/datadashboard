import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.subplots as sp
import plotly.graph_objects as go
import pandas as pd

##st.set_page_config(layout='wide')
st.title('Marketplce Metrics')


hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Load data
data = pd.read_csv('sales.csv',sep=',', index_col=False)

data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Format Date column in Day-Month-Year format
data['Date'] = data['Date'].dt.strftime('%d-%b-%Y')

data=data.reset_index(drop=True)


columns=['Units', 'Sales','Ads']

def bar_graph(daily_totals,x,y1,y2):

    x=x
    s_c1=y1
    s_c2=y2

    fig = go.Figure(
        data=[
            go.Bar(x=daily_totals[x], y=daily_totals[s_c1], name=s_c1, yaxis='y', offsetgroup=1, text=daily_totals[s_c1], textposition='auto'),
            go.Bar(x=daily_totals[x], y=daily_totals[s_c2], name=s_c2, yaxis='y2', offsetgroup=2, text=daily_totals[s_c2], textposition='auto')
        ],
        layout={
            'yaxis': {'title': s_c1, 'range': [0, max(daily_totals[s_c1])+500]},
            'yaxis2': {'title': s_c2, 'overlaying': 'y', 'side': 'right', 'range': [0, max(daily_totals[s_c2])+500]}
            ,'showlegend': False
        }
    )


    return fig




### Group data by date and sum units and sales
daily_totals = data.groupby('Date')[columns].sum().reset_index()

### Format Units and Sales columns
daily_totals['Units'] = daily_totals['Units'].astype(int)
daily_totals['Sales'] = daily_totals['Sales'].astype(int)

daily_totals['Ads'] = daily_totals['Ads'].astype(int)
daily_totals['Ads'] = daily_totals['Ads'].abs()




##------------------------------------------

# Create two columns
col1, col2 = st.columns(2)

import datetime

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=-20)


# Create a dropdown menu to select the first column name
with col1:
    start_date = st.date_input('Start date', tomorrow)

# Create a dropdown menu to select the second column name
with col2:
    end_date = st.date_input('End date', today)

# Convert the date inputs to datetime objects
start_date = pd.to_datetime(start_date).date()
end_date = pd.to_datetime(end_date).date()






# Create two columns
col1, col2 = st.columns(2)

# Create a dropdown menu to select the first column name
with col1:
    s_c1 = st.selectbox('Y_Axis_1:', options=columns, key='selectbox1')

# Create a dropdown menu to select the second column name
with col2:
    s_c2 = st.selectbox('Y_Axis_2:', options=columns,index=1, key='selectbox2')




# Filter the daily_totals DataFrame based on the selected date range
fil_df = daily_totals.loc[(pd.to_datetime(daily_totals['Date']).dt.date >= start_date) & 
                          (pd.to_datetime(daily_totals['Date']).dt.date <= end_date)]


st.plotly_chart(bar_graph(fil_df,"Date",s_c1,s_c2))



st.table(fil_df.style.set_properties(**{'text-align': 'center'}))



#---------------------------------------------------------
##st.set_page_config(layout='wide')

st.subheader("ASIN WISE DATA:")

### Group data by date and sum units and sales
daily_totals = data.groupby(["Date",'ASIN'])[columns].sum().reset_index()



### Format Units and Sales columns
daily_totals['Units'] = daily_totals['Units'].astype(int)
daily_totals['Sales'] = daily_totals['Sales'].astype(int)

daily_totals['Ads'] = daily_totals['Ads'].astype(int)
daily_totals['Ads'] = daily_totals['Ads'].abs()

##------------------------------------------

# Create two columns
col6, col7 = st.columns(2)


tod1 = datetime.date.today()
tom = today + datetime.timedelta(days=-15)


# Create a dropdown menu to select the first column name
with col6:
    sta_date = st.date_input('Start date', tom,key='sel')

# Create a dropdown menu to select the second column name
with col7:
    ea_date = st.date_input('End date', tod1,key='sel2')

# Convert the date inputs to datetime objects
sta_date = pd.to_datetime(sta_date).date()
ea_date = pd.to_datetime(ea_date).date()



# Create two columns
col1, col2 = st.columns(2)

# Create a dropdown menu to select the first column name
with col1:
    s_c1 = st.selectbox('Y_Axis_1:', options=columns, key='selectbox3')

# Create a dropdown menu to select the second column name
with col2:
    s_c2 = st.selectbox('Y_Axis_2:', options=columns,index=1, key='selectbox4')

##st.table(daily_totals)


### Filter the daily_totals DataFrame based on the selected date range
fil_df = daily_totals.loc[(pd.to_datetime(daily_totals['Date']).dt.date >= sta_date) & 
                          (pd.to_datetime(daily_totals['Date']).dt.date <= ea_date)]



##### Group data by date and sum units and sales
fil = fil_df.groupby('ASIN')[columns].sum().reset_index()

fil_sort = fil.sort_values(by='Sales', ascending=False)[:10]

st.plotly_chart(bar_graph(fil_sort,"ASIN",s_c1,s_c2))


st.table(fil_sort)

##


##st.table(fil_df.style.hide_index())


