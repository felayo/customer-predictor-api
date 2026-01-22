# Expected request from React
POST /predict
Content-Type: application/json

{
  "default": "no",
  "balance": 1200,
  "housing": "yes",
  "day": 15,
  "month": "jul",
  "campaign": 2,
  "previous": 0,
  "poutcome": "unknown",
  "duration": 300
}

# Expected response
```
{
  "probability": 0.6732,
  "prediction": 1,
  "message": "Customer will subscribe bank Term Deposit"
}

{
    "message": "Customer will subscribe",
    "prediction": 1,
    "probability": 0.5232
}
```

OR

```
{
  "probability": 0.3128,
  "prediction": 0,
  "message": "Customer will not subscribe to bank Term Deposit"
}

```
## to run the api
export FLASK_APP=app.py
flask run