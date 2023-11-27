import requests
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

st.title('Welcome to Histogram and availability checker!\nApp built by Ammar MT. ©')

st.write(
    'Please select the website you want to check the availability of'
    )

websites = {
    "Google": "https://www.google.com",
    "Saat Teknoloji": "https://saatteknoloji.com/",
    "Beykoz Official Website": "https://www.beykoz.edu.tr/",
    "OIS": "https://online.beykoz.edu.tr",
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
    "Select the date to see the history of the website's availability",
    date.today(),
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
    'Below you can see the charts and the history for the history of the availability of the website.   '
)

if st.button('Show history', help='click the message to show the history of the availability of the website'):
    show_chart = True

# Show the "Hide chart" button only when the chart is showing
if show_chart:
    st.line_chart(
        # Enter your data below! Usually this is not a dict, but a Pandas Dataframe.,
        data={'time': [0, 1, 2, 3, 4, 5, 6], 'stock_value': [100, 200, 150, 300, 450, 500, 600]},
        x='time',
        y='stock_value'
    )

    if show_chart and not hide_chart:
        if st.button('Hide chart', help='click the message to hide the chart'):
            hide_chart = True
st_lottie(lottie_coding, height=600, key="coding")
