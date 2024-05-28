import numpy as np
import pandas as pd
import streamlit as st
import pickle

# Load the model and encoder
# model = pickle.load(open('model.pkl', 'rb'))

# Define unique keys for each button
keys = {
    "home_login": "home_login_btn",
    "home_signup": "home_signup_btn",
    "signup_signup": "signup_signup_btn",
    "signup_login": "signup_login_btn",
    "login_login": "login_login_btn",
    "login_signup": "login_signup_btn",
    "predict": "predict_btn",
    "logout": "logout_btn"
}

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
                margin-bottom: 20px;
            }
            .btn {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 18px;
                text-align: center;
                margin: 5px;
            }
            .btn:hover {
                background-color: #45a049;
            }
        </style>
    """, unsafe_allow_html=True)
    st.title("Driver Demand Prediction App")
    st.write("This application is designed to help you make predictions about the demand for drivers based on the data provided by you. Our platform offers a range of features to assist you in your analysis.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign Up", key=keys["home_signup"]):
            st.session_state.page = "signup"
    with col2:
        if st.button("Go to Login", key=keys["home_login"]):
            st.session_state.page = "login"

def show_signup():
    st.markdown("""
        <style>
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
                margin-bottom: 20px;
            }
            .btn-signup {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 18px;
                text-align: center;
            }
            .btn-signup:hover {
                background-color: #45a049;
            }
        </style>
    """, unsafe_allow_html=True)
    st.title("Sign Up")
    st.write("Create an account to access the prediction page.")
    new_username = st.text_input("New Username", key="signup_new_username")
    new_password = st.text_input("New Password", type="password", key="signup_new_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password")
    
    if st.button("Sign Up", key=keys["signup_signup"]):
        if new_password == confirm_password:
            st.success("Account created successfully! Please log in.")
            st.session_state.page = "login"
        else:
            st.error("Passwords do not match.")
    if st.button("Go to Login", key=keys["signup_login"]):
        st.session_state.page = "login"

def show_login():
    st.markdown("""
        <style>
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
                margin-bottom: 20px;
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
    st.title("Login")
    st.write("Please enter your credentials to access the prediction page.")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Login", key=keys["login_login"]):
        if username == "admin" and password == "password":
            st.session_state.page = "prediction"
        else:
            st.error("Invalid username or password")
    if st.button("Go to Sign Up", key=keys["login_signup"]):
        st.session_state.page = "signup"

def predict_demand():
    st.markdown("""
        <style>
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
                margin-bottom: 20px;
            }
            .btn-predict {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 18px;
                text-align: center;
            }
            .btn-predict:hover {
                background-color: #45a049;
            }
        </style>
    """, unsafe_allow_html=True)
    st.title("Predict your demand!!")
    st.write("Predict your demand!!")
    
    # Gather user input
    month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], key="predict_month")
    hour = st.number_input("Hour", 0, key="predict_hour")
    date = st.number_input("Date", 1, key="predict_date")
    location = st.selectbox("Pickup Location", ["Location 1 : Central Park", "Location 2 : Times Square", "Location 3 : Statue of Liberty", "Location 4 : Empire State Building", "Location 5 : Brooklyn Bridge"], key="predict_location")
    passenger_count = st.number_input("Passenger Count", 0, key="predict_passenger_count")
    trip_distance = st.number_input("Trip Distance", 0.0, key="predict_trip_distance")
    RateCodeID = st.selectbox("Rate Type", ['Standard rates', 'JFK trips', 'Newark trips', 'Nassau/Westchester trips', 'Negotiated fare', 'Group rides', 'unknown rate code'], key="predict_rate_code")
    tipamount = st.number_input("Tip Amount", 0.0, key="predict_tip_amount")

    if st.button("Predict", key=keys["predict"]):
        # Convert month to numeric value
        month_dict = {
            "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, 
            "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, 
            "November": 11, "December": 12}
        month_numeric = month_dict[month]

        # Read the CSV file containing pickup data
        pickup_data = pd.read_csv('pickup.csv')

        # Filter the rows where the parameters match
        filtered_data = pickup_data[
            (pickup_data['pickup_day'] == date) & 
            (pickup_data['pickup_hour'] == hour)    
        ]

        # Check if any rows match and return the last column's value
        if not filtered_data.empty:
            number_of_pickups = pickup_data.columns[-1]
            predicted_value = filtered_data[number_of_pickups].values[0]
            st.write(f"Predicted value : ({number_of_pickups}):", predicted_value)
        else:
            st.write("No data found.")
    
    if st.button("Log Out", key=keys["logout"]):
        st.write("Logging Out!")
        st.session_state.page = "login"

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Routing logic
if st.session_state.page == 'home':
    main()
elif st.session_state.page == 'signup':
    show_signup()
elif st.session_state.page == 'login':
    show_login()
elif st.session_state.page == 'prediction':
    predict_demand()
if __name__ == "__main__": 
    main()
