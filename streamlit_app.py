from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as npy

import datetime
from datetime import date
#from data_collection import *
#import matplotlib.pyplot as plt

"""
# Welcome to our coffee list!

In order to submit a coffee break, you need to be logged in with your username and password. Pauses are then automatically generated for you.
"""

def start_break():
    return
    
def log_in(user, user_pw):
    st.write(user)
    st.write(user_pw)
    #start.disabled = False

montly_coffees=[[19, 9, 16, 19, 29, 31, 32, 30, 14, 41, 39, 34, 37, 24, 10], [15, 6, 6, 20, 29, 20, 24, 25, 29, 22, 32, 30, 35, 18, 12], [13, 6, 12, 16, 25, 35, 28, 37, 31, 27, 36, 30, 22, 14, 0], [10, 3, 7, 12, 27, 36, 37, 15, 22, 44, 10, 6, 4, 7, 1], [18, 1, 18, 21, 34, 35, 35, 26, 21, 43, 43, 27, 36, 22, 9], [0, 0, 0, 0, 19, 27, 23, 9, 5, 16, 22, 17, 26, 17, 0], [0, 0, 0, 0, 0, 12, 18, 8, 5, 13, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0]]
    
    

with st.echo(code_location='below'):
    
    col1, buff1, col2, buff2, col3 = st.columns([2,1,2,1,1])
    user = col1.text_input(label="", placeholder="Username")
    user_pw = col2.text_input(label="", type="password", placeholder="Password")
    col3.write("")
    col3.write("")
    login = col3.button("Log In", help="Log in with your username and password", on_click=log_in(user, user_pw))
    
    #start = st.button("Start break", help="Start a new coffee break", on_click=start_break())
    st.write(monthly_coffees)
    #cpm = st.write(monthly_coffees)
    #for i in range(len(monthly_coffees)):
    #    st.line_chart(monthly_coffees[i])
    
   
    
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)
    #test=st.slider("Test", "08.03.2021", "11.01.2022")

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))
    st.write(data)
    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
