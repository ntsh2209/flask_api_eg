import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'cusip': ['123456', '123456', '123456', '654321', '654321', '654321', '789012', '789012', '789012'],
    'invQty': [100, 150, 120, 80, 70, 75, 60, 65, 62],
    'loanQty': [50, 55, 60, 40, 35, 38, 45, 48, 47],
    'date': ['2024-01-01', '2024-01-02', '2024-01-03', 
             '2024-01-01', '2024-01-02', '2024-01-03',
             '2024-01-01', '2024-01-02', '2024-01-03']
}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])  # Ensure the date column is in datetime format

# Define the reusable plotting function
def plot_time_series(dataframe, cusips, y_columns):
    plt.figure(figsize=(12, 8))
    
    # Loop through each specified CUSIP
    for cusip in cusips:
        filtered_df = dataframe[dataframe['cusip'] == cusip]
        
        # Loop through each specified y-column
        for y_col in y_columns:
            plt.plot(filtered_df['date'], filtered_df[y_col], label=f'{cusip} - {y_col}', marker='o')
    
    # Adding labels, title, and legend
    plt.xlabel('Date')
    plt.ylabel('Quantity')
    plt.title('Time Series Plot for Selected CUSIPs')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Puts the legend outside the plot
    plt.grid(True)
    
    # Show plot with adjusted layout
    plt.tight_layout()
    plt.show()

# Example usage
cusips_to_plot = ['123456', '654321']  # Specify CUSIPs you want to plot
y_columns_to_plot = ['invQty', 'loanQty']  # Specify columns you want to plot on the y-axis

plot_time_series(df, cusips=cusips_to_plot, y_columns=y_columns_to_plot)
