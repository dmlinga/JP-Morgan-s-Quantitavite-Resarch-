def calculate_contract_value(injection_dates, withdrawal_dates, purchase_prices, sale_prices, injection_rate, max_volume, storage_costs):
    """
    Calculate the value of a gas storage contract.

    Args:
        injection_dates (list): List of injection dates.
        withdrawal_dates (list): List of withdrawal dates.
        purchase_prices (list): List of purchase prices on injection dates.
        sale_prices (list): List of sale prices on withdrawal dates.
        injection_rate (float): Rate at which gas can be injected per day.
        max_volume (float): Maximum volume that can be stored.
        storage_costs (float): Storage costs per day per unit of gas stored.

    Returns:
        float: The value of the gas storage contract.
    """
    contract_value = 0.0  # Initialize the contract value

    # Calculate the value for each injection and withdrawal date pair
    for i in range(len(injection_dates)):
        injection_date = injection_dates[i]
        withdrawal_date = withdrawal_dates[i]
        purchase_price = purchase_prices[i]
        sale_price = sale_prices[i]

        # Calculate the injected volume and stored volume
        injected_volume = injection_rate * (withdrawal_date - injection_date)
        stored_volume = min(injected_volume, max_volume)  # Limited by max_volume

        # Calculate the cost of storage for the stored volume
        storage_cost = stored_volume * storage_costs * (withdrawal_date - injection_date)

        # Calculate the profit for this transaction
        profit = (sale_price - purchase_price) * stored_volume

        # Add the profit and subtract the storage cost to the contract value
        contract_value += profit - storage_cost

    return contract_value

def main():
    injection_dates = [1, 10, 20]  # Dates in days
    withdrawal_dates = [5, 15, 25]  # Dates in days
    purchase_prices = [2.0, 2.5, 3.0]  # Prices in $/MMBtu
    sale_prices = [3.5, 3.0, 2.8]  # Prices in $/MMBtu
    injection_rate = 10000.0  # MMBtu per day
    max_volume = 50000.0  # MMBtu
    storage_costs = 0.01  # $/MMBtu per day

    contract_value = calculate_contract_value(injection_dates, withdrawal_dates, purchase_prices, sale_prices,
                                              injection_rate, max_volume, storage_costs)

    print("Contract Value: ${:,.2f}".format(contract_value))

if __name__ == '__main__':
    main()
