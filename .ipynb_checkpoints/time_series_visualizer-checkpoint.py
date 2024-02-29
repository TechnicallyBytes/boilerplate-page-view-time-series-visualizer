



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)

df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')


# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
# Clean data

df = df[
        (df['value'] >= df['value'].quantile(0.025))&
        (df['value'] <= df['value'].quantile(0.975))
        ]


# Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.

def draw_line_plot():
    df_line_plot = df.copy()
    
    font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16
        }
    
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.plot(df_line_plot, color='red')
    ax.set_xlabel('Date', fontdict=font)
    ax.set_ylabel('Page Views', fontdict=font)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontdict=font)
    
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig



# Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    #df_bar = df.copy()
    #df_bar['Years'] = df_bar.index.year
    #df_bar['Months'] = df_bar.index.month_name()
    #df_bar = df_bar.groupby(['Years', 'Months']).mean()
    #df_bar = df_bar.rename(columns={"value": "Average Page Views"})
    #df_bar = df_bar.reset_index()
    
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Fix missing values for Jan through April of 2016 and concat with df_bar
    #missing = {
    #      "Years": [2016, 2016, 2016, 2016],
    #      "Months": ['January', 'February', 'March', 'April'],
    #      "Average Page Views": [0, 0, 0, 0]}
    #missing_months = pd.DataFrame(missing)
    #df_bar = pd.concat([missing_months, df_bar], ignore_index=False, sort=False, axis=0)

    # Draw bar plot    
    #fig = sns.catplot(data=df_bar, kind='bar', x='Years', y='Average Page Views', hue='Months', palette = 'bright')
    fig = df_bar.plot.bar(legend=True, figsize=(12, 10), ylabel='Average Page Views', xlabel='Years').figure
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    plt.legend(labels, title='Months')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


# Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize = (20,6))

    axes[0] = sns.boxplot(x='year', y='value', ax=axes[0], data=df_box)
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')

    axes[1] = sns.boxplot(x='month', y='value', ax=axes[1], data=df_box, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

