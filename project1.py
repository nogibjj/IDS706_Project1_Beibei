import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##################
df = pd.read_csv("day.csv")


c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)


################

with st.container():

    st.set_page_config(page_title = 'Bike Dataset', page_icon=":bike:", layout="wide")

    # -----Header Section --------#
    st.subheader("Here is the link for the dataset")
    st.write("[Link >](https://www.kaggle.com/datasets/shrutipandit707/bikesharing)")



    # df = pd.read_csv("day.csv")
    # df.head()

    # plt.hist(df['temp'], alpha = 0.7)