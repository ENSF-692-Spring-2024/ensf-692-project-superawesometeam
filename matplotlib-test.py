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

#plot_life_quality(plot_df, country)

category = 'Economy'
plot_df = analyze_data(df, category, country)

def plot_economy(grouped_data, country):
    years = grouped_data.index
    start_year = years.min()
    end_year = years.max()

    gdp_total = grouped_data['GDP_USD_Total'] / 1e9  # Convert GDP to 100 Million USD
    population = grouped_data['population'] / 1e6  # Convert population to million

    inflation = grouped_data['inflation_percent']
    
    fig, axs = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle(f'Economy Trends in {country.capitalize()} from {start_year} to {end_year}', fontsize=16)

    ax1 = axs[0]
    ax2 = ax1.twinx()
    ax1.plot(years, gdp_total, marker='o', linestyle='-', color='b', label='Total GDP (100 Million USD)')
    ax2.plot(years, population, marker='o', linestyle='-', color='g', label='Population (Million)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total GDP (100 Million USD)', color='b')
    ax2.set_ylabel('Population (Million)', color='g')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2.tick_params(axis='y', labelcolor='g')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax1.set_title('Total GDP and Population')

    ax3 = axs[1]
    ax3.plot(years, inflation, marker='o', linestyle='-', color='r', label='Inflation')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Inflation (%)', color='r')
    ax3.tick_params(axis='y', labelcolor='r')
    ax3.legend(loc='upper left')
    ax3.set_title('Inflation')

    filename = f'output/economy_{country.lower()}_grouped.png'
    plt.savefig(filename)
    plt.show()

#plot_economy(plot_df, country)

category = 'Energy'
plot_df = analyze_data(df, category, country)

def plot_energy(grouped_data, country):
    years = grouped_data.index
    start_year = years.min()
    end_year = years.max()

    # Convert units as necessary
    electricity_generation = grouped_data['electricity_generation'] / 1e6  # Convert MWh to million MWh
    coal_consumption = grouped_data['coal'] / 1e6  # Convert tons to million tons
    internet_users = grouped_data['Internet_Penetration_Rate']  # Already in percentage

    # Creating figure and subplots
    fig, axs = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle(f'Energy Trends in {country.capitalize()} from {start_year} to {end_year}', fontsize=16)

    # Subplot 1: Electricity Generation and Coal Consumption
    ax1 = axs[0]
    ax2 = ax1.twinx()
    ax1.plot(years, electricity_generation, marker='o', linestyle='-', color='b', label='Electricity Generation (Million MWh)')
    ax2.plot(years, coal_consumption, marker='o', linestyle='-', color='g', label='Coal Consumption (Million Tons)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Electricity Generation (Million MWh)', color='b')
    ax2.set_ylabel('Coal Consumption (Million Tons)', color='g')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2.tick_params(axis='y', labelcolor='g')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax1.set_title('Electricity Generation and Coal Consumption')

    # Subplot 2: Internet Users
    ax3 = axs[1]
    ax3.plot(years, internet_users, marker='o', linestyle='-', color='r', label='Internet Users (%)')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Internet Users (Percentage)', color='r')
    ax3.tick_params(axis='y', labelcolor='r')
    ax3.legend(loc='upper left')
    ax3.set_title('Internet Users')

    # Save the plot as a PNG file
    filename = f'output/energy_{country.lower()}_grouped.png'
    plt.savefig(filename)
    plt.show()

#plot_energy(plot_df, country)

category = 'Technology'
plot_df = analyze_data(df, category, country)

def plot_technology(grouped_data, country):
    years = grouped_data.index
    start_year = years.min()
    end_year = years.max()

    # Extracting data for each subplot
    cellphones = grouped_data['cell_phone_total'] / 1e8  # Convert to 100 Million
    internet_users = grouped_data['Internet_Penetration_Rate']
    gdp_total = grouped_data['GDP_USD_Total'] / 1e9  # Convert to 100 Million USD 
    daily_income = grouped_data['daily_income']
    
    # Creating figure and subplots
    fig, axs = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle(f'Technology Trends in {country.capitalize()} from {start_year} to {end_year}', fontsize=16)

    # Subplot 1: Number of Cellphones and Internet Users
    ax1 = axs[0]
    ax2 = ax1.twinx()
    ax1.plot(years, cellphones, marker='o', linestyle='-', color='b', label='Number of Cellphones (100 Million)')
    ax2.plot(years, internet_users, marker='o', linestyle='-', color='g', label='Internet Users')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Cellphones (100 Million)', color='b')
    ax2.set_ylabel('Internet Users (Percentage)', color='g')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2.tick_params(axis='y', labelcolor='g')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax1.set_title('Number of Cellphones and Internet Users')

    # Subplot 2: Total GDP and Daily Income
    ax3 = axs[1]
    ax4 = ax3.twinx()
    ax3.plot(years, gdp_total, marker='o', linestyle='-', color='r', label='Total GDP (100 Million USD)')
    ax4.plot(years, daily_income, marker='o', linestyle='-', color='m', label='Daily Income')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Total GDP (100 Million USD)', color='r')
    ax4.set_ylabel('Daily Income (USD)', color='m')
    ax3.tick_params(axis='y', labelcolor='r')
    ax4.tick_params(axis='y', labelcolor='m')
    ax3.legend(loc='upper left')
    ax4.legend(loc='upper right')
    ax3.set_title('Total GDP and Daily Income')

    # Save the plot as a PNG file
    filename = f'output/technology_{country.lower()}_grouped.png'
    plt.savefig(filename)
    plt.show()

#plot_technology(plot_df, country)

category = 'Digital Infrastructure'
plot_df = analyze_data(df, category, country)

def plot_digital_infrastructure(grouped_data, country):
    years = grouped_data.index
    start_year = years.min()
    end_year = years.max()

    # Extracting data for each subplot
    cellphones = grouped_data['cell_phone_total'] / 1e8  # Convert to 100 Million
    internet_users = grouped_data['Internet_Penetration_Rate']
    electricity_generation = grouped_data['electricity_generation'] / 1e6  # Convert to Million MWh
    
    # Creating figure and subplots
    fig, axs = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle(f'Digital Infrastructure Trends in {country.capitalize()} from {start_year} to {end_year}', fontsize=16)

    # Subplot 1: Number of Cellphones and Internet Users
    ax1 = axs[0]
    ax2 = ax1.twinx()
    ax1.plot(years, cellphones, marker='o', linestyle='-', color='b', label='Number of Cellphones (100 Million)')
    ax2.plot(years, internet_users, marker='o', linestyle='-', color='g', label='Internet Users')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Cellphones (100 Million)', color='b')
    ax2.set_ylabel('Internet Users (Percentage)', color='g')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2.tick_params(axis='y', labelcolor='g')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax1.set_title('Number of Cellphones and Internet Users')

    # Subplot 2: Electricity Generation
    ax3 = axs[1]
    ax3.plot(years, electricity_generation, marker='o', linestyle='-', color='r', label='Electricity Generation (Million MWh)')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Electricity Generation (Million MWh)', color='r')
    ax3.tick_params(axis='y', labelcolor='r')
    ax3.legend(loc='upper left')
    ax3.set_title('Electricity Generation')

    # Save the plot as a PNG file
    filename = f'output/digital_infrastructure_{country.lower()}_grouped.png'
    plt.savefig(filename)
    plt.show()

#plot_digital_infrastructure(plot_df, country)