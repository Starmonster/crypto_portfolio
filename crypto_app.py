import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import datetime
import time

matplotlib.use('Agg')
plt.style.use('fivethirtyeight')

import os
os.environ['TZ'] = 'UTC'

from app_functions import *

# load in the portfolio and transactions
load_port = open("my_portfolio.pkl", "rb")
portfolio = pickle.load(load_port)

# transactions
load_trans = open("my_transactions.pkl", "rb")
transactions = pickle.load(load_trans)





def main():
    """Crypto portfolio tracker and analysis app """

    st.title("Cryptocurrency portfolio analysis")
    st.subheader("To the MOOOON 2!!")

    st.text("You hodl the following cryptocurrencies:")
    for i in simple_portfolio(portfolio):
        st.write(i, "qty")

    # Create a user input to request which coin they would like to review
    hodling = list(portfolio.keys())
    analysis = st.text_input("What would you like to look at? Enter a coin name such as 'bitcoin' or type 'overall' ", "bitcoin")
    ## Need to  add in a loop for invalid inputs - drop down menus on app?

    while analysis:
        if analysis in hodling:
            # We're good - you have that coin in your portfolio
            break
        else:
            # We bad, you have entered an invalid coin - either a typo or you don't hodl it!
            analysis = st.text_input("ERROR: You do not hodl that coin, please enter the name of a coin that you "
                                     "hodl in your portfolio")

    # Write a user input for the timeframe they would like to investigate
    timeframe = st.text_input("What timeframe would you like to review performance over? Enter 30d, 90d, portfolio", "portfolio")

    while timeframe:
        if timeframe == "30d" or timeframe == "90d" or timeframe == "portfolio":
            # Accepted entries! we can move on
            break
        else:
            timeframe = st.text_input("You have entered an invalid timeframe, please enter 30d, 90d or portfolio")

    df, coin, percent_change, timeframe_data = terminal(portfolio, transactions, timeframe, analysis)

    # my_name = st.text_input("What is your name?", "name")
    # st.text(my_name)

    # st.dataframe(df)

    if timeframe == "30d":
        st.text(f'{coin} has had a {percent_change}% change this month!')
    elif timeframe == "90d":
        st.text(f'{coin} has had a {percent_change}% change this quarter!')
    elif timeframe == "portfolio":
        st.text(f'{coin} has had a {percent_change}% change since investment!')


    # Plot the graph to show performance thro' requested period
    fig, ax = plt.subplots(figsize=(12, 7))
    # plt.figure(figsize=(12,7))
    if timeframe_data.price.iloc[-1] > timeframe_data.price.iloc[0]:
        ax.plot(timeframe_data.price, label=coin.capitalize() + " price", color="b")
    elif timeframe_data.price.iloc[-1] <= timeframe_data.price.iloc[0]:
        ax.plot(timeframe_data.price, label=coin.capitalize() + " price", color="r")
    else:
        st.text("...no data")

    ax.set_title(coin.capitalize() + " price for current " + timeframe + " period")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price(USD)")
    # plt.xticks(rotation=45)
    fig.autofmt_xdate()
    plt.legend()

    # show graph in streamlit
    st.pyplot(fig)

if __name__ == '__main__':
    main()
