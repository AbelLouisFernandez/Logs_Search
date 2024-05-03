import streamlit as st
import requests
import subprocess
import time

# Streamlit UI elements
st.title("Logs Search")

question = st.text_input(
    "Search for something",
    placeholder="Search in logs"
)


if question:
    url = "http://localhost:8080"
    data = {"query": question}
    process = subprocess.Popen(['python', 'pdf.py'])
    process.communicate()  # Wait for the subprocess to finish
    time.sleep(3) #Wait for the pathway to get the updated logs
    response = requests.post(url, json=data, timeout=100)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")
