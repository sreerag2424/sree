import pickle
import streamlit as st
from os import path
import numpy as np 


st.title("Flower Classificstion App")

file_name = "lr_model.pkl"
with open(path.join("model",file_name),'rb') as f:
    lr_modle = pickle.load(f)

sl = st.number_input("Insert a sepel length")
sw = st.number_input("Insert a sepel width")
pl = st.number_input("Imsert a petal length")
pw = st.number_input("Insert a petal width")

if st.button("Predict"):
    pred = lr_modle.predict(np.array([[sl,sw,pl,pw]]))
    st.write("The Flower is :",pred[0])
