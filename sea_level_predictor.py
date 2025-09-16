import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level']  )

    #https://www.w3schools.com/python/python_ml_linear_regression.asp
    # Create first line of best fit
    slope, intercept, r, p, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    def lineCalculation(x):
        return slope * x + intercept
    
    y = list(map(lineCalculation, df['Year']))

    plt.plot(df['Year'], y)
    plt.show()
    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()