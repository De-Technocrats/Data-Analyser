from by_city import total_victims
from analyzing import analyze_data
from visualization import plot_victims_trend
from predict import predict_victims

"""
De technocrats
"""


def menu():
    while True:
        print("\nWelcome to the program!")
        print("Please choose an option:")
        print("1. Total Victims by City")
        print("2. Analysis of Disaster Victims Dataset")
        print("3. Visualizing Trend of Number of Victims")
        print("4. Predict Victims")
        print("5. Exit program")
        choice = input("Enter your choice: ")
        if choice == '1':
            total_victims("data.csv")
            input("Press Enter to go back to the main menu...")
        elif choice == '2':
            analyze_data("data.csv")
            input("Press Enter to go back to the main menu...")
        elif choice == '3':
            plot_victims_trend('data.csv')
            input("Press Enter to go back to the main menu...")
        elif choice == '4':
            future_years = [2022, 2023, 2024]
            predictions = predict_victims("data.csv", future_years)
            for year, prediction in predictions.items():
                print(
                    f"The number of victims in {year} is estimated to be {prediction:.2f}")
            input("Press Enter to go back to the main menu...")
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    menu()
