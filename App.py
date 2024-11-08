import streamlit as st
from predict_page import show_predict_page
from predict_page_tension import show_predict_page_tension
from predict_page_slump import show_predict_page_slump


page = st.sidebar.selectbox("Response", ("Compressive Strength", "Flexural Strength", "Slump"))

if page == "Compressive Strength":
    show_predict_page()
elif page == "Flexural Strength":
    show_predict_page_tension()
else:
    show_predict_page_slump()