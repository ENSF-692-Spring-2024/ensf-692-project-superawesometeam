import pandas as pd
import matplotlib.pyplot as plt
from ImportCSV import process_float_csv_file
import numpy as np

#Author: Warisa

# -----------   Rick's Functions for pivot table ploting   -----------------#



def compare_by_GDP(data_frame, country):
    """
    Reduce original data frame to selected country, country with highest GDP_per_capita, and country with lowest GDP_per_capita

    Args:
        data_frame (pandas data frame): data frame before running analyze_data, after adding add_columns

    Returns:
        compare_by_GDP_table ( pandas data frame): reduced data frame that contains data of selected country, country with highest GDP_per_capita
    """
    df_gdp_per_capita = pd.DataFrame(data_frame['GDP_per_capita'].groupby(data_frame['country']).mean())
    max_value = df_gdp_per_capita.max().values[0]
    min_value = df_gdp_per_capita.min().values[0]
    df_mean = df_gdp_per_capita.reset_index()
    country_max = df_mean['country'][df_mean['GDP_per_capita'] == max_value].values[0]
    country_min = df_mean['country'][df_mean['GDP_per_capita'] == min_value].values[0]
    #print("Max GDP", country_max, max_value)
    #print("Min GDP", country_min, min_value)
    #print(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(z['country'] == country_max) | (z['country'] == country_min) | (z['country'] == 'China')])
    compare_by_GDP_table = pd.DataFrame(data_frame[['country', 'year','GDP_per_capita']][(data_frame['country'] == country_max) | (data_frame['country'] == country_min) | (data_frame['country'] == country)])
    
    return compare_by_GDP_table.reset_index()

def compare_by_internet(data_frame, country):
    """
    Reduce original data frame to selected country, country with highest Internet_Penetration_Rate, coutry with lowest Internet_Penetration_Rate

    Args:
        data_frame (pandas data frame): data frame before running analyze_data, after adding add_columns

    Returns:
        compare_by_internet_table (pandas data frame): reduced data frame that contains data of selected country, country with highest Internet_Penetration_Rate, coutry with lowest Internet_Penetration_Rate

    """
    df_internet = pd.DataFrame(data_frame['Internet_Penetration_Rate'].groupby(data_frame['country']).mean())
    max_value = df_internet.max().values[0]
    min_value = df_internet.min().values[0]
    df_mean = df_internet.reset_index()
    country_max = df_mean['country'][df_mean['Internet_Penetration_Rate'] == max_value].values[0]
    country_min = df_mean['country'][df_mean['Internet_Penetration_Rate'] == min_value].values[0]
    #print("Max Internet", country_max, max_value)
    #print("Min Internet", country_min, min_value)
    #print(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(z['country'] == country_max) | (z['country'] == country_min) | (z['country'] == 'China')])
    compare_by_internet_table = pd.DataFrame(data_frame[['country', 'year', 'Internet_Penetration_Rate']][(data_frame['country'] == country_max) | (data_frame['country'] == country_min) | (data_frame['country'] == country)])
    
    return compare_by_internet_table.reset_index()

def compare_by_life_exp(data_frame, country):
    """
    Reduce original data frame to selected country, country with highest life_exp_year, coutry with lowest life_exp_year

    Args:
        data_frame (pandas data frame): data frame before running analyze_data, after adding add_columns

    Returns:
        compare_by_life_exp_table (pandas data frame): reduced data frame that contains data of selected country, country with highest life_exp_year, coutry with lowest life_exp_year

    """
    df_life_exp = pd.DataFrame(data_frame['life_exp_year'].groupby(data_frame['country']).mean())
    max_value = df_life_exp.max().values[0]
    min_value = df_life_exp.min().values[0]
    df_mean = df_life_exp.reset_index()
    country_max = df_mean['country'][df_mean['life_exp_year'] == max_value].values[0]
    country_min = df_mean['country'][df_mean['life_exp_year'] == min_value].values[0]
    #print("Max Internet", country_max, max_value)
    #print("Min Internet", country_min, min_value)
    #print(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(z['country'] == country_max) | (z['country'] == country_min) | (z['country'] == 'China')])
    compare_by_life_exp_table = pd.DataFrame(data_frame[['country', 'year', 'life_exp_year']][(data_frame['country'] == country_max) | (data_frame['country'] == country_min) | (data_frame['country'] == country)])
    
    return compare_by_life_exp_table.reset_index()


def compare_by_energy(data_frame, country):
    """
    Reduce original data frame to selected country, country with highest Energy_per_capita, coutry with lowest Energy_per_capita

    Args:
        data_frame (pandas data frame): data frame before running analyze_data, after adding add_columns

    Returns:
        compare_by_energy_table (pandas data frame): reduced data frame that contains data of selected country, country with highest Energy_per_capita, coutry with lowest Energy_per_capita

    """
    df_energy = pd.DataFrame(data_frame['Energy_per_capita'].groupby(data_frame['country']).mean())
    max_value = df_energy.max().values[0]
    min_value = df_energy.min().values[0]
    df_mean = df_energy.reset_index()
    country_max = df_mean['country'][df_mean['Energy_per_capita'] == max_value].values[0]
    country_min = df_mean['country'][df_mean['Energy_per_capita'] == min_value].values[0]
    #print("Max Internet", country_max, max_value)
    #print("Min Internet", country_min, min_value)
    #print(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(z['country'] == country_max) | (z['country'] == country_min) | (z['country'] == 'China')])
    compare_by_energy_table = pd.DataFrame(data_frame[['country', 'year','Energy_per_capita']][(data_frame['country'] == country_max) | (data_frame['country'] == country_min) | (data_frame['country'] == country)])
    
    return compare_by_energy_table.reset_index()

def compare_by_cell_phone(data_frame, country):
    """
    Reduce original data frame to selected country, country with highest Cell_phone_per_capita, coutry with lowest Cell_phone_per_capita

    Args:
        data_frame (pandas data frame): data frame before running analyze_data, after adding add_columns

    Returns:
        compare_by_cell_phone_table (pandas data frame): reduced data frame that contains data of selected country, country with highest Cell_phone_per_capita, coutry with lowest Cell_phone_per_capita

    """
    df_cell_phone = pd.DataFrame(data_frame['Cell_phone_per_capita'].groupby(data_frame['country']).mean())
    max_value = df_cell_phone.max().values[0]
    min_value = df_cell_phone.min().values[0]
    df_mean = df_cell_phone.reset_index()
    country_max = df_mean['country'][df_mean['Cell_phone_per_capita'] == max_value].values[0]
    country_min = df_mean['country'][df_mean['Cell_phone_per_capita'] == min_value].values[0]
    #print("Max Internet", country_max, max_value)
    #print("Min Internet", country_min, min_value)
    #print(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(z['country'] == country_max) | (z['country'] == country_min) | (z['country'] == 'China')])
    compare_by_cell_phone_table = pd.DataFrame(data_frame[['country', 'year','Cell_phone_per_capita']][(data_frame['country'] == country_max) | (data_frame['country'] == country_min) | (data_frame['country'] == country)])
    
    return compare_by_cell_phone_table.reset_index()




#-----------------------------------------#



#df = pd.read_csv('df_final.csv')
#df = add_columns(df)

#category = 'Life Quality'
#country = 'Egypt'
#plot_df = analyze_data(df, category, country)

def plot_life_quality(grouped_data, country, data_frame):
    years = grouped_data.index
    start_year = years.min()
    end_year = years.max()

    # Extracting data for each subplot
    life_exp = grouped_data['life_exp_year']
    gdp = grouped_data['GDP_per_capita']
    cellphones = grouped_data['cell_phone_total']
    internet_users = grouped_data['Internet_Penetration_Rate']

    # Creating figure and subplots
    fig, axs = plt.subplots(3, 1, figsize=(12, 8), constrained_layout=True)
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


    # Rick added a pivot table plot -------#

    life_exp_df_for_pivot = compare_by_life_exp(data_frame, country)
    #print(digital_infrastructure_df_for_pivot)
    life_exp_pivot_table = life_exp_df_for_pivot.pivot_table('life_exp_year', index='year', columns='country')
    plot_3 = axs[2]
    plot_3.set_title(' '.join(['Life Expectancy (Years)', ''.join(['(', country]) , 'vs the highest and lowest in the world)']))
    plot_3.set_xlabel('Year')
    plot_3.set_ylabel('Life Expectancy (Years)')
    plot_3.plot(life_exp_pivot_table, marker='o', linestyle='-')
    plot_3.set_xticks(np.arange(life_exp_df_for_pivot['year'].min(), life_exp_df_for_pivot['year'].max() + 1, 1))
    plot_3.legend(life_exp_pivot_table.columns)

    filename_pivot = f"output/{country.lower()}_life_quality_pivot.csv"

    life_exp_pivot_table.to_csv(filename_pivot)
    print(f"\nPivot table saved as '{filename_pivot}'.")


   
    # -------------------------------------#


    # Save the plot as a PNG file
    filename = f'output/life_quality_{country.lower()}_grouped.png'
    print("\nGraph saved as:", filename, "\n")
    plt.savefig(filename)
    plt.show()

#plot_life_quality(plot_df, country, df)

#category = 'Economy'
#plot_df = analyze_data(df, category, country)

def plot_economy(grouped_data, country, data_frame):
    years = grouped_data.index
    start_year = years.min()
    end_year = years.max()

    gdp_total = grouped_data['GDP_USD_Total'] / 1e9  # Convert GDP to 100 Million USD
    population = grouped_data['population'] / 1e6  # Convert population to million

    inflation = grouped_data['inflation_percent']
    
    fig, axs = plt.subplots(3, 1, figsize=(12, 8), constrained_layout=True)
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


    # Rick added a pivot table plot -------#

    economy_df_for_pivot = compare_by_GDP(data_frame, country)
    #print(digital_infrastructure_df_for_pivot)
    economy_pivot_table = economy_df_for_pivot.pivot_table('GDP_per_capita', index='year', columns='country')
    plot_3 = axs[2]
    plot_3.set_title(' '.join(['GDP_per_capita', ''.join(['(', country]) , 'vs the highest and lowest in the world)']))
    plot_3.set_xlabel('Year')
    plot_3.set_ylabel('GDP per Capita (USD)')
    plot_3.plot(economy_pivot_table, marker='o', linestyle='-')
    plot_3.set_xticks(np.arange(economy_df_for_pivot['year'].min(), economy_df_for_pivot['year'].max() + 1, 1))
    plot_3.legend(economy_pivot_table.columns)

    filename_pivot = f"output/{country.lower()}_economy_pivot.csv"

    economy_pivot_table.to_csv(filename_pivot)
    print(f"\nPivot table saved as '{filename_pivot}'.")

   
   
    # -------------------------------------#


    filename = f'output/economy_{country.lower()}_grouped.png'
    print("\nGraph saved as:", filename, "\n")
    plt.savefig(filename)
    plt.show()

#plot_economy(plot_df, country,df)

#category = 'Energy'
#plot_df = analyze_data(df, category, country)

def plot_energy(grouped_data, country, data_frame):
    years = grouped_data.index
    start_year = years.min()
    end_year = years.max()

    # Convert units as necessary
    electricity_generation = grouped_data['electricity_generation'] / 1e6  # Convert MWh to million MWh
    coal_consumption = grouped_data['coal'] / 1e6  # Convert tons to million tons
    internet_users = grouped_data['internet']  # Already in percentage

    # Creating figure and subplots
    fig, axs = plt.subplots(3, 1, figsize=(12, 8), constrained_layout=True)
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

    # Rick added a pivot table plot -------#

    energy_df_for_pivot = compare_by_energy(data_frame, country)
    #print(digital_infrastructure_df_for_pivot)
    energy_pivot_table = energy_df_for_pivot.pivot_table('Energy_per_capita', index='year', columns='country')
    plot_3 = axs[2]
    plot_3.set_title(' '.join(['Electricity per Capita', ''.join(['(', country]) , 'vs the highest and lowest in the world)']))
    plot_3.set_xlabel('Year')
    plot_3.set_ylabel('Electricity per Capita (KWh)')
    plot_3.plot(energy_pivot_table, marker='o', linestyle='-')
    plot_3.set_xticks(np.arange(energy_df_for_pivot['year'].min(), energy_df_for_pivot['year'].max() + 1, 1))
    plot_3.legend(energy_pivot_table.columns)

    filename_pivot = f"output/{country.lower()}_energy_pivot.csv"

    energy_pivot_table.to_csv(filename_pivot)
    print(f"\nPivot table saved as '{filename_pivot}'.")

   
   
    # -------------------------------------#



    # Save the plot as a PNG file
    filename = f'output/energy_{country.lower()}_grouped.png'
    print("\nGraph saved as:", filename, "\n")
    
    plt.savefig(filename)
    plt.show()

#plot_energy(plot_df, country, df)

#category = 'Technology'
#plot_df = analyze_data(df, category, country)

def plot_technology(grouped_data, country, data_frame):
    years = grouped_data.index
    start_year = years.min()
    end_year = years.max()

    # Extracting data for each subplot
    cellphones = grouped_data['cell_phone_total'] / 1e8  # Convert to 100 Million
    internet_users = grouped_data['Internet_Penetration_Rate']
    gdp_total = grouped_data['GDP_USD_Total'] / 1e9  # Convert to 100 Million USD 
    daily_income = grouped_data['daily_income']
    
    # Creating figure and subplots
    fig, axs = plt.subplots(3, 1, figsize=(12, 8), constrained_layout=True)
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

    # Rick added a pivot table plot -------#
    
    technology_df_for_pivot = compare_by_internet(data_frame, country)
    #print(digital_infrastructure_df_for_pivot)
    technology_pivot_table = technology_df_for_pivot.pivot_table('Internet_Penetration_Rate', index='year', columns='country')
    plot_3 = axs[2]
    plot_3.set_title(' '.join(['Internet Users (Percentage)', ''.join(['(', country]) , 'vs the highest and lowest in the world)']))
    plot_3.set_xlabel('Year')
    plot_3.set_ylabel('Internet Users (Percentage)')
    plot_3.plot(technology_pivot_table, marker='o', linestyle='-', label=['Internet Users (Percentage)', '1', '1'])
    plot_3.set_xticks(np.arange(technology_df_for_pivot['year'].min(), technology_df_for_pivot['year'].max() + 1, 1))
    plot_3.legend(technology_pivot_table.columns)

    filename_pivot = f"output/{country.lower()}_technology_pivot.csv"

    technology_pivot_table.to_csv(filename_pivot)
    print(f"\nPivot table saved as '{filename_pivot}'.")

  
   
    # -------------------------------------#



    # Save the plot as a PNG file
    filename = f'output/technology_{country.lower()}_grouped.png'
    print("\nGraph saved as:", filename, "\n")

    plt.savefig(filename)
    plt.show()

#plot_technology(plot_df, country, df)

#category = 'Digital Infrastructure'
#plot_df = analyze_data(df, category, country)

def plot_digital_infrastructure(grouped_data, country, data_frame):
    years = grouped_data.index
    start_year = years.min()
    end_year = years.max()

    # Extracting data for each subplot
    cellphones = grouped_data['cell_phone_total'] / 1e8  # Convert to 100 Million
    internet_users = grouped_data['internet']
    electricity_generation = grouped_data['electricity_generation'] / 1e6  # Convert to Million MWh
    
    # Creating figure and subplots
    fig, axs = plt.subplots(3, 1, figsize=(12, 8), constrained_layout=True)
    fig.suptitle(f'Digital Infrastructure Trends in {country.capitalize()} from {start_year} to {end_year}', fontsize=16)

    # Subplot 1: Number of Cellphones and Internet Users
    ax1 = axs[0]
    ax2 = ax1.twinx()
    ax1.plot(years, cellphones, marker='o', linestyle='-', color='b', label='Number of Cellphones (100 Million)')
    ax2.plot(years, internet_users, marker='o', linestyle='-', color='g', label='Internet Users')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Cellphones (100 Million)', color='b')
    ax2.set_ylabel('Internet Users', color='g')
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

    # Rick added a pivot table plot -------#

    digital_infrastructure_df_for_pivot = compare_by_cell_phone(data_frame, country)
    #print(digital_infrastructure_df_for_pivot)
    digital_infrastructure_pivot_table = digital_infrastructure_df_for_pivot.pivot_table('Cell_phone_per_capita', index='year', columns='country')
    plot_3 = axs[2]
    plot_3.set_title(' '.join(['Cell Phone per Capita', ''.join(['(', country]) , 'vs the highest and lowest in the world)']))
    plot_3.set_xlabel('Year')
    plot_3.set_ylabel('Cell Phone per Capita')
    plot_3.plot(digital_infrastructure_pivot_table, marker='o', linestyle='-')
    plot_3.set_xticks(np.arange(digital_infrastructure_df_for_pivot['year'].min(), digital_infrastructure_df_for_pivot['year'].max() + 1, 1))
    plot_3.legend(digital_infrastructure_pivot_table.columns)

    filename_pivot = f"output/{country.lower()}_digital_infrastructure_pivot.csv"

    digital_infrastructure_pivot_table.to_csv(filename_pivot)
    print(f"\nPivot table saved as '{filename_pivot}'.")

   
   
    # -------------------------------------#


    # Save the plot as a PNG file
    filename = f'output/digital_infrastructure_{country.lower()}_grouped.png'
    print("\nGraph saved as:", filename, "\n")
    plt.savefig(filename)
    plt.show()

#plot_digital_infrastructure(plot_df, country, df)