import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_distribution(df, column, bins=15, color='lightcoral', kde=False, mean_line=True, median_line=True):
    """
    Plots the distribution of a numeric column with improved visualization features 
    for accessibility and professionalism. Includes mean and median lines with 
    distinct styles, enhanced color contrast, and a legend for clarity.

    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing the data to be visualized.
    column : str
        The column name to plot the distribution of.
    bins : int, optional
        The number of bins for the histogram. Default is 15.
    color : str, optional
        The color of the bars in the histogram. Default is 'lightcoral'.
    kde : bool, optional
        Whether to plot the Kernel Density Estimate (KDE) curve. Default is False.
    mean_line : bool, optional
        Whether to add a mean line to the plot. Default is True.
    median_line : bool, optional
        Whether to add a median line to the plot. Default is True.
        
    Returns:
    --------
    None
        Displays the histogram with enhancements.
    """
    # Set up the plot figure size
    plt.figure(figsize=(10, 6))

    # Plot the histogram with KDE if specified
    sns.histplot(df[column], kde=kde, bins=bins, color=color, edgecolor='black')

    # Add mean line if specified
    if mean_line:
        mean_value = df[column].mean()
        plt.axvline(mean_value, color='red', linestyle='-', linewidth=2, label=f'Mean: {mean_value:.2f}')

    # Add median line if specified
    if median_line:
        median_value = df[column].median()
        plt.axvline(median_value, color='blue', linestyle='--', linewidth=2, label=f'Median: {median_value:.2f}')
    
    # Title and labels with increased font sizes for readability
    plt.title(f'Distribution of {column.replace("_", " ").title()}', fontsize=16, fontweight='bold')
    plt.xlabel(column.replace("_", " ").title(), fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    
    # Add a legend for clarification
    plt.legend(fontsize=12)
    
    sns.despine()  # Remove top and right spines for cleaner look
    
    plt.tight_layout()  # Adjust layout to fit everything
    plt.show()
    
    
def plot_categorical_distribution(df, column, title=None, xlabel=None, ylabel=None, 
                                  color='tab:blue', figsize=(8, 6), annotate=False, orientation='v'):
    """
    Visualizes the distribution of a categorical column (e.g., sales methods, states) using a count plot.
    Displays counts directly on bars for clarity. This version uses a single color and allows for horizontal 
    or vertical bar orientations.

    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing the categorical column to be visualized.
    column : str
        The column name for the categorical variable to visualize.
    title : str, optional
        The title of the plot. If None, defaults to None.
    xlabel : str, optional
        The label for the x-axis. If None, defaults to the column name.
    ylabel : str, optional
        The label for the y-axis. If None, defaults to "Count".
    color : str, optional
        The color for the bars. Default is 'tab:blue'.
    figsize : tuple, optional
        The figure size. Default is (8, 6).
    annotate : bool, optional
        Whether to annotate the bars with count values. Default is False.
    orientation : str, optional
        The orientation of the count plot, either 'h' for horizontal or 'v' for vertical. Default is 'v'.

    Returns:
    --------
    None
        Displays the count plot with the distribution of the categorical variable.
    """
    plt.figure(figsize=figsize)
    sns.set_theme(style="white")  # Set style without gridlines
    
    # Create count plot based on orientation
    if orientation == 'h':
        ax = sns.countplot(y=column, data=df, color=color, order=df[column].value_counts().index)
    else:
        ax = sns.countplot(x=column, data=df, color=color, order=df[column].value_counts().index)
    
    # Annotate bars with counts, if specified
    if annotate:
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}', 
                        (p.get_x() + p.get_width() / 2., p.get_height()) if orientation == 'h' else 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='baseline', fontsize=12, color='black')
    
    # Set plot title and labels
    plt.title(title if title else f'{column.replace("_", " ").title()} Distribution', fontsize=14)
    plt.xlabel(xlabel if xlabel else column.replace("_", " ").title(), fontsize=12)
    plt.ylabel(ylabel if ylabel else 'Count', fontsize=12)
    
    # Remove gridlines
    ax.grid(False)
    
    # Adjust layout and display plot
    plt.tight_layout()
    plt.show()
    
    
def plot_column_distribution_pie(df, value_column, category_column, 
                                  plot_title=None, figsize=(10, 8), autopct='%1.1f%%', colors=None):
    """
    Creates a pie chart to visualize the distribution of a specified value across different categories.

    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame containing the value and category data.
    value_column : str
        The name of the column representing the values to be summed (e.g., revenue).
    category_column : str
        The name of the column representing the categories (e.g., sales methods).
    plot_title : str, optional
        The title of the plot. If None, a default title is generated based on the column names.
    figsize : tuple, optional
        The size of the figure. Default is (10, 8).
    autopct : str, optional
        The format for displaying the percentage on each slice of the pie. Default is '%1.1f%%'.
    colors : list, optional
        A list of colors to use for the pie chart slices. If None, default colors are used.

    Returns:
    --------
    None
        Displays the pie chart showing the distribution of the specified value across categories.
    """
    # Group the data by category and sum the values
    category_distribution = df.groupby(category_column)[value_column].sum().reset_index()

    # Create the pie chart
    plt.figure(figsize=figsize)

    # Set custom colors if provided
    if colors is None:
        colors = plt.cm.Set1(range(len(category_distribution)))  # Use default color palette
    
    # Plot the pie chart with customized options
    plt.pie(category_distribution[value_column], autopct=autopct, colors=colors, 
            startangle=140, wedgeprops=dict(width=0.3))

    # Add a title to the chart
    plt.title(plot_title if plot_title else f'{value_column.replace("_", " ").title()} Distribution by {category_column.replace("_", " ").title()}', fontsize=16)

    # Add a legend with category labels
    plt.legend(category_distribution[category_column], title=category_column.replace("_", " ").title(), 
               loc="upper left", bbox_to_anchor=(1, 1))

    # Ensure the pie chart is drawn as a circle
    plt.axis('equal')

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Display the plot
    plt.show()

