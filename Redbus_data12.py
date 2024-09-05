import streamlit as st  
import pandas as pd
import pymysql
from streamlit_option_menu import option_menu
import numpy as np
import mysql.connector as db

#streamlit app name
st.set_page_config(page_title="Redbus Data", page_icon="🚌", layout="wide")

mydb= pymysql.connect(
    
    host= 'localhost',
    user= "root",
    password= "root",
    database= "ja15"
)
print('connected')

curr = mydb.cursor()



st.title('Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit')

with st.sidebar:
    menu =option_menu(
        menu_title ="Select Any menu",
        options = ["States", "Bus Selection"],
        styles = {
            "nav-link-selected": {"background-color": "green"}
        }
    )
if menu == "States":
    st.subheader(f''"Select states")
    S = st.selectbox("States", ["Kerala(KSRTC)", "Andhra Pradesh(APSRTC)", "Telangana(TSRTC)", "Bihar(BSRTC)", "Rajasthan(RSRTC)", 
                                          "South Bengal(SBSTC)", "Himachal(HRTC)", "Assam(ASTC)", "Uttar Pradesh(UPSRTC)", "West Bengal(WBTC)"])

if menu == "Bus Selection":
    st.subheader("Bus Routes")

    # curr.execute("SELECT * FROM rd_data5")
    # data = curr.fetchall()
    # mydb = pd.DataFrame(data)
    # col = [i[0] for i in curr.description]
    # mydb =pd.DataFrame(data,columns = col)
   
    
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        select_type = st.selectbox("Choose bus type", ("sleeper", "semi-sleeper", "a\c", "non a\c"))
    with col2:
        select_price = st.radio("Choose price ", ("50-1000", "1000-2000", "2000 and above") )
    with col3:
        Select_DepTIME=st.time_input("select the dept_time")
    with col4:
        Select_ReachTIME=st.time_input("select the reach_time")
    with col5:
        select_rating = st.slider('1-5')
        
        
    def type_and_price(bus_type, price_range,rating_range):
            if price_range == "50 - 1000":
                price_min, price_max = 50, 1000
            elif price_range == "1000 -2000":
                price_min, price_max = 1000, 2000
            else:
                price_min, price_max = 2000 , 11000
            
            if rating_range == "1-2":
                rating_min, rating_max = 1, 2
            elif rating_range == "2-3":
                rating_min, rating_max = 2, 3
            else:
                rating_min, rating_max = 3, 5

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            elif bus_type == "A\C":
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Semi-Sleeper%'"
            
            Query = f'''
                SELECT * FROM rd_data5
                WHERE Price BETWEEN {price_min} AND {price_max} AND Ratings BETWEEN {rating_min} AND {rating_max}
                AND {bus_type_condition} AND Departing_time>='{Select_DepTIME}'
                ORDER BY Price and Departing_time DESC
            
            '''
            curr = mydb.cursor()
            curr.execute(Query)
            out = curr.fetchall()
        
            # mydb = pd.DataFrame(out, columns=[
            #     "Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Total_duration",
            #     "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                
            # ])

            Redbus = pd.DataFrame(out,columns=[
                "Bus_id","Bus_name", "Bus_type", "Departing_time", "Reaching_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
                
            ])
            return Redbus
    df_result = type_and_price(select_type, select_price, select_rating)
    st.dataframe(df_result)



           
              
          
              






        


    
    
    
    

















   
    





    










                                    

    
