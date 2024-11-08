import streamlit as st
import pickle
from pickle import load
import pandas as pd
import numpy as np

filename='saved_steps_slump.pkl'
data=load(open(filename,'rb'))

xgb_model_slump = data["model_slump"]
le_type = data["le_type"]

def show_predict_page_slump():
    st.title("Prediction of the Slump of RAFRC-FA")

    #st.write("""### We need some information to predict the Residual Compressive Strength""")
    Fiber_type=("Basalt","Carbon","Glass","Non-Fiber","Polypropylene","Steel")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        Water = st.number_input("Water (kg/$m^3$)")
        st.write("Min: 95, Max: 344")
        Cement = st.number_input("Cement (kg/$m^3$)")
        st.write("Min: 148, Max: 600")
        Sand = st.number_input("Sand (kg/$m^3$)")
        st.write("Min: 395, Max: 1005")
        NA = st.number_input("NA (kg/$m^3$)")
        st.write("Min: 0, Max: 1311")
        RCA = st.number_input("RCA (kg/$m^3$)")
        st.write("Min: 0, Max: 1267")

    with col2:
        FA = st.number_input("FA (kg/$m^3$)")
        st.write("Min: 0, Max: 255")
        SG_of_FA = st.number_input("SG of FA")
        st.write("Min: 0, Max: 2.72")
        SA_of_FA = st.number_input("SA of FA ($cm^2$/g)")
        st.write("Min: 0, Max: 4130")
        Type_of_Fibers = st.selectbox("Type of Fibres", Fiber_type)
        st.write("B, C, G, N, P, and S")
        Fibers_Vf = st.number_input("${V_f}$ (%)")
        st.write("Min: 0, Max: 6")

    with col3:
        Fibers_Length = st.number_input("Fibres' Length (mm)")
        st.write("Min: 0, Max: 50")
        Fibers_Diameter = st.number_input("Fibres' Diameter (mm)")
        st.write("Min: 0, Max: 1")
        Fibers_Fu = st.number_input("Fibres' Fu (MPa)")
        st.write("Min: 0, Max: 4900")
        Fibers_E = st.number_input("Fibres' Elastic Modulus (GPa)")
        st.write("Min: 0, Max: 250")
        RCA_Size= st.number_input("Maximum RCA Size (mm)")
        st.write("Min: 0, Max: 32")

    with col4:
        NA_Size= st.number_input("Maximum NA Size (mm)")
        st.write("Min: 0, Max: 38")
        RCA_Density= st.number_input("Density of RCA (kg/$m^3$)")
        st.write("Min: 0, Max: 2700")
        NA_Density= st.number_input("Density of NA (kg/$m^3$)")
        st.write("Min: 0, Max: 2950")
        RCA_Water_absorption= st.number_input("Water Absorption of RCA (%)")
        st.write("Min: 0, Max: 12")
        NA_Water_absorption= st.number_input("Water Absorption of NA (%)")
        st.write("Min: 0, Max: 3")

    ok = st.button("Calculate the Slump of FA-RAFRC")
    if ok:
        X = np.array([[Water, Cement, Sand, NA, RCA, FA, SG_of_FA, SA_of_FA, Type_of_Fibers, Fibers_Vf, Fibers_Length, Fibers_Diameter,
                       Fibers_Fu, Fibers_E, RCA_Size, NA_Size, RCA_Density, NA_Density,
                         RCA_Water_absorption, NA_Water_absorption]])
        X[:, 8] = le_type.transform(X[:,8])
        X = X.astype(float)
        if np.all(X == 0):
            Slump = np.array([0])
        else:
            Slump = xgb_model_slump.predict(X)
        
        st.subheader(f"The Slump of RAFRC-FA is  {Slump[0]:.2f} mm")

#show_predict_page_slump()


