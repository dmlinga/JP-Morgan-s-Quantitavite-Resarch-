import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import csv


class Prices:

    def __init__(self, filename="Natural Gas Data .csv"):

        self.MonthToPrice = dict()
        self.PriceToMonth = dict()

        # reading the file
        with open(filename, newline='') as csvfile:
            data = csv.DictReader(csvfile)
            # iterating through the file
            for row in data:
                month = row["Dates"]
                price = row["Prices"]
                # storing the month's price
                self.MonthToPrice[month] = price
                if price not in self.PriceToMonth:
                    self.PriceToMonth[price] = [month]
                else:
                    self.MonthToPrice[price].append(month)


    def MonthToPrice(self, month: str) -> str:

        if month in self.MonthToPrice:
            return self.MonthToPrice[month]
        else:
            return ""

