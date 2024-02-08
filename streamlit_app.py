import streamlit as st 
import pandas as pd 
import numpy as np 
df=pd
st.title('IRIS FLOWER DASHBOARD')
st.divider()
st.subheader("Description")
st.write("The flowers commonly possess three sepals, three petals, and three broad pollen-receptive stigma branches, under which the pollen-producing anthers are hidden. Of the six petal-like floral segments in irises, the more erect inner ones are called standards and the usually drooping outer ones are called falls. These flower parts are located above the ovary (inferior ovary), which consists of three carpels unified into a single pistil. Ovules within the ovary portion become seeds, and the ovary matures into dry capsule fruits.")
col1,col2=st.columns(2)
with col1:
    st.subheader("Pie chart of species")
    class_data=df['class'].value_counts() 
with col2:
    st.subheader("Bar chart of species")
    Iris=pd.DataFrame(np.random.randn(20,3),columns=["Iris-setosa","Iris-versicolor","Iris-virginica"])
    st.bar_chart(Iris)

