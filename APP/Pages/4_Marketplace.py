import streamlit as st
import pandas as pd

from datetime import datetime

yr_st="2022-04-01"

tdy=datetime.today().strftime('%Y-%m-%d')

m_st=datetime.today().replace(day=1).strftime('%Y-%m-%d')



df = pd.read_csv('Customer_DB_V2 - Amazon.csv' ,sep=',', index_col=False, dtype='unicode')

print(df)


df["Quantity"] = pd.to_numeric(df["Quantity"])

df["Revenue in INR(without Tax)"] = pd.to_numeric(df["Revenue in INR(without Tax)"])

df['Date'] = pd.to_datetime(df['Date'],dayfirst=True)



print(df)


c=["K7 Anti-Virus Premium Version- 3PCs, 1 Year.",
"K7 Total Security Antivirus 2021|1 User, 3 years",
"K7 Antivirus Premium |1 User,1 Year",
"K7 Total Security Antivirus 2021 |1 User, 1 year",
"K7 Ultimate Security Antivirus Software 2021 |5 Devices, 1 Year",
"K7 Antivirus for Mac 2021|1 User,1 Year",
"K7 Ultimate Security Antivirus Software 2021 |1 Devices, 1 Year",
"K7 Mobile Security for Android|1 User, 1 Year",
"K7 Total Security Antivirus 2021|3 User, 3 years",
"K7 Ultimate Security Antivirus Software 2021 |2 Devices, 1 Year",
"K7 Ultimate Security Antivirus Software 2021 |3 Devices, 1 Year",
"K7 Ultimate Security INFINITI Antivirus | 5 Device",
"K7 Antivirus for IOS MOBILE 2021|1 User,1 Year",
"K7 Total Security Antivirus 2021|3 User, 1 year",
"K7 Total Security Antivirus 2021|5 Device, 1 year",
"K7 Ultimate Security Antivirus |1 Devices, 2 Year",
"K7 Antivirus Premium |3 User,1 Year",
"K7 Antivirus Premium |1 User,3 Year",
"K7 Ultimate Security Trial Version |1 Device, 30 Days",
"K7 Ultimate Security Antivirus Software 2022 |1 Device, 3 Year",
"K7 Anti-Virus Premium Version- 2PC, 3 Years",
"K7 Anti-Virus Premium Version- 3PC, 3 Years",
"K7 Ultimate Security Antivirus Software 2022 |3 Devices, 3 Year",
"K7 Ultimate Security Antivirus Software |5 Devices, 5 Year",
"K7 Total Security Antivirus|1 User, 2 year",
"K7 Total Security Antivirus|2 User, 1 year"]



d=["K7 Anti-Virus Premium Version- 3PCs, 1 Year.",
"K7 Total Security Antivirus |1 User, 3 years",
"K7 Antivirus Premium |1 User,1 Year",
"K7 Total Security Antivirus|1 User, 1 year",
"K7 Ultimate Security Antivirus Software |5 Devices, 1 Year",
"K7 Antivirus for Mac |1 User,1 Year",
"K7 Ultimate Security Antivirus Software |1 Devices, 1 Year",
"K7 Mobile Security for Android|1 User, 1 Year",
"K7 Total Security Antivirus |3 User, 3 years",
"K7 Ultimate Security Antivirus Software |2 Devices, 1 Year",
"K7 Ultimate Security Antivirus Software |3 Devices, 1 Year",
"K7 Ultimate Security INFINITI Antivirus | 5 Device",
"K7 Antivirus for IOS MOBILE |1 User,1 Year",
"K7 Total Security Antivirus |3 User, 1 year",
"K7 Total Security Antivirus |5 Device, 1 year",
"K7 Ultimate Security Antivirus |1 Devices, 2 Year",
"K7 Antivirus Premium |3 User,1 Year",
"K7 Antivirus Premium |1 User,3 Year",
"K7 Ultimate Security Trial Version |1 Device, 30 Days",
"K7 Ultimate Security Antivirus Software|1 Device, 3 Year",
"K7 Anti-Virus Premium Version- 2PC, 3 Years",
"K7 Anti-Virus Premium Version- 3PC, 3 Years",
"K7 Ultimate Security Antivirus Software 2022 |3 Devices, 3 Year",
"K7 Ultimate Security Antivirus Software |5 Devices, 5 Year",
"K7 Total Security Antivirus|1 User, 2 year",
"K7 Total Security Antivirus|2 User, 1 year"]


for i,x in enumerate(c):
    df['Product Name']=df['Product Name'].replace(c[i],d[i])#need to edit






def data(df,a,b):
    

    df = df.loc[(df['Date'] >=a) & (df['Date'] <= b)]

    dfs=(df.groupby(["Product Name"]).agg({'Quantity': 'sum', 'Revenue in INR(without Tax)': 'sum'}))

    dfs.loc['Total'] = dfs[['Quantity','Revenue in INR(without Tax)']].sum()

             
    data=dfs


    return data


def data_2(df,a,b):
    

    df = df.loc[(df['Date'] >=a) & (df['Date'] <= b)]

    dfs=(df.groupby(["Marketplace"]).agg({'Quantity': 'sum', 'Revenue in INR(without Tax)': 'sum'}))

    dfs.loc['Total'] = dfs[['Quantity','Revenue in INR(without Tax)']].sum()

             
    data=dfs


    return data


def data_3(df,a,b):
    
    

    df = df.loc[(df['Date'] >=a) & (df['Date'] <= b)]
 

    dfs=(df.groupby(["Date"]).agg({'Quantity': 'sum', 'Revenue in INR(without Tax)': 'sum'}))
        

    dfs.loc['Total'] = dfs[['Quantity','Revenue in INR(without Tax)']].sum()



    print(dfs.columns)

    

             
    data=dfs


    return data




st.set_page_config(layout='wide')
st.title('Marketplce Metrics')



st.write('Product Wise')
col1, col2, col3,bench = st.tabs(["YTD","MTD","FTD","BenchMark"])


with col1:

    a=yr_st
    b=tdy
    
    st.table(data(df,str(a),str(b)).style.format({'Quantity': '{:.0f}', 'Revenue in INR(without Tax)': '{:.1f}'}))
    
        
with col2:
    

    a=m_st
    print(a)
    b=tdy
    

    st.table(data(df,str(a),str(b)).style.format({'Quantity': '{:.1f}', 'Revenue in INR(without Tax)': '{:.1f}'}))

   
with col3:

    a=tdy
    b=tdy

    st.table(data(df,str(a),str(b)).style.format({'Quantity': '{:.1f}', 'Revenue in INR(without Tax)': '{:.1f}'}))



##with bench:
##    
##
##    st.table(ben.style.format({'Quantity': '{:.1f}', 'Price in INR': '{:.1f}'}))

st.write('Marketplace Wise')

co1, co2, co3,co4 = st.tabs(["YTD","MTD","FTD","Date_wise"])


with co1:

    a=yr_st
    b=tdy
    
    st.table(data_2(df,str(a),str(b)).style.format({'Quantity': '{:.0f}', 'Revenue in INR(without Tax)': '{:.1f}'}))
    
        
with co2:
    

    a=m_st
    print(a)
    b=tdy
    

    st.table(data_2(df,str(a),str(b)).style.format({'Quantity': '{:.1f}', 'Revenue in INR(without Tax)': '{:.1f}'}))

   
with co3:

    a=tdy
    b=tdy

    st.table(data_2(df,str(a),str(b)).style.format({'Quantity': '{:.1f}', 'Revenue in INR(without Tax)': '{:.1f}'}))

with co4:

    a=m_st
    print(a)
    b=tdy

    st.table(data_3(df,str(a),str(b)).style.format({'Quantity': '{:.1f}', 'Revenue in INR(without Tax)': '{:.1f}'}))































##st.sidebar.markdown("# Overall metrics 🎈")
##st.sidebar.write("# Entire Marketplace Metrics")


##a=st.date_input("From Date:")
##
##b=st.date_input("To Date:")
##st.button('Calculate')


##col1, col2, col3 = st.tabs(["Overall Metrics","Trial2Paid","Renewal"])
##
##print(type(str(a)),b)
##
##
##
##
##with col1:
##    
##    st.table(data(df,str(a),str(b)).style.format({'Quantity': '{:.0f}', 'Price in INR': '{:.0f}'}))
##    
##        
##with col2:
##
##    st.table(data(df,str(a),str(b)).style.format({'Quantity': '{:.1f}', 'Price in INR': '{:.1f}'}))
##
##
##    
##with col3:
##
##    st.table(data(df,str(a),str(b)).style.format({'Quantity': '{:.1f}', 'Price in INR': '{:.1f}'}))


##
##if st.button('Overall Metrics'):
##    
##    
##
##    st.dataframe(data(df))


