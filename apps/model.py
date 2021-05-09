import streamlit as st
import time

def app():
    st.info("Modeling under construction...Check Sometime Soon.")

    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.0)
    my_bar.progress(percent_complete + 1)
    
