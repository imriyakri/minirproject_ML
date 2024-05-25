import numpy as np
import pandas as pd
import streamlit as st 
import pickle

# Load the model and encoder
#model = pickle.load(open('model.pkl', 'rb'))

# Function to display the homepage

# Define unique keys for each button

button_key_login = "button_login"
button_key_logout = "button_logout"
button_key_login2 = "button_login2"


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

    if st.button("Go to Login",key = button_key_login):
        st.session_state.page = "login"

# Function to display the login page
def show_login():
    st.title("Login")
    st.write("Please enter your credentials to access the prediction page.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    
    if st.button("Login", key = button_key_login2):
        if username == "admin" and password == "password":
            st.session_state.page = "prediction"
        else:
            st.error("Invalid username or password")

# Function to display the prediction page
def predict_demand():
    st.title("Predict your demand!!")
    st.write("Predict your demand!!")
    
    # Gather user input
    month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    hour = st.number_input("Hour", 0)
    date = st.number_input("Date", 1)
    location = st.selectbox("Pickup Location", ["Location 1 : Central Park", "Location 2 : Times Square", "Location 3 : Statue of Liberty", "Location 4 : Empire State Building", "Location 5 : Brooklyn Bridge"])
    passenger_count = st.number_input("Passenger Count", 0)
    trip_distance = st.number_input("Trip Distance", 0.0)
    RateCodeID = st.selectbox("Rate Type", ['Standard rates', 'JFK trips', 'Newark trips', 'Nassau/Westchester trips', 'Negotiated fare', 'Group rides', 'unknown rate code'])
    tipamount = st.number_input("Tip Amount", 0.0)
    
    # Read the CSV file containing pickup data
    pickup_data = pd.read_csv('pickup.csv')
    
    # Convert month to numeric value
    month_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    month_numeric = month_dict[month]

    # Create a DataFrame with user input
    input_data = pd.DataFrame({
        'date': [date],
        'hour': [hour],
        'location': [location],
        'passenger_count': [passenger_count],
        'trip_distance': [trip_distance],
        'RateCodeID': [RateCodeID],
        'tipamount': [tipamount],
        'month': [month_numeric]
    })
    
    # Combine user input with pickup data
    combined_data = pd.concat([pickup_data, input_data], ignore_index=True)
    
    # Predict the demand using the model
    filtered_data = pickup_data[
        (pickup_data['pickup_day'] == date) & 
        (pickup_data['pickup_hour'] == hour) 
    ]

    # Check if any rows match and return the predicted value from the specified column
    if not filtered_data.empty:
        predicted_value = filtered_data['number_of_pickups'].values[0]
        return predicted_value
    




# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Routing logic
if st.session_state.page == 'home':
    main()
    
    st.session_state.page = "login"
elif st.session_state.page == 'login':
    show_login()
    
elif st.session_state.page == 'prediction':
    predict_demand()

if st.button("Log Out", key=button_key_logout):
    # Button 1 is clicked
    st.write("Logging Out!")
    st.session_state.page = "login"


if __name__ == "__main__":
    main()




