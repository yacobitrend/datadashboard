import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('Daily Data Upload')

df = pd.read_csv('Customer_DB_V2 - Amazon.csv' ,sep=',', index_col=False, dtype='unicode')


col1, col2, col3 = st.tabs(["Marketplace","Overall","Retention"])


##print(type(str(a)),b)


with col1:


    with st.form("my-form", clear_on_submit=True):

        uploaded_file = st.file_uploader("Choose a Marketplace file",label_visibility="hidden")

        submitted = st.form_submit_button("submit")
        

        

        if uploaded_file is not None:
            
            
            dataframe = pd.read_csv(uploaded_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

            
            frames = [df,dataframe]

            result = pd.concat(frames,ignore_index=False,)
            
    ##        st.write(result)

            

            if submitted==1:

                result.to_csv(("D:\\python\\performance metrics\\Customer_DB_V2 - Amazon.csv"),index=False)

                st.write("Upload sucessful")

            

            





    
    
