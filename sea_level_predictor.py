# Import all the libraries that will be used
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Definition of the function that draws the chart
def draw_plot():
    # A method of the matplotlib library that clears the state of 
    # the current figure, so charts are not plotted on top of each other.
    plt.clf() 

    # Read data from csv file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot - With all the exercises we did previously, I already knew I could
    # just pass the x and y axes. In VS Code, when you hover your mouse over the scatter method,
    # it shows you what the parameters are. So, I hovered my mouse over the scatter method and it said
    # that x and y are supposed to be array-like. Instead of passing just the name of the array,
    # I passed df['Year'] and df['CSIRO Adjusted Sea Level'] as parameters because I know
    # those return arrays.
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit - To do this, I searched and found
    # this website: https://www.w3schools.com/python/python_ml_linear_regression.asp. There
    # I learned that the linregress() function returns 5 values that you can use later, so
    # I decided to store these values in variables just like the example on the website. Each variable
    # represents one thing:
    # slope: inclination
    # intercept: where the line meets the y-axis
    # r: correlation coefficient
    # p: p-value
    # std_err: standard error
    slope, intercept, r, p, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Definition of the function that calculates the y values of the first regression line
    def CalculusOfTheLine(x):
        return slope * x + intercept # The function uses the slope, x, and the intercept.
        # It is a first degree function, so f(x) = ax + b, where slope is 'a' and intercept is 'b'.
    
    # Selection of the years
    # First, I tried the code below but it didn't work because it wasn't going up to the year 2050.
    # That's because the maximum value in the dataset for years is 2013.
    # y = list(map(CalculusOfTheLine, df['Year']))  # It's not going up to the year 2050

    # To address this, I created a list of years using the list function, starting at the minimum value of the
    # 'Year' column and going up to 2050. When you use the range function with two parameters,
    # it starts at the first value and goes up to (but does not include) the second value.
    # That's why I used 2051, so the last year included is 2050.
    # All the functions I used below I had already seen in previous lessons.
    listOfYears1 = list(range(int(df['Year'].min()), 2051))

    # Now, to create the line, I need to pass all the values in listOfYears1
    # to the function. To do this, I use the map function, and then convert the result to a list
    # since map returns a map object. This way, we get a list of y values that will form the line.
    y1 = list(map(CalculusOfTheLine, listOfYears1))

    # Plot the line - To plot the line, you just need to pass the values for the x-axis and y-axis.
    # As calculated before, the y-axis will be a list with the values stored in the y1 variable,
    # and the x-axis will be the listOfYears1 variable. This way, we get a sequence of points that,
    # when connected, form a line in the plot. I also added the color parameter to set the line color to red,
    # and the label parameter so the final chart has a legend explaining that this line refers 
    # to the years from 1880 to 2050.
    plt.plot(listOfYears1, y1, color = 'red', label = '1880-2050')

    # Create second line of best fit
    # I tried this first approach, but it didn't work because the array shapes were incompatible for broadcasting.
    # Since the 'CSIRO Adjusted Sea Level' column is longer than the 'Year' column when I try to use 
    # years from 2000 onward, the shapes don't match.
    # slope2, intercept2, r2, p2, std_err2 = linregress(list(range(2000, df['Year'].max())), 
    # df['CSIRO Adjusted Sea Level'])

    # To fix this, I filtered the original dataframe to only include rows where
    # the 'Year' column is greater than or equal to 2000. I'm also creating another dataframe
    # called df_recent so I don't modify the original one.
    df_recent = df[df['Year'] >= 2000] # Now I'm filtering the role dataframe, making both columns have the same shape
    # and allowing the linregress function to work 
    
    # Now I will use the linregress function again to store the same 5 values as before,
    # but this time for the second line. The difference is that, for the first line, I used 
    # all years from 1880 to 2050. For this second regression line, I will use only the data from years 2000 to 2050.
    slope2, intercept2, r2, p2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # List of years to be used for the second regression line, created using the list and 
    # range functions. This time, the years start at 2000 and go up to 2050.
    listOfYears2 = list(range(2000, 2051))

    # Definition of the function that calculates the y values of the second regression line
    def CalculusOfTheLine2(x):
        return slope2 * x + intercept2 # It uses the slope2 and intercept2 variables that we created before 
    
    # To get all the y values, we pass the listOfYears2 variable to the CalculusOfTheLine2
    # function using the map function. We then convert the result to a list, since map returns a map object.
    y2 = list(map(CalculusOfTheLine2, listOfYears2))

    # Now we plot the second regression line by passing the x values (listOfYears2) and the y values (y2) to plt.plot.
    # I also used the optional parameters color (to make the line green) and label (so the chart has a legend
    # explaining that this green line refers to the linear regression using the years from 2000 to 2050).
    plt.plot(listOfYears2, y2, color = 'green', label = '2000-2050')

    # Add labels and title
    plt.xlabel('Year') # Add a label for the x-axis
    plt.ylabel('Sea Level (inches)') # Add a label for the y-axis
    plt.title('Rise in Sea Level') # Add a title for the chart
    plt.legend() # Add a legend for the chart

    # Save plot and return data for testing 
    plt.savefig('sea_level_plot.png')  # Save the plot as a PNG image file. 
    return plt.gca()  # Return the current axes object for further testing