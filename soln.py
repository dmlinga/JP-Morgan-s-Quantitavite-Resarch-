import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import csv


class Prices:

    def __init__(self, filename="Natural Gas Data .csv"):
        self.DateToPrice = dict()

        # reading the file
        with open(filename, newline='') as csvfile:
            data = csv.DictReader(csvfile)
            # iterating through the file
            for row in data:
                month = row["Dates"]
                price = float(row["Prices"])  # Convert price to float
                # Check if the month is already in the dictionary
                if month in self.DateToPrice:
                    self.DateToPrice[month].append(price)
                else:
                    self.DateToPrice[month] = [price]

        # Extract unique dates and calculate the average price for each date
        self.dates = [datetime.strptime(date, "%m/%d/%y") for date in self.DateToPrice.keys()]
        self.prices = [np.mean(self.DateToPrice[date]) for date in self.DateToPrice.keys()]

        # Convert datetime objects to numeric values (days since the start date)
        start_date = min(self.dates)
        self.dates_numeric = [(date - start_date).days for date in self.dates]

        # Perform linear regression
        self.model = LinearRegression()
        self.dates_numeric = np.array(self.dates_numeric).reshape(-1, 1)  # Reshape for regression
        self.model.fit(self.dates_numeric, self.prices)

    def estimate_price(self, date_str: str) -> float:
        target_date = datetime.strptime(date_str, "%m/%d/%y")
        # Extrapolate one year into the future
        future_date = target_date + timedelta(days=365)
        # Convert the future date to a numeric value
        future_date_numeric = (future_date - self.dates[0]).days
        # Predict the price for the future date using linear regression
        future_price = self.model.predict(np.array([[future_date_numeric]]))
        return future_price[0]


# Example usage:
if __name__ == "__main__":
    gas_prices = Prices("Natural Gas Data .csv")
    date_to_estimate = "10/31/20"
    estimated_price = gas_prices.estimate_price(date_to_estimate)
    print(f"Estimated price on {date_to_estimate}: {estimated_price:.2f}")
