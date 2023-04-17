import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind


def analyze_data(data_path):
    # Load data
    data = pd.read_csv(data_path)

    # Descriptive analysis
    print("Summary statistics:")
    print(data.describe())

    # Correlation analysis
    print("Correlation matrix:")
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    corr_matrix = data[numeric_cols].corr()
    print(corr_matrix)

    # Visualize data
    sns.boxplot(x="kondisi_korban", y="jumlah_korban", data=data)
    plt.title("Number of victims by disaster type")
    plt.show()

    sns.scatterplot(x="tahun", y="jumlah_korban",
                    hue="nama_provinsi", data=data)
    plt.title("Number of victims by year and province")
    plt.show()

    # Hypothesis testing
    print("Mean number of victims by disaster type:")
    print(data.groupby('kondisi_korban')['jumlah_korban'].mean())

    print("Mean number of victims by year:")
    print(data.groupby('tahun')['jumlah_korban'].mean())

    print("Mean number of victims by province:")
    print(data.groupby('nama_provinsi')['jumlah_korban'].mean())

    # Perform t-test between two groups
    group1 = data[data['kondisi_korban'] == 'MENINGGAL DUNIA']['jumlah_korban']
    group2 = data[data['kondisi_korban'] == 'LUKA-LUKA']['jumlah_korban']
    t, p = ttest_ind(group1, group2, equal_var=False)
    print("t-statistic: {:.2f}".format(t))
    print("p-value: {:.2f}".format(p))
