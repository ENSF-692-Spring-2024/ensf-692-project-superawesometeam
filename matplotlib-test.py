import pandas as pd
import matplotlib.pyplot as plt
from ImportCSV import process_float_csv_file

#Author: Warisa

def analyze_data(df, category, country):
    '''
    Analyze the data for the selected category and country
    :param df: dataframe to analyze
    :param category: category to analyze
    :param country: country to analyze
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
            'Internet_Penetration_Rate': 'mean',
            'population': 'max'  # Ensure population is included
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
    print(grouped_data.describe())                          # Aggregation computation
    print("Pivot table for visualizing trends:")
    print(pivot)

    filename = f"output/{category.replace(' ', '_').lower()}_{country.lower()}_pivot.csv"

    pivot.to_csv(filename)
    print(f"Pivot table saved as '{filename}'.")

    # Warisa added return at June12th
    #
    #
    # Notice Frank to return a value
    return grouped_data

def add_columns(df):
    '''
    Add columns to the dataframe for GDP per capita and Internet Penetration Rate
    :param df: dataframe to add columns to
    :return: dataframe with added columns
    '''

    print("\nAdding columns to the dataframe...")
    # GDP per capita
    df['GDP_per_capita'] = df['GDP_USD_Total'] / df['population']
    # percentage of the total population that has access to the Internet
    df['Internet_Penetration_Rate'] = (df['internet'].replace(',', '').astype(float) / df['population'].replace(',', '').astype(float)) * 100
    print("Successfully added columns: GDP_per_capita, Internet_Penetration_Rate\n")
    return df

df = pd.read_csv('df_final.csv')
df = add_columns(df)
category = 'Life Quality'
country = 'china'
plot_df = analyze_data(df, category, country)
#print(plot_df)

def plot_life_quality(grouped_data, country):
    years = grouped_data.index
    start_year = years.min()
    end_year = years.max()

    # Extracting data for each subplot
    life_exp = grouped_data['life_exp_year']
    gdp = grouped_data['GDP_per_capita']
    cellphones = grouped_data['cell_phone_total']
    internet_users = grouped_data['Internet_Penetration_Rate']
    
    # Creating figure and subplots
    fig, axs = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle(f'Life Quality Trends in {country.capitalize()} from {start_year} to {end_year}', fontsize=16)

    # Subplot 1: Life Expectancy and GDP per Capita
    ax1 = axs[0]
    ax2 = ax1.twinx()
    ax1.plot(years, life_exp, marker='o', linestyle='-', color='b', label='Life Expectancy')
    ax2.plot(years, gdp, marker='o', linestyle='-', color='g', label='GDP per Capita')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Life Expectancy (Years)', color='b')
    ax2.set_ylabel('GDP per Capita (USD)', color='g')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2.tick_params(axis='y', labelcolor='g')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax1.set_title('Life Expectancy and GDP per Capita')

    # Subplot 2: Number of Cellphones and Internet Users
    ax3 = axs[1]
    ax4 = ax3.twinx()
    ax3.plot(years, cellphones, marker='o', linestyle='-', color='r', label='Number of Cellphones')
    ax4.plot(years, internet_users, marker='o', linestyle='-', color='m', label='Internet Users')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Number of Cellphones (in 100 million)', color='r')
    ax4.set_ylabel('Internet Users (Percentage)', color='m')
    ax3.tick_params(axis='y', labelcolor='r')
    ax4.tick_params(axis='y', labelcolor='m')
    ax3.legend(loc='upper left')
    ax4.legend(loc='upper right')
    ax3.set_title('Number of Cellphones and Internet Users')

    # Save the plot as a PNG file
    filename = f'output/life_quality_{country.lower()}_grouped.png'
    plt.savefig(filename)
    plt.show()

plot_life_quality(plot_df, country)

