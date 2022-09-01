# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:52:16 2022

@author: Zach
"""

import pandas as pd
# import yfinance as yf
import datetime as dt
from datetime import  date, timedelta
# import matplotlib as mpl
from yahoo_fin import stock_info
import streamlit as st

symbols = pd.read_csv('symbols.csv')
tickers = symbols['Ticker'].sort_values().tolist() 
ticker = st.selectbox('Choose a stock',tickers)
    
yesterday = date.today() - timedelta(days=1)
yesterday.strftime('%m%d%y')

st.subheader('Single Stock Daily Performance')
stonkForm = st.form("Enter Ticker")
inputTicker = stonkForm.text_input('Ticker Symbol',value=ticker)
submit_button = stonkForm.form_submit_button("GO")
if submit_button:
    start = dt.datetime.now()
    name = stock_info.get_data(ticker)
    name = list(name['ticker'])
    name = name[0]
    stock = stock_info.get_live_price(ticker)
    stock = round(stock,2)
    last = stock_info.get_data(ticker,start_date=start)
    last = list(last['open'])
    change = stock/round(last[0],2)-1
    st.metric(label=name,value=stock,delta=change)
else:
    st.subheader('Press GO')
