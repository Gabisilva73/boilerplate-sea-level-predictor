import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Original Data')

    # Create first line of best fit for the entire dataset
    slope, intercept = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])[:2]
    years_full = pd.Series(range(1880, 2051))
    sea_level_full = intercept + slope * years_full
    ax.plot(years_full, sea_level_full, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit for data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])[:2]
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent = intercept_recent + slope_recent * years_recent
    ax.plot(years_recent, sea_level_recent, 'g', label='Best Fit Line (2000-2050)')

    # Add labels, title, and legend
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
