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

    def CalculusOfTheLine(x):
        return slope * x + intercept
    
    # y = list(map(CalculusOfTheLine, df['Year'])) It's not going by the year 20250
    listOfYears1 = list(range(int(df['Year'].min()), 2051))
    y1 = list(map(CalculusOfTheLine, listOfYears1))

    plt.plot(listOfYears1, y1, color = 'green')

    # Create second line of best fit
    # I tried this aproach but it didn't worked because the array shapes are incompatible for broadcasting
    # Since the 'CSIRO Adjusted Sea Level' column will be bigger then the 'Year' column now that i'm getting 
    # the years from 2000 above.
    # slope2, intercept2, r2, p2, std_err2 = linregress(list(range(2000, df['Year'].max())), df['CSIRO Adjusted Sea Level'])
    df_recent = df[df['Year'] >= 2000] # Now I'm filtering the role dataframe, making both columns have the same shape
    # and allowing the linregress function to work 
    slope2, intercept2, r2, p2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    listOfYears2 = list(range(2000, 2051))
    def CalculusOfTheLine2(x):
        slope2 * x + intercept2
    y2 = list(map(CalculusOfTheLine2, listOfYears2))
    plt.plot(listOfYears2, y2, color = 'red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()