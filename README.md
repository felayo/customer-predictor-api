# Backend API – Setup & Usage Guide

This project implements a machine learning–based customer behaviour prediction system designed to determine whether a customer will subscribe to a bank term deposit.

This section explains how to clone, install, run, and inspect the Flask API locally..
It is the backend API for the Customer's Behaviour Predictor

# System Architecture

```
React GUI
   |
   v
Flask REST API
   |
   v
Machine Learning Model (Artificial Neural Network, Logistic Regression, Gradient Boosting, LightGBM, Gradient Descent)
   |
   v
SQLite Database (Prediction Logs)

```


# Requirements

```
Python 3.14.2
SQLite
GIT
```

# Clone the Project from GitHub
Open a terminal (Command Prompt, PowerShell, or Terminal) and run:
```
git clone https://github.com/felayo/customer-predictor-api
```

Then move into the backend directory:
```
cd customer-predictor-api
```

# Setup

## Virtual environment

How to setup a python virtual environment

- Create the virtual environment,

  ```
  python -m venv .venv
  ```

- Activate the virtual environment
  - for windows
  ```
  .venv\Scripts\activate
  ```
  - for Linux / macOS
  ```
  source .venv/bin/activate
  ```
- Deactivate the virtual environment when you need to,

  ```
  deactivate
  ```

## Install requirements

For local development

```
pip install -r requirements.txt
```


## **Run the Flask API**

Start the application using:

```
python app.py
```

If successful, you will see output similar to:

```
Running on http://127.0.0.1:5000
```
The API is now running locally.

## Test the Prediction Endpoint
The API exposes a prediction endpoint:

```
POST /predict
```

It accepts JSON input and returns a prediction and probability.

This endpoint is consumed automatically by the React frontend.

## SQLite Database (Prediction Logs)
All predictions are automatically stored in a local SQLite database file
```
predictions.db
```
### Inspecting the Database
In the backend directory, run:
```
sqlite3 predictions.db
```

Inside the SQLite prompt, run:
```
.tables
```

To view stored predictions:
```
SELECT * FROM prediction_logs;
```

Exit SQLite:
```
.exit
```

### Export Prediction Logs (CSV)
An export script is provided to extract logged predictions.
Run:
```
python exportdb.py
```

This will generate a CSV file containing:

Input parameters

Model predictions

Probability values

Timestamps

The exported file can be used for:

Analysis

Tables

Graphs

Research evidence