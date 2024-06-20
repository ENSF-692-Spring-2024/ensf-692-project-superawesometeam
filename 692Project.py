# ENSF692 Group Project
# Super Awesome Team
# Members: Bo Zheng, Rick, Warisa
#
# This file contains the main loop
# To run the file, make sure to use the command: python 692Project.py while in the directory, and not run it directly using VSCode
# Program to merge all csv files into one csv file, and perform analysis and plot graphs using the data. 
# Will output a csv file with the pivot table data for the selected category and country.
# Will output a png file containing the plot of the data.
# Will output a csv file containing the final dataframe.

from ImportCSV import process_str_csv_file
from ImportCSV import process_float_csv_file
from matplotlib_for_692_project import compare_by_cell_phone, compare_by_GDP, compare_by_energy, compare_by_internet, compare_by_life_exp
from matplotlib_for_692_project import plot_digital_infrastructure, plot_economy, plot_energy, plot_life_quality, plot_technology


import pandas as pd

# Stage 1 & 2
def loaddata():
    '''
    Load all data from 10 csv files and merge them into one dataframe
    :@return: a dataframe that contains all data from 10 csv files
    '''
    print("\nLoading data begin....")
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
    df_population = process_str_csv_file("src/pop.csv", "population")
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
    print("\nSaving final dataframe to output/df_merged.csv\n")
    df_final.to_csv("output/df_merged.csv", index = True, header = True)
    df_final.reset_index(inplace=True)

    return df_final

def add_columns(df):
    '''
    Add columns to the dataframe for GDP per capita and Internet Penetration Rate
    :@param df: dataframe to add columns to
    :@return: dataframe with added columns
    '''

    print("\nAdding columns to the dataframe...")
    try:
        # GDP per capita
        df['GDP_per_capita'] = df['GDP_USD_Total'] / df['population']
        # percentage of the total population that has access to the Internet
        df['Internet_Penetration_Rate'] = (df['internet'].replace(',', '').astype(float) / df['population'].replace(',', '').astype(float)) * 100
        df['Energy_per_capita'] = (df['residential_electricity_use'].replace(',', '').astype(float) / df['population'].replace(',', '').astype(float))
        df['Cell_phone_per_capita'] = (df['cell_phone_total'].replace(',', '').astype(float) / df['population'].replace(',', '').astype(float))
        print("Successfully added columns: GDP_per_capita, Internet_Penetration_Rate, Energy_per_capita, Cell_phone_per_capita\n")
    except Exception as e:
        print(f"Failed to add columns, an error occurred: {e}.")
    
    
    return df

def analyze_data(df, category, country):
    '''
    Analyze the data for the selected category and country
    :@param df: dataframe to analyze
    :@param category: category to analyze
    :@param country: country to analyze
    '''

    print(f"\nAnalyzing {category} data for {country.upper()}:")
    df_country = df[df['country'].str.lower() == country.lower()]

    # masking to focus on relevant data points for each analysis
    df_country = df_country[df_country['GDP_USD_Total'] > (df_country['GDP_USD_Total'].max()*0.25)]  # masking operation

    if category == 'Life Quality':
        # Life Expectancy, GDP per capita, Number of Cellphones, Internet Users
        grouped_data = df_country.groupby('year').agg({
            'life_exp_year': 'mean', 
            'GDP_per_capita': 'mean',
            'cell_phone_total': 'sum',
            'Internet_Penetration_Rate': 'mean'
        })

        # pivot = pd.pivot_table(df_country, values=['GDP_per_capita', 'life_exp_year', 'cell_phone_total', 'Internet_Penetration_Rate'], index='country', columns='year', aggfunc='mean')
        

    elif category == 'Economy':
        # Total GDP, Population, Inflation
        grouped_data = df_country.groupby('year').agg({
            'GDP_USD_Total': 'sum', 
            'population': 'max', 
            'inflation_percent': 'mean'
        })
        # pivot = pd.pivot_table(df_country, values=['GDP_USD_Total', 'population', 'inflation_percent'], index='country', columns='year', aggfunc='mean')

    elif category == 'Energy':
        # Electricity Generation, Coal Consumption, Internet Users
        grouped_data = df_country.groupby('year').agg({
            'electricity_generation': 'sum', 
            'coal': 'mean', 
            'internet': 'mean'
        })
        # pivot = pd.pivot_table(df_country, values=['electricity_generation', 'coal', 'internet'], index='country', columns='year', aggfunc='mean')

    elif category == 'Technology':
        # Number of Cellphones, Internet penetration rate, Total GDP, Daily Income
        grouped_data = df_country.groupby('year').agg({
            'cell_phone_total': 'sum', 
            'Internet_Penetration_Rate': 'mean', 
            'GDP_USD_Total': 'sum',
            'daily_income': 'mean'
        })
        # pivot = pd.pivot_table(df_country, values=['cell_phone_total', 'Internet_Penetration_Rate', 'GDP_USD_Total', 'daily_income'], index='country', columns='year', aggfunc='mean')

    elif category == 'Digital Infrastructure':
        # Number of Cellphones, Internet Users, Electricity Generation
        grouped_data = df_country.groupby('year').agg({
            'cell_phone_total': 'sum', 
            'internet': 'mean', 
            'electricity_generation': 'sum'
        })
        # pivot = pd.pivot_table(df_country, values=['cell_phone_total', 'internet', 'electricity_generation'], index='country', columns='year', aggfunc='mean')
    

    print("Category specific aggregation and analysis:")
    print(grouped_data.describe())                          
    # print("\nPivot table for visualizing trends:")
    # print(pivot)

    filename = f"output/{category.replace(' ', '_').lower()}_{country.lower()}_pivot.csv"

    # pivot.to_csv(filename)
    # print(f"\nPivot table saved as :'{filename}'.")

    print("\nFinal dataframe saved as: 'output/df_export'\n")
    df.to_csv("output/df_export.csv", index = True, header = True)
    return grouped_data
    

def get_user_input(prompt, options):
    """
    Prompt the user for input and validate it against the provided options.

    Args:
        prompt (str): The prompt to display to the user.
        options (list): A list of valid options.

    Returns:
        str: The user's input (validated).
    """
    # Prompt the user for input and convert it to lowercase

    # Continue prompting the user until a valid input is provided
    while True:
        try:
            user_input_raw = input(prompt)
            user_input = user_input_raw.strip().lower()
            #user_input = input(prompt).strip().lower()
            if user_input not in options:
                raise ValueError("Invalid input, please try again.")

        # Print an error message for invalid input
        except ValueError as e:
            print(e)
            continue
        break
    
     # Return the validated user input
    return user_input, user_input_raw
    #return user_input, user_input_raw

def get_user_selection(df):
    """
    Function to get user selection so that the data can be analyzed.

    Args:
        df (DataFrame): The DataFrame containing the dataset.

    Returns:
        tuple: A tuple containing the user's selected information and country.
    """

    categories = {
        '1': 'Life Quality', # Life Expectancy, Total GDP USA (Inflation adjusted), Number of Cellphones, Net Internet Users (Average per year)
        '2': 'Economy', # Total GDP (Inflation adjusted), Population, Inflation annual percent
        '3': 'Energy', # Electricity generated, Total Coal Consumption, Net Internet Users (Average per year)
        '4': 'Technology', # Number of Cellphones, Net Internet Users (Average per year), Total GDP USA (Inflation adjusted), Daily income
        '5': 'Digital Infrastructure', # Number of Cellphones, Net Internet Users, Electricity Generated
        '0': 'Exit' # Exit the program
    }


    print("\n\nTopics for analysis:")
    for key, value in categories.items():
        print(f"{key}. {value}")

    info_prompt = "\nPlease select the information you want to retrieve by entering their corresponding number: "
    category_code, category_code_raw = get_user_input(info_prompt, [str(i) for i in range(6)])
    if category_code == '0':
        print("\n***Exiting the program***")
        return None, None, None
    
    # Print the list of countries available for analysis
    valid_countries = [str(val) for val in df['country'].unique()]
    print("\n\nAvailable countries:")
    for country in sorted(valid_countries):
        print(country, end="  ")

    category = categories[category_code]
    country_prompt = "\n\n\nPlease enter the country you want to analyze (Enter in displayed format): "
    valid_countries = [str(val).lower() for val in df['country'].unique()]
    #country, country_raw = get_user_input(country_prompt, valid_countries)
    country, country_raw= get_user_input(country_prompt, valid_countries)

    #return category, country, country_raw
    return category, country, country_raw


def load_data_choice():
    """
    Function to prompt the user to choose between re-importing the data or using the preloaded data.
    """
    print("\n\n\n\n******* Data analysis program *******")
    while True:
        try:
            choice = input("\nDo you want to: \n1. Re-import data. (Do this if you want to see the csv files importing and merging)  \n2. Use preloaded data. (Do this to save time and utilize merged dataset)\n0. Exit\n\nPlease make a selection by entering a number: ").strip()
            if choice == '1':
                return loaddata()
            elif choice == '2':
                try:
                    return pd.read_csv('output/df_merged.csv')
                except FileNotFoundError:
                    print("File df_merged.csv not found. Loading new data instead.")
                    return loaddata()
            elif choice == '0':
                return pd.DataFrame() # Empty DataFrame to exit the program
            else:
                raise ValueError("Invalid choice. Please enter '1','2', or '0'.")
        except ValueError as e:
            print(f"An error occurred: {e}")

def plot_after_analysis(grouped_data, data_frame, category, country):
    '''
    Generate, show, and save plots after analysis
    :@param 
        grouped_data (pandas data frame): data frame returned by function analyze_data
        data_frame (pandas data frame): data frame before running analyze_data, after running add_colums
        category (str): category selected by user
        country (str): countery selected by user
    :@return: None
    '''

    if category == 'Life Quality':
        plot_life_quality(grouped_data, country, data_frame)
    elif category == 'Economy':
        plot_economy(grouped_data, country, data_frame)
    elif category == 'Energy':
        plot_energy(grouped_data, country, data_frame)
    elif category == 'Technology':
        plot_technology(grouped_data, country, data_frame)
    elif category == 'Digital Infrastructure':
        plot_digital_infrastructure(grouped_data, country, data_frame)

def main():
    try:
        df = load_data_choice()
        if df.empty: # Exit the program if the DataFrame is empty
            print("\n***Exiting the program***")
            return
        df = add_columns(df)
        print("\nAggregate statistics for the entire dataset:")
        print(df.describe())
        while True:
            category, country, country_raw = get_user_selection(df)
            #category, country= get_user_selection(df)

            if category is None or country is None:
                break
            df_for_plot = analyze_data(df, category, country)
            while True:
                try:
                    plot_or_not = input("Do you want to view and store analysis plots for current country? (1 for yes, 2 for no): ")
                    if plot_or_not == "1":
                        print("\nPlotting the data...\nClose the plot window to continue the program.")
                        plot_after_analysis(df_for_plot, df, category, country_raw)
                        break
                    elif plot_or_not == "2":
                        break
                    else:
                        raise ValueError("Invalid input. Please enter 1 for yes or 2 for no.")
                except ValueError as e:
                    print(e)
    except Exception as e:
        print(f"An error occurred: {e}. \n\nExiting the program.")
        return

if __name__ == '__main__':
    main()