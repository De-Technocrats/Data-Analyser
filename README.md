# Disaster Victims Dataset Analysis

<p align="center">
  <img src="https://img.freepik.com/free-vector/process-optimization-concept-idea-business-improvement-development-company-data-analysis-effective-entrepreneurship-organization-isolated-flat-vector-illustration_613284-3337.jpg">
</p>

This repository contains Python code for analyzing and visualizing the disaster victims dataset. The dataset provides information about the number of victims by year, province, and disaster type in Indonesia. The code uses various Python libraries, including pandas, matplotlib, seaborn, and scikit-learn. The data used is obtained [from here](https://opendata.jabarprov.go.id/id/dataset/jumlah-korban-jiwa-akibat-bencana-berdasarkan-kondisi-di-jawa-barat).
## Dependencies

The code requires the following dependencies:

-   pandas
-   matplotlib
-   seaborn
-   scipy
-   scikit-learn

You can install these dependencies using pip. For example:

`pip install -r requirements.txt` 

## Usage

To use the code, follow these steps:

1.  Clone the repository or download the files.
2.  Open a terminal or command prompt and navigate to the directory containing the files.
3.  Run the Python script using the command `python main.py`.
4.  Choose one of the options from the menu to perform an analysis.

## Functions

The following functions are available in the code:

-   `plot_victims_trend(data_file)`: Plots the trend of the number of victims over time.
-   `analyze_data(data_path)`: Performs descriptive analysis, correlation analysis, and hypothesis testing on the data.
-   `total_victims(data_file)`: Calculates the total number of victims by province and regency/city.
-   `predict_victims(data_file, future_years)`: Predicts the number of victims for future years using linear regression.
-   `menu()`: Provides a menu to choose from the available functions.

## License

The code is available under the [MIT License](https://github.com/De-Technocrats/Disaster-Victims-Dataset-Analysis/blob/main/LICENSE).