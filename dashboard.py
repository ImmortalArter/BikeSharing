import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency


# Load cleaned data
day_df = pd.read_csv("day.csv")

for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column])

# Filter data
min_date = day_df["order_date"].min()
max_date = day_df["order_date"].max()


