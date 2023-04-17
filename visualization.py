import pandas as pd
import matplotlib.pyplot as plt


def plot_victims_trend(data_file):
    # Load data
    data = pd.read_csv(data_file)

    # Convert 'tahun' column to datetime type
    data['tahun'] = pd.to_datetime(data['tahun'], format='%Y')

    # Group data by 'tahun' and 'kondisi_korban' columns and sum the 'jumlah_korban' column
    grouped_data = data.groupby(['tahun', 'kondisi_korban'])[
        'jumlah_korban'].sum().reset_index()

    # Pivot the data to make 'kondisi_korban' as columns
    pivoted_data = grouped_data.pivot(
        index='tahun', columns='kondisi_korban', values='jumlah_korban')

    # Create line chart
    pivoted_data.plot(kind='line')
    plt.title('Trend of Number of Victims over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Victims')
    plt.show()
