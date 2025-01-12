# -*- coding: utf-8 -*-
"""ForecastingwithProphet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ogd8OnUWRkdNj3xt3npx816NnZUnJHs4
"""

import pandas as pd
import numpy as np
from google.colab import files
import matplotlib.pyplot as plt
from prophet import Prophet

uploaded = files.upload()

data = pd.read_csv("CryptoData.csv")

data.head()

data = data.rename(columns={"date":"ds","close":"y"})

model = Prophet()
model.fit(data)

future = model.make_future_dataframe(periods=10)

forecast = model.predict(future)

# Print the results
forecasted_prices = forecast[["ds","yhat"]].tail(10)
print("Forecasted Price:")
print(forecasted_prices)

fig = model.plot(forecast)
plt.show