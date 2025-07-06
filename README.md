# PhonePe Transaction Insights

## Project Overview

This project analyzes and visualizes PhonePe's digital transaction data across various categories, states, and time periods. The insights generated help understand trends in user engagement, payment behavior, and geographical usage.

## Domain

Finance / Payment Systems

## Skills Demonstrated

- Data Extraction
- ETL (Extract, Transform, Load)
- SQL Proficiency
- Data Analysis using Python
- Data Visualization using Chart.js and HTML
- FastAPI for backend APIs
- Git and GitHub for version control
- Documentation

## Problem Statement

With increasing digital payment adoption, analyzing large-scale transaction data is essential for business strategy and service improvements. This project focuses on:

- Aggregated analysis of payment categories
- User engagement metrics
- Insurance-related insights
- State- and district-level mapping
- Top-performing states, districts, and brands


## Project Structure
PhonePe_Insights_Project/
├── app/
│ └── routes/
│ ├── aggregated.py
│ ├── map.py
│ └── top.py
├── exports/
│ └── transformed/
│ ├── aggregated_transaction.csv
│ ├── aggregated_user.csv
│ └── ... (other CSVs)
├── pulse/
│ └── data/
├── scripts/
│ └── transform_and_export.py
├── main.py
├── index.html
├── style.css
└── README.md


## Approach

### 1. Data Extraction

- Cloned the GitHub dataset from PhonePe Pulse
- Cleaned and transformed CSVs using Python
- Stored structured data into PostgreSQL

### 2. Backend with FastAPI

- Created REST API endpoints for aggregated data
- Enabled filters (by year, quarter)

### 3. Frontend Visualization

- Built interactive dashboards with HTML and Chart.js
- Included filters for year/quarter
- Visualized transaction counts and amounts (bar and pie charts)

### 4. Insights Generated

- Recharge & bill payments and peer-to-peer transfers dominate transaction volume
- Mobile brand usage highlights Xiaomi and Samsung as leaders in earlier years
- Transaction volume has grown significantly year over year

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL
- Git
- VS Code (or any IDE)

### Installation

```bash
git clone https://github.com/yourusername/PhonePe_Insights_Project.git
cd PhonePe_Insights_Project
pip install -r requirements.txt


