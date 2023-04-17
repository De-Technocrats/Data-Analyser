import pandas as pd
from sklearn.linear_model import LinearRegression


def predict_victims(data_file, future_years):
    # Load data and group by year
    data = pd.read_csv(data_file).groupby('tahun')[
        'jumlah_korban'].sum().reset_index()

    # Train model
    model = LinearRegression().fit(data[['tahun']], data['jumlah_korban'])

    # Predict future values
    future_predictions = model.predict(
        pd.DataFrame(future_years, columns=['tahun']))

    # Create a dictionary to store the predictions
    predictions_dict = {}
    for year, prediction in zip(future_years, future_predictions):
        predictions_dict[year] = prediction

    return predictions_dict
