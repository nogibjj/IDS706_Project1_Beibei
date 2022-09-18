import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title = 'Bike Dataset', page_icon=":bike:", layout="wide")

# df = pd.read_csv("day.csv")
# df.head()

# plt.hist(df['temp'], alpha = 0.7)

# -----Header Section --------#
st.subheader("Here is the link for the dataset")
st.write("[Link >](https://www.kaggle.com/datasets/shrutipandit707/bikesharing))")