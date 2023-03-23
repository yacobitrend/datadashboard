import streamlit as st

st.set_page_config(layout='wide')

#st.title('Itrend Solution')

import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.subplots as sp
import plotly.graph_objects as go
import pandas as pd
import datetime


st.title('Marketplace Dashboard')


hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Load data

data = pd.read_csv('Pages/Sales.csv',sep=',', index_col=False)

#ASIN Details..
asin_data = pd.read_csv('Pages/ASIN-TIER.csv',sep=',', index_col=False)


data = pd.read_csv('Pages/Sales.csv',sep=',', index_col=False)

#ASIN Details..
asin_data = pd.read_csv('Pages/ASIN-TIER.csv',sep=',', index_col=False)


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
col1,col2,col3= st.columns((2,2,3))



today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=-20)


# Create a dropdown menu to select the first column name
with col1:
    start_date = st.date_input('Start date', tomorrow)
    end_date = st.date_input('End date', today)
    s_c1 = st.selectbox('Y_Axis_1:', options=columns, key='selectbox1')
    s_c2 = st.selectbox('Y_Axis_2:', options=columns,index=1, key='selectbox2')


  

# Convert the date inputs to datetime objects
start_date = pd.to_datetime(start_date).date()
end_date = pd.to_datetime(end_date).date()

# Filter the daily_totals DataFrame based on the selected date range
fil_df = daily_totals.loc[(pd.to_datetime(daily_totals['Date']).dt.date >= start_date) & 
                          (pd.to_datetime(daily_totals['Date']).dt.date <= end_date)]

# Create a dropdown menu to select the second column name
with col2:
    st.plotly_chart(bar_graph(fil_df,"Date",s_c1,s_c2))

##st.table(fil_df)



#---------------------------------------------------------
st.subheader("ASIN WISE DATA:")

### Group data by date and sum units and sales
daily_totals = data.groupby(["Date",'ASIN'])[columns].sum().reset_index()


### Format Units and Sales columns
daily_totals['Units'] = daily_totals['Units'].astype(int)
daily_totals['Sales'] = daily_totals['Sales'].astype(int)

daily_totals['Ads'] = daily_totals['Ads'].astype(int)
daily_totals['Ads'] = daily_totals['Ads'].abs()

# Create two columns
col6, col7 = st.columns((2,4))


tod1 = datetime.date.today()
tom = today + datetime.timedelta(days=-15)



# Create a dropdown menu to select the first column name
with col6:
    sta_date = st.date_input('Start date', tom,key='sel')
    ea_date = st.date_input('End date', tod1,key='sel2')
    s_c1 = st.selectbox('Y_Axis_1:', options=columns, key='selectbox3')
    s_c2 = st.selectbox('Y_Axis_2:', options=columns,index=1, key='selectbox4')



# Convert the date inputs to datetime objects
sta_date = pd.to_datetime(sta_date).date()
ea_date = pd.to_datetime(ea_date).date()


### Filter the daily_totals DataFrame based on the selected date range
fil_df = daily_totals.loc[(pd.to_datetime(daily_totals['Date']).dt.date >= sta_date) & 
                          (pd.to_datetime(daily_totals['Date']).dt.date <= ea_date)]



##### Group data by date and sum units and sales
fil = fil_df.groupby('ASIN')[columns].sum().reset_index()

with col7:

    fil_sort = fil.sort_values(by='Sales', ascending=False)[:10]

    st.plotly_chart(bar_graph(fil_sort,"ASIN",s_c1,s_c2))


##st.table(fil_sort)

##-------------------------------------

st.subheader("Split Up:")

### Group data by date and sum units and sales
daily_totals = data.groupby(["Date",'ASIN'])[columns].sum().reset_index()


### Format Units and Sales columns
daily_totals['Units'] = daily_totals['Units'].astype(int)
daily_totals['Sales'] = daily_totals['Sales'].astype(int)

daily_totals['Ads'] = daily_totals['Ads'].astype(int)
daily_totals['Ads'] = daily_totals['Ads'].abs()

# Merge the two dataframes on the 'ASIN' column
merged_df = pd.merge(daily_totals, asin_data, on='ASIN')




tod1 = datetime.date.today()
tom = today + datetime.timedelta(days=-15)

tp1,tp2=st.columns((2,2))

with tp1:
    sta_date = st.date_input('Start date', tom,key='sel4')
    s_c1 = st.selectbox('Y_Axis_1:', options=columns, key='selectbox5')
with tp2:
    ea_date = st.date_input('End date', tod1,key='sel5')
    s_c2 = st.selectbox('Y_Axis_2:', options=columns,index=1, key='selectbox6')

# Create two columns
col6, col7,col8,col9= st.tabs(["Tier-Wise Product","Manger-Wise","Team-wise","Team Member wise"])



# Convert the date inputs to datetime objects
sta_date = pd.to_datetime(sta_date).date()
ea_date = pd.to_datetime(ea_date).date()



# Create a dropdown menu to select the first column name
with col6:
    
   
        c1,c2=st.columns((4,4))

        with c1:
                        ### Filter the daily_totals DataFrame based on the selected date range
                        fil_df = merged_df.loc[(pd.to_datetime(daily_totals['Date']).dt.date >= sta_date) & 
                                  (pd.to_datetime(daily_totals['Date']).dt.date <= ea_date)]
                        ##### Group data by date and sum units and sale
                        fil = fil_df.groupby('Tier')[columns].sum().reset_index()
                        fil_sort = fil.sort_values(by='Sales', ascending=False)[:10]
                        st.plotly_chart(bar_graph(fil_sort,"Tier",s_c1,s_c2))
        with c2:
            #st.subheading("Table Data")
            st.table(fil_sort)




    

with col7:

        name='Manager'
        c3,c4=st.columns((4,4))
        

        with c3:
                        ### Filter the daily_totals DataFrame based on the selected date range
                        fil_df = merged_df.loc[(pd.to_datetime(daily_totals['Date']).dt.date >= sta_date) & 
                                  (pd.to_datetime(daily_totals['Date']).dt.date <= ea_date)]
                        ##### Group data by date and sum units and sale
                        fil = fil_df.groupby(name)[columns].sum().reset_index()
                        fil_sort = fil.sort_values(by='Sales', ascending=False)[:10]
                        st.plotly_chart(bar_graph(fil_sort,name,s_c1,s_c2))
        with c4:
            #st.subheading("Table Data")
            st.table(fil_sort)


with col8:

        name='Team Name'
        c5,c6=st.columns((4,4))
        

        with c5:
                        ### Filter the daily_totals DataFrame based on the selected date range
                        fil_df = merged_df.loc[(pd.to_datetime(daily_totals['Date']).dt.date >= sta_date) & 
                                  (pd.to_datetime(daily_totals['Date']).dt.date <= ea_date)]
                        ##### Group data by date and sum units and sale
                        fil = fil_df.groupby(name)[columns].sum().reset_index()
                        fil_sort = fil.sort_values(by='Sales', ascending=False)[:10]
                        st.plotly_chart(bar_graph(fil_sort,name,s_c1,s_c2))
        with c6:
            #st.subheading("Table Data")
            st.table(fil_sort)
            
with col9:

        name='Team Member'

        c7,c8=st.columns((4,4))
        

        with c7:
                        ### Filter the daily_totals DataFrame based on the selected date range
                        fil_df = merged_df.loc[(pd.to_datetime(daily_totals['Date']).dt.date >= sta_date) & 
                                  (pd.to_datetime(daily_totals['Date']).dt.date <= ea_date)]
                        ##### Group data by date and sum units and sale
                        fil = fil_df.groupby(name)[columns].sum().reset_index()
                        fil_sort = fil.sort_values(by='Sales', ascending=False)[:10]
                        st.plotly_chart(bar_graph(fil_sort,name,s_c1,s_c2))
                        
        with c8:
            
            #st.subheading("Table Data")
            st.table(fil_sort)
        
        

       

##-------------------------------------















