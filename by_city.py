import pandas as pd


def total_victims(data_file):
    """
    Load data and calculate total number of victims by province and regency/city.

    Parameters:
    data_file (str): file path for data in CSV format.

    Returns:
    None. Prints the total number of victims by province and regency/city.
    """
    # Load data
    data = pd.read_csv(data_file)

    # Group data by province and calculate total number of victims
    by_province = data.groupby(['kode_provinsi', 'nama_provinsi'])[
        'jumlah_korban'].sum().reset_index()

    # Group data by regency/city and calculate total number of victims
    by_regency = data.groupby(['kode_kabupaten_kota', 'nama_kabupaten_kota'])[
        'jumlah_korban'].sum().reset_index()

    # Print the results
    print("Total victims by province:")
    print(by_province)
    print("\nTotal victims by regency/city:")
    print(by_regency)
