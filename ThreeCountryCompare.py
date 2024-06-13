from ImportCSV import process_str_csv_file
from ImportCSV import process_float_csv_file
import matplotlib.pyplot as plt

import pandas as pd

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

country = 'China'
df = pd.read_csv('df_final.csv')
df = add_columns(df)



def compare_by_GDP(data_frame, country):
    df_gdp_per_capita = pd.DataFrame(data_frame['GDP_per_capita'].groupby(df['country']).mean())
    max_value = df_gdp_per_capita.max().values[0]
    min_value = df_gdp_per_capita.min().values[0]
    df_mean = df_gdp_per_capita.reset_index()
    country_max = df_mean['country'][df_mean['GDP_per_capita'] == max_value].values[0]
    country_min = df_mean['country'][df_mean['GDP_per_capita'] == min_value].values[0]
    #print("Max GDP", country_max, max_value)
    #print("Min GDP", country_min, min_value)
    #print(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(z['country'] == country_max) | (z['country'] == country_min) | (z['country'] == 'China')])
    compare_by_GDP_table = pd.DataFrame(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(data_frame['country'] == country_max) | (data_frame['country'] == country_min) | (data_frame['country'] == 'China')])
    
    return compare_by_GDP_table.reset_index()

def compare_by_internet(data_frame, country):
    df_gdp_per_capita = pd.DataFrame(data_frame['Internet_Penetration_Rate'].groupby(df['country']).mean())
    max_value = df_gdp_per_capita.max().values[0]
    min_value = df_gdp_per_capita.min().values[0]
    df_mean = df_gdp_per_capita.reset_index()
    country_max = df_mean['country'][df_mean['Internet_Penetration_Rate'] == max_value].values[0]
    country_min = df_mean['country'][df_mean['Internet_Penetration_Rate'] == min_value].values[0]
    #print("Max Internet", country_max, max_value)
    #print("Min Internet", country_min, min_value)
    #print(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(z['country'] == country_max) | (z['country'] == country_min) | (z['country'] == 'China')])
    compare_by_internet_table = pd.DataFrame(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(data_frame['country'] == country_max) | (data_frame['country'] == country_min) | (data_frame['country'] == 'China')])
    
    return compare_by_internet_table.reset_index()

def compare_by_life_exp(data_frame, country):
    df_gdp_per_capita = pd.DataFrame(data_frame['life_exp_year'].groupby(df['country']).mean())
    max_value = df_gdp_per_capita.max().values[0]
    min_value = df_gdp_per_capita.min().values[0]
    df_mean = df_gdp_per_capita.reset_index()
    country_max = df_mean['country'][df_mean['life_exp_year'] == max_value].values[0]
    country_min = df_mean['country'][df_mean['life_exp_year'] == min_value].values[0]
    #print("Max Internet", country_max, max_value)
    #print("Min Internet", country_min, min_value)
    #print(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(z['country'] == country_max) | (z['country'] == country_min) | (z['country'] == 'China')])
    compare_by_life_exp_table = pd.DataFrame(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(data_frame['country'] == country_max) | (data_frame['country'] == country_min) | (data_frame['country'] == 'China')])
    
    return compare_by_life_exp_table.reset_index()

#w = compare_by_GDP(df, country)
#w = compare_by_internet(df, country)
def plot_life_exp_tri():
    w = compare_by_life_exp(df, country)
    #print(w)
    #w.pivot_table('life_exp_year', index='year', columns='country', aggfunc='sum')
    d = w.pivot_table('life_exp_year', index='year', columns='country')
    print(d)
    a = d.plot()
    plt.ylabel('Life Expetancy')
    plt.show()

def plot_gdp_tri():
    w = compare_by_GDP(df, country)
    #print(w)
    #w.pivot_table('life_exp_year', index='year', columns='country', aggfunc='sum')
    d = w.pivot_table('GDP_per_capita', index='year', columns='country')
    print(d)
    a = d.plot()
    plt.ylabel('GDP per capita')
    plt.show()

def plot_internet_tri():
    w = compare_by_internet(df, country)
    #print(w)
    #w.pivot_table('life_exp_year', index='year', columns='country', aggfunc='sum')
    d = w.pivot_table('Internet_Penetration_Rate', index='year', columns='country')
    print(d)
    a = d.plot()
    plt.ylabel('Internet Penetration Rate%')
    plt.show()

#plot_life_exp_tri()
#plot_gdp_tri()
plot_internet_tri()
