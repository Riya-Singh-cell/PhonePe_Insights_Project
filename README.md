# PhonePe Transaction Insights Dashboard

A comprehensive data visualization dashboard for analyzing PhonePe transaction data across different states and time periods using FastAPI, PostgreSQL, Python, and Streamlit.

## Project Overview

This project visualizes the PhonePe transaction data to offer insights into digital payment adoption across India. Users can filter data by year and quarter to observe transaction trends, state-wise performance, and user engagement metrics.

## Features

- Interactive Dashboard built with Streamlit
- Real-time filtering by Year and Quarter
- Visualizations including:
  - Top 10 States by Transaction Amount
  - State-wise Transaction Count Pie Chart
  - Quarterly Transaction Trend for Top States
  - TreeMap for Transaction Amount
- FastAPI backend that serves filtered data from PostgreSQL
- Clean UI with styling and smooth transitions

## Technologies Used

- Python
- Streamlit
- FastAPI
- PostgreSQL
- Pandas
- Plotly


## How It Works

1. **Data Transformation**  
   PhonePe GitHub data is transformed into structured CSVs like `map_transaction.csv` and `map_user.csv`.

2. **Database Setup**  
   PostgreSQL is used to store and query these datasets.

3. **FastAPI Backend**  
   Provides endpoints for filtered transaction/user data:
   - `/map/transactions?year=2020&quarter=2`
   - `/map/users?year=2021&quarter=3`

4. **Streamlit Dashboard**  
   Visualizes the data using:
   - Bar Chart
   - Pie Chart
   - Line Chart
   - TreeMap




