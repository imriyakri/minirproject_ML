import numpy as np
import pandas as pd
import streamlit as st 
from sklearn import preprocessing
import pickle

# Load the model and encoder
model = pickle.load(open('model.pkl', 'rb'))

# Function to display the homepage
def main():
    st.markdown("""
        <style>
            .main {
                background-color: #f5f5f5;
                padding: 20px;
                border-radius: 10px;
            }
            .title {
                text-align: center;
                font-size: 36px;
                color: #4CAF50;
                margin-bottom: 20px;
            }
            .header {
                font-size: 24px;
                color: #333333;
                margin-bottom: 10px;
            }
            .content {
                font-size: 18px;
                color: #666666;
                margin-bottom: 20px;
                line-height: 1.6;
            }
            .button {
                display: flex;
                justify-content: center;
            }
            .btn-login {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 18px;
                text-align: center;
            }
            .btn-login:hover {
                background-color: #45a049;
            }
        </style>
    """, unsafe_allow_html=True)
    st.title("Driver Demand Prediction App")
    st.write("This application is designed to help you make predictions about the demand of drivers based on the data provided by you.Our platform offers a range of features to assist you in your analysis.")

    if st.button("Go to Login"):
        st.session_state.page = "login"

# Function to display the login page
def show_login():
    st.title("Login")
    st.write("Please enter your credentials to access the prediction page.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.page = "prediction"
        else:
            st.error("Invalid username or password")

# Function to display the prediction page
def predict_demand(date, hour, location):
    st.title("Predict your demand!!")
    st.write("Predict your demand!!")

    month = st.selectbox("Month",["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]) 
    hour = st.number_input("Hour","0") 
    date = st.number_input("Date","1") 
    location = st.selectbox(" Pickup Location",["Location 1 : Central Park",
    "Location 2 : Times Square",
    "Location 3 : Statue of Liberty",
    "Location 4 : Empire State Building",
    "Location 5 : Brooklyn Bridge",
    "Location 6 : Metropolitan Museum of Art",
    "Location 7 : One World Trade Center",
    "Location 8 : The High Line",
    "Location 9 : Rockefeller Center",
    "Location 10 : American Museum of Natural History",
    "Location 11 : Broadway",
    "Location 12 : Battery Park",
    "Location 13 : Wall Street",
    "Location 14 : Prospect Park",
    "Location 15 : Chrysler Building",
    "Location 16 : Coney Island",
    "Location 17 : Brooklyn Botanic Garden",
    "Location 18 : The Bronx Zoo",
    "Location 19 : Grand Central Terminal",
    "Location 20 : The Guggenheim Museum",
    "Location 21 : New York Public Library",
    "Location 22 : Radio City Music Hall",
    "Location 23 : The Vessel",
    "Location 24 : Grand Army Plaza",
    "Location 25 : St. Patrick's Cathedral",
    "Location 26 : Central Park Zoo",
    "Location 27 : Flatiron Building",
    "Location 28 : The Cloisters",
    "Location 29 : Madison Square Garden",
    "Location 30 : Union Square",
    "Location 31 : Lincoln Center for the Performing Arts",
    "Location 32 : The Metropolitan Opera",
    "Location 33 : Bryant Park",
    "Location 34 : Columbia University",
    "Location 35 : The Morgan Library & Museum",
    "Location 36 : Museum of the City of New York",
    "Location 37 : Chelsea Market",
    "Location 38 : New York Botanical Garden",
    "Location 39 : The Frick Collection",
    "Location 40 : Intrepid Sea, Air & Space Museum"
    ])
    
    passenger_count = st.number_input("Passenger Count","0") 
    trip_distance = st.number_input("Trip Distance","0") 
    RateCodeID = st.selectbox("Rate Type",['Standard rates','JFK trips','Newark trips','Nassau/Westchester trips','Negotiated fare','Group rides','unknownrate code'])
    tipamount = st.number_input ("Tip Amount", "0" )

    input_data = pd.DataFrame({
            'date': [date],
            'hour': [hour],
            'location': [location],
            'passenger_count' : [passenger_count],
            'trip_distance' : [trip_distance],
            'tipamount' : [tipamount]
        })
    
    inputt_data = pd.read_csv('pickups_df.csv')
    # Predict the demand using the model
    prediction = model.predict(inputt_data)  
    return prediction[0]

if st.button("Log out"):
    st.session_state.page = "login"


# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Routing logic
if st.session_state.page == 'home':
    main()
elif st.session_state.page == 'login':
    show_login()
elif st.session_state.page == 'prediction':
    predict_demand()


if __name__ == "__main__":
    main()
