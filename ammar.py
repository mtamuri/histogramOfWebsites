import requests
import time
import csv
import streamlit as st
from streamlit_lottie import st_lottie
import datetime as dt
from PIL import Image
from datetime import date

st.set_page_config(page_title="SysProg, Ammar's Project", page_icon=":👨‍💻:")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/279133b8-d82b-4d56-870d-daae4fce9a1b/OX1EXSxzFL.json")

st.title('Welcome to Histogram and availability checker!\nWebApp built for systems programming by: [Ammar MT.](https://ammarmt.tech/) ©')


st.write(
    'Please select the website you want to check the availability of'
)

websites = {
    "Google": "https://www.google.com",
    "Saat Teknoloji": "https://saatteknoloji.com/",
    "Beykoz Official Website": "https://beykoz.edu.tr/",
    "OIS": "https://ois.beykoz.edu.tr",
}

selection = st.selectbox("Select a website:", websites.keys())
website_url = websites.get(selection)

if selection:
    st.write(f"You selected: {selection}")
    st.write(f"Website URL: {website_url}")

# Initialize variables
selected_option = None
show_slider = False

# Multiselect options
options = ['Day', 'Hour', 'Minute', 'Second']

# Get the selected option from the multiselect
selected_option = st.selectbox('Label goes here', options, help='time intervals')


# Show the slider bar only if "Second" is selected
if 'Second' in selected_option:
    show_slider = True

# Display the slider bar
if show_slider:
    st.slider(
        'intervals to check availability in minutes',
        15,
        60,
        45,
        help='slide the bar to select the interval in minutes'
    )

selected_date = st.date_input(
    "Select the date to see the history of the website's availability.\nAvailable date's is between January 1st 2023 and Today.",
    date.today(),
    min_value=date(2023, 1, 1),
    max_value=date.today(),  # Restrict date selection to today or earlier
    help="Get the history",
)   

if selection and selected_date:
    st.write(f"You selected: {selection}")
    st.write(f"Selected Date: {selected_date}")

# Initialize the button state variables
show_chart = False
hide_chart = False

st.write(
    f'Below you can see the charts and the history for the history of the availability of: {selection}   '
)

# Check website availability only if the selected website matches the website being checked
if st.button('Show history', help='click the message to show the history of the availability of the website'):
    # Check website availability and update chart
    response_times = []
    for i in range(10):
        start_time = time.perf_counter()
        response = requests.get(website_url)  # Use the selected website URL here
        end_time = time.perf_counter()
        response_time = end_time - start_time
        response_times.append(response_time)

    show_chart = True  # You can use this variable to trigger chart display in your Streamlit app

# Show the chart
if show_chart:
    chart_data = {'round': [i + 1 for i in range(10)], 'response_time': response_times}
    st.bar_chart(
        data=chart_data,
        x='round',
        y='response_time'
    )

    if show_chart and not hide_chart:
        if st.button('Hide chart', help='click the message to hide the chart'):
            hide_chart = True
st_lottie(lottie_coding, height=600, key="coding")

st.write('''
        This app is built by [Ammar MT.](https://ammarmt.tech/) ©
        ''')
