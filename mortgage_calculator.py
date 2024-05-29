import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Function to plot the distribution of parameters
def dist_of_params(frame, variable, title):
    frame_reset_index = frame.reset_index(drop=True)  # Reset index to avoid duplicate labels
    sns.FacetGrid(frame_reset_index, height=10).map(sns.kdeplot, variable).add_legend()
    if variable in frame.columns:
        plt.title(title)
        plt.xlabel(variable)  # Set x-axis label
        plt.ylabel('Density')         # Set y-axis label
        plt.grid(True)                # Add grid lines
        st.pyplot(plt)  # Display the plot using Streamlit
    else:
        st.error(f"Variable '{variable}' not found in the dataframe.")

# Function to display the homepage
def main():
    if st.session_state.page == 'home':
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
        st.write("This application is designed to help you make predictions about the demand of drivers based on the data provided by you. Our platform offers a range of features to assist you in your analysis.")

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
            st.experimental_rerun()  # Refresh the app to reflect the new state
        else:
            st.error("Invalid username or password")

# Function to display the prediction page
def predict_demand():
    st.title("Predict Your Demand")
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
    try:
        pickup_data = pd.read_csv('pickup.csv')
    except Exception as e:
        st.error(f"Error loading 'pickup.csv': {e}")
        return

    # Convert month to numeric value
    month_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    month_numeric = month_dict.get(month)
    if month_numeric is None:
        st.error("Invalid month selected.")
        return

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

    # Add the buttons side by side
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Predict"):
            # Predict the demand using the model (mocked here as we don't have the actual model)
            filtered_data = pickup_data[
                (pickup_data['pickup_day'] == date) &
                (pickup_data['pickup_hour'] == hour)
            ]

            if not filtered_data.empty:
                predicted_value = filtered_data['number_of_pickups'].values[0]
                st.write(f"Predicted number of pickups: {predicted_value}")
            else:
                st.write("No data available for the selected inputs.")
    with col2:
        if st.button("Show Graphs"):
            # Read the additional dataset for plotting
            try:
                additional_data = pd.read_csv('frame_with_durations_outliers_removed.csv')
            except Exception as e:
                st.error(f"Error loading 'frame_with_durations_outliers_removed.csv': {e}")
                return
            
            # Plot distribution of trip times
            dist_of_params(additional_data, 'trip_times', 'Time for cab trips distribution (in minutes)')

            # Log trip times
            log_trip_times = additional_data.trip_times.values
            additional_data['log_times'] = np.log(log_trip_times)
            dist_of_params(additional_data, 'log_times', 'Log of time for cab trips distribution')

            # Plot distribution of trip distances
            log_trip_distance = additional_data.trip_distance.values
            additional_data['log_distance'] = np.log(log_trip_distance)
            dist_of_params(additional_data, 'trip_distance', 'Distance for cab trips distribution')

            # Log trip distances
            dist_of_params(additional_data, 'log_distance', 'Log of distance for cab trips distribution')

            # Plot distribution of trip speed
            dist_of_params(additional_data, 'Speed', 'Average speed of cab trips distribution')

            # Log trip speed
            log_trip_speed = additional_data.Speed.values
            additional_data['log_speed'] = np.log(log_trip_speed)
            dist_of_params(additional_data, 'log_speed', 'Log of speed for cab trips distribution')

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

# Run the app
if __name__ == "__main__":
    main()
