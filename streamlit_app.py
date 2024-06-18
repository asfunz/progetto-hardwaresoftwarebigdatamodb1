pip install matplotlib


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Data Analysis App')

# File uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    xls = pd.ExcelFile(uploaded_file)
    sheet_names = xls.sheet_names
    selected_sheet = st.selectbox('Select a sheet', sheet_names)
    
    # Data processing
    df = pd.read_excel(uploaded_file, sheet_name=selected_sheet)
    st.write(df.head())  # Display the first few rows of the dataframe
    
    # Visualization (example using seaborn for a pairplot)
    if st.button('Show Pairplot'):
        st.pyplot(sns.pairplot(df.select_dtypes(include=[np.number])))

# Additional processing and visualization options can be added based on the rest of the notebook content


