import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
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
        <div class="main">
            <div class="title">Driver Demand Prediction App</div>
                
            <div class="content">
                This application is designed to help you make predictions about the demand of drivers based on the data provided by you.
                Our platform offers a range of features to assist you in your analysis.
            </div>
            <div class="header">Features</div>
                
            <div class="header">Get Started</div>
            <div class="content">
                To get started, simply click the login button below. If you don't have an account,
                please contact our support team to set one up.
            </div>
            <div class="button">
                <button class="btn-login" onclick="window.location.reload();">Go to Login</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

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
def show_prediction():
    st.title("Predict your demand!!")
    st.write("Predict your demand!!")
    # Placeholder for prediction logic

    if st.button("Log out"):
        st.session_state.page = "login"

def predict_demand(day, hour, location):
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
  # Predict the demand using the model
    prediction = model.predict(input_data)
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
