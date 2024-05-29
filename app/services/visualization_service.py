import asyncio

import pandas as pd
from matplotlib import pyplot as plt


async def group_amounts_by_year(year: int, data):
    """
    Groups the amounts by month for a specific year using the provided data and visualizes the spending graph.

    Parameters:
    - year (int): The year for which amounts will be grouped and visualized.
    - data: The data containing information about expenditure amounts and dates.

    Operation:
    - Converts the data into a DataFrame and extracts relevant date and amount information.
    - Filters the data for the specified year and groups amounts by month.
    - Generates a spending graph to visualize the monthly expenditure for the given year.

    Note: This function uses Pandas for data manipulation and Matplotlib for plotting.
    """
    df = pd.DataFrame(data)
    dates = list()
    for date_object in df[5]:
        (name, date) = date_object
        dates.append(date)
    df[5] = pd.to_datetime(dates)
    rows_year = pd.DataFrame(df[df[5].dt.year == year])
    rows_year[5] = rows_year[5].dt.month
    amounts = list()
    for amount_object in rows_year[2]:
        (name, amount) = amount_object
        amounts.append(amount)
    rows_year[2] = amounts
    group_by = rows_year.groupby(5)[2].sum().reset_index()
    print(group_by)
    x = list(group_by[5])
    y = list(group_by[2])
    plt.plot(x, y, marker='o', linestyle='-')
    plt.title(f'Your spending graph for {year}')
    plt.xlabel('month')
    plt.ylabel('amount')
    plt.show()
