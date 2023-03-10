#import libraries
import pandas as pd
import numpy as np
import streamlit as st

# title of web app


def main():
    st.title('Credit Card Transactions Anomaly Detection')
    menu = ['Home']
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        st.title('Classifying credit card transaction as normal or not normal')


if __name__ == '__main__':
    main()
