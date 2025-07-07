import streamlit as st
from datetime import datetime, date, time
import requests
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

mydate = st.date_input("input your date", value="today", format="YYYY/MM/DD")
mytime = st.time_input("input your time", value="now")
pickup_latitude = st.number_input("pickup latitude", value=40.761432, min_value=-90.0, max_value=90.0, step=0.0001)
pickup_longitude = st.number_input("pickup longitude", value=-73.979815, min_value=-180.0, max_value=180.0, step=0.0001)
dropoff_longitude = st.number_input("dropoff longitude", min_value=-180.0, max_value=180.0, step=0.0001)
dropoff_latitude = st.number_input("dropoff lattitude", min_value=-180.0, max_value=180.0, step=0.0001)
passenger_count = st.number_input("number of passengers", min_value=0, max_value=5, step=1)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

st.image("images/téléchargement (1).jfif")

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...
'''
params = {
    "pickup_datetime" : datetime.combine(mydate, mytime).isoformat(),
    "pickup_longitude" : pickup_longitude,
    "pickup_latitude" : pickup_latitude,
    "dropoff_longitude" : dropoff_longitude,
    "dropoff_latitude" : dropoff_latitude,
    "passenger_count" :passenger_count
}

#for keys, values in params.items():
#    print(keys, values)

# Create a DataFrame with the point
df = pd.DataFrame({
    'lat': [pickup_latitude],
    'lon': [pickup_longitude]
})

# Display map
st.map(df, zoom=12)



response = requests.get(url = url, params = params).json()

print(response)
answer = f"prediction is{response}"
st.markdown(answer)
'''
3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
