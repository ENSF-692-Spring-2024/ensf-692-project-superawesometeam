# ENSF692 Group Project
# Super Awesome Team
# Members: Amrit, Bo Zheng, Rick, Warisa
#
# Please run ImportCSV.py first before running this file
# To run the file, make sure to use the command: python 692Project.py, and not run it directly using VSCode
# Program to merge all csv files into one csv file, and perform analysis and plot graphs using the data

from ImportCSV import process_str_csv_file
from ImportCSV import process_float_csv_file

import pandas as pd

# Stage 1 & 2: import all csv files
# @return: a dataframe that contains all data from 10 csv files
def loaddata():
    print("Loading data begin....")
    print("1. Loading inflation data...")
    df_inflation = process_float_csv_file("src/inflation_annual_percent.csv", "inflation_percent")
    print(df_inflation.size, "values imported successfully...")

    print("2. Loading mincpcap data...")
    df_mincpcap = process_float_csv_file("src/mincpcap_cppp.csv", "daily_income")
    print(df_mincpcap.size, "values imported successfully...")

    print("3. Loading internet user data...")
    df_internet = process_str_csv_file("src/net_users_num.csv", "internet")
    print(df_internet.size, "values imported successfully...")

    print("4. Loading coal consumption data...")
    df_coal_consu = process_str_csv_file("src/coal_consumption_total.csv", "coal")
    print(df_coal_consu.size, "values imported successfully...")

    print("5. Loading total GDP data...")
    df_GDP_total = process_str_csv_file("src/total_gdp_us_inflation_adjusted.csv", "GDP_USD_Total")
    print(df_GDP_total.size, "values imported successfully...")

    print("6. Loading life expectancy data...")
    df_life_exp = process_float_csv_file("src/lex.csv", "life_exp_year")
    print(df_life_exp.size, "values imported successfully...")

    print("7. Loading population data...")
    df_population = process_str_csv_file("src/pop.csv", "polulation")
    print(df_population.size, "values imported successfully...")

    print("8. Loading electricity generation data...")
    df_electricity_gen = process_str_csv_file("src/electricity_generation_total.csv", "electricity_generation")
    print(df_electricity_gen.size, "values imported successfully...")

    print("9. Loading electricity consumption data...")
    df_resi_electricity_consu = process_str_csv_file("src/residential_electricity_use_total.csv", "residential_electricity_use")
    print(df_resi_electricity_consu.size, "values imported successfully...")

    print("10. Loading cell phone user data...")
    df_cell_phone = process_str_csv_file("src/cell_phones_total.csv", "cell_phone_total")
    print(df_cell_phone.size, "values imported successfully...")

    print("Finished data import.")

    # Merge 10 csv files
    print("Merging data...")
    df_list = [df_inflation, df_coal_consu, df_internet, df_mincpcap, df_GDP_total, df_life_exp, df_population, df_electricity_gen, df_resi_electricity_consu, df_cell_phone]
    df_final = df_list[0]

    print(len(df_list))

    # Merge all dataframes
    for i in range(1, len(df_list)):
        print(".")
        df_final = pd.merge(df_final, df_list[i], left_index=True, right_on=['country', 'year'])
    print("Final data size:", df_final.shape)
    print("Finished data merge.")
    print("Data preview:")
    print(df_final.head(3))
    df_final.to_csv("df_final.csv", index = True, header = True)

    return df_final

def get_user_input(prompt, options):
    # Prompt the user for input and convert it to lowercase
    user_input = input(prompt).strip().lower()

    # Continue prompting the user until a valid input is provided
    while user_input not in options:
        # Print an error message for invalid input
        print("Invalid input, please try again.")
        # Prompt the user again for input and convert it to lowercase
        user_input = input(prompt).strip().lower()
    
     # Return the validated user input
    return user_input

def get_user_selection(df):

    # Define the options dictionary
    info_options = {
        '1': 'Inflation annual percent',
        '2': 'Total Coal Consumption',
        '3': 'Net Internet Users',
        '4': 'Daily income ($ earned/person on a daily basis)',
        '5': 'Total GDP USA (Inflation adjusted)',
        '6': 'Life Expectancy',
        '7': 'Population',
        '8': 'ELectricity generated',
        '9': 'Residential Electricity Consumption',
        '10': 'Number of Cellphones'
    }
    # Display the available options to the user
    print("\nThe program can provide the following information for a selected country:")
    for option, info in info_options.items():
        print(f"{option}. {info}")

    # Prompt the user to select an option
    info_prompt = "\nPlease select the information you want to retrieve or 0 to exit: "
    info_selection = get_user_input(info_prompt, [str(i) for i in range(11)])

    # Check if the user wants to exit
    if info_selection == '0':
        print("***Exiting the program***")
        return None, None
    
    # Prompt the user to enter the country
    country_prompt = "Please enter the country you want to search: "
    # Create a list of valid country names from the DataFrame, converted to lowercase for comparison
    valid_countries = [str(val).lower() for val in df.reset_index()['country'].unique()]
    country = get_user_input(country_prompt, valid_countries)

    return info_selection, country

def main():
    try:
        df = loaddata()
    except Exception as e:
        print("Error:", e)
        print("Please check the error and try again.")
        return
    
    while True:
        info, country = get_user_selection(df)

        if info is None or country is None:
            break

        # Placeholder for the function that will calculate and display the output
        # This function will be implemented in the next step
        print("\n" + f"Country selected: {country.upper()}")
        info_options = {
            '1': 'Inflation annual percent',
            '2': 'Total Coal Consumption',
            '3': 'Net Internet Users',
            '4': 'Daily income ($ earned/person on a daily basis)',
            '5': 'Total GDP USA (Inflation adjusted)',
            '6': 'Life Expectancy',
            '7': 'Population',
            '8': 'ELectricity generated',
            '9': 'Residential Electricity Consumption',
            '10': 'Number of Cellphones'
        }
        print(f"Information selected: {info_options[info]}")



if __name__ == '__main__':
    main()