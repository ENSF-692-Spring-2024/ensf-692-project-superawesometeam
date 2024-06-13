# ENSF692 Group Project
# Super Awesome Team
# Members: Amrit, Bo Zheng, Rick, Warisa
#
# To run the file, make sure to use the command: python 692Project.py, and not run it directly using VSCode
# Program to merge all csv files into one csv file, and perform analysis and plot graphs using the data. 
# Will output a csv file with the pivot table data for the selected category and country.

from ImportCSV import process_str_csv_file
from ImportCSV import process_float_csv_file

import pandas as pd

# Stage 1 & 2
def loaddata():
    '''
    Load all data from 10 csv files and merge them into one dataframe
    :@return: a dataframe that contains all data from 10 csv files
    '''
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

    df_final.to_csv("df_final.csv", index = True, header = True)
    df_final.reset_index(inplace=True)

    return df_final

def add_columns(df):
    '''
    Add columns to the dataframe for GDP per capita and Internet Penetration Rate
    :@param df: dataframe to add columns to
    :@return: dataframe with added columns
    '''

    print("\nAdding columns to the dataframe...")
    # GDP per capita
    df['GDP_per_capita'] = df['GDP_USD_Total'] / df['population']
    # percentage of the total population that has access to the Internet
    df['Internet_Penetration_Rate'] = (df['internet'].replace(',', '').astype(float) / df['population'].replace(',', '').astype(float)) * 100
    print("Successfully added columns: GDP_per_capita, Internet_Penetration_Rate\n")
    print("\nFinal dataframe saved as: output/df_export\n")
    df.to_csv("output/df_export.csv", index = True, header = True)
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
        # Life Expectancy, Total GDP, Number of Cellphones, Internet Users
        grouped_data = df_country.groupby('year').agg({
            'life_exp_year': 'mean', 
            'GDP_per_capita': 'mean',
            'cell_phone_total': 'sum',
            'Internet_Penetration_Rate': 'mean'
        })

        pivot = pd.pivot_table(df_country, values=['GDP_per_capita', 'life_exp_year', 'cell_phone_total', 'Internet_Penetration_Rate'], index='country', columns='year', aggfunc='mean')
        

    elif category == 'Economy':
        # Total GDP, Population, Inflation
        grouped_data = df_country.groupby('year').agg({
            'GDP_USD_Total': 'sum', 
            'population': 'max', 
            'inflation_percent': 'mean'
        })
        pivot = pd.pivot_table(df_country, values=['GDP_USD_Total', 'population', 'inflation_percent'], index='country', columns='year', aggfunc='mean')

    elif category == 'Energy':
        # Electricity Generation, Coal Consumption, Internet Users
        grouped_data = df_country.groupby('year').agg({
            'electricity_generation': 'sum', 
            'coal': 'mean', 
            'Internet_Penetration_Rate': 'mean'
        })
        pivot = pd.pivot_table(df_country, values=['electricity_generation', 'coal', 'Internet_Penetration_Rate'], index='country', columns='year', aggfunc='mean')

    elif category == 'Technology':
        # Number of Cellphones, Internet Users, Total GDP, Daily Income
        grouped_data = df_country.groupby('year').agg({
            'cell_phone_total': 'sum', 
            'Internet_Penetration_Rate': 'mean', 
            'GDP_USD_Total': 'sum',
            'daily_income': 'mean'
        })
        pivot = pd.pivot_table(df_country, values=['cell_phone_total', 'Internet_Penetration_Rate', 'GDP_USD_Total', 'daily_income'], index='country', columns='year', aggfunc='mean')

    elif category == 'Digital Infrastructure':
        # Number of Cellphones, Internet Users, Electricity Generation
        grouped_data = df_country.groupby('year').agg({
            'cell_phone_total': 'sum', 
            'Internet_Penetration_Rate': 'mean', 
            'electricity_generation': 'sum'
        })
        pivot = pd.pivot_table(df_country, values=['cell_phone_total', 'Internet_Penetration_Rate', 'electricity_generation'], index='country', columns='year', aggfunc='mean')


    print("Category specific aggregation and analysis:")
    print(grouped_data.describe())                          
    print("Pivot table for visualizing trends:")
    print(pivot)

    filename = f"output/{category.replace(' ', '_').lower()}_{country.lower()}_pivot.csv"

    pivot.to_csv(filename)
    print(f"Pivot table saved as '{filename}'.")
    

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
    user_input = input(prompt).strip().lower()

    # Continue prompting the user until a valid input is provided
    while user_input not in options:
        # Print an error message for invalid input
        print("Invalid input, please try again.")
        user_input = input(prompt).strip().lower()
    
     # Return the validated user input
    return user_input

def get_user_selection(df):
    """
    Function to get user selection for data filtering.

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
    }
    print("\n\nSelect a category for analysis:")
    for key, value in categories.items():
        print(f"{key}. {value}")

    info_prompt = "\nPlease select the information you want to retrieve or 0 to exit: "
    category_code = get_user_input(info_prompt, [str(i) for i in range(11)])
    if category_code == '0':
        print("***Exiting the program***")
        return None, None

    category = categories[category_code]
    country_prompt = "Please enter the country you want to analyze: "
    valid_countries = [str(val).lower() for val in df['country'].unique()]
    country = get_user_input(country_prompt, valid_countries)
    return category, country

def load_data_choice():
    print("\n\n****Data analysis program!***")
    while True:
        choice = input("\nDo you want to: \n1. Re-import data  \n2. Use preloaded data \nPlease enter '1' or '2': ").strip().lower()
        if choice == '1':
            return loaddata()
        elif choice == '2':
            try:
                return pd.read_csv('df_final.csv')
            except FileNotFoundError:
                print("File df_final.csv not found. Loading new data instead.")
                return loaddata()
        else:
            print("Invalid choice. Please enter 'load' or 'existing'.")

def main():
    try:
        df = load_data_choice()
        df = add_columns(df)
        print("\nAggregate statistics for the entire dataset:")
        print(df.describe())
        while True:
            category, country = get_user_selection(df)
            if category is None or country is None:
                break
            analyze_data(df, category, country)
    except Exception as e:
        print(f"An error occurred: {e}. \n\nExiting the program.")
        return

if __name__ == '__main__':
    main()