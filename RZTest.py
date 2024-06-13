from ImportCSV import process_str_csv_file
from ImportCSV import process_float_csv_file

import pandas as pd

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
    print("Max GDP", country_max, max_value)
    print("Min GDP", country_min, min_value)
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
    print("Max Internet", country_max, max_value)
    print("Min Internet", country_min, min_value)
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
    print("Max Internet", country_max, max_value)
    print("Min Internet", country_min, min_value)
    #print(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(z['country'] == country_max) | (z['country'] == country_min) | (z['country'] == 'China')])
    compare_by_life_exp_table = pd.DataFrame(data_frame[['country', 'year','GDP_per_capita','Internet_Penetration_Rate', 'life_exp_year']][(data_frame['country'] == country_max) | (data_frame['country'] == country_min) | (data_frame['country'] == 'China')])
    
    return compare_by_life_exp_table.reset_index()

#w = compare_by_GDP(df, country)
#w = compare_by_internet(df, country)
w = compare_by_life_exp(df, country)
print(w)


'''
print("Loding data begin....")
print("1. Loading inflation data...")
df_inflation = process_float_csv_file("inflation_annual_percent.csv", "inflation_percent")
print(df_inflation.size, "values imported successfully...")

print("2. Loading mincpcap data...")
df_mincpcap = process_float_csv_file("mincpcap_cppp.csv", "mincacap")
print(df_mincpcap.size, "values imported successfully...")

print("3. Loading internet user data...")
df_internet = process_str_csv_file("net_users_num.csv", "internet")
print(df_internet.size, "values imported successfully...")

print("4. Loading coal consumption data...")
df_coal_consu = process_str_csv_file("coal_consumption_total.csv", "coal")
print(df_coal_consu.size, "values imported successfully...")

print("5. Loading total GDP data...")
df_GDP_total = process_str_csv_file("total_gdp_us_inflation_adjusted.csv", "GDP_USD_Total")
print(df_GDP_total.size, "values imported successfully...")

print("6. Loading life expectancy data...")
df_life_exp = process_float_csv_file("lex.csv", "life_exp_year")
print(df_life_exp.size, "values imported successfully...")

print("7. Loading population data...")
df_population = process_str_csv_file("pop.csv", "polulation")
print(df_population.size, "values imported successfully...")

print("8. Loading electricity generation data...")
df_electricity_gen = process_str_csv_file("electricity_generation_total.csv", "electricity_generation")
print(df_electricity_gen.size, "values imported successfully...")

print("9. Loading electricity consumption data...")
df_resi_electricity_consu = process_str_csv_file("residential_electricity_use_total.csv", "residential_electricity_use")
print(df_resi_electricity_consu.size, "values imported successfully...")

print("10. Loading cell phone user data...")
df_cell_phone = process_str_csv_file("cell_phones_total.csv", "cell_phone_total")
print(df_cell_phone.size, "values imported successfully...")

print("Finished data import.")
'''
'''
df_final = pd.merge(df_inflation, df_mincpcap, left_index=True, right_on=['country', 'year'])
print(df_final.size)

df_final = pd.merge(df_final, df_internet, left_index=True, right_on=['country', 'year'])
print(df_final.size)

df_final = pd.merge(df_final, df_coal_consu, left_index=True, right_on=['country', 'year'])
print(df_final.size)
#print(df_final)
'''
'''
print("Merging data...")
df_list = [df_inflation, df_coal_consu, df_internet, df_mincpcap, df_GDP_total, df_life_exp, df_population, df_electricity_gen, df_resi_electricity_consu, df_cell_phone]
df_final2 = df_list[0]

print(len(df_list))

for i in range(1, len(df_list)):
    print(".")
    df_final2 = pd.merge(df_final2, df_list[i], left_index=True, right_on=['country', 'year'])

print("Final data size:", df_final2.shape)
#print(df_final2)
print("Finished data merge.")
print("Data preview:")
print(df_final2.head(3))


#def_demo_3 = pd.merge(def_demo, def_demo_2, left_index=True, right_on=['country', 'year'])

#print(def_demo_3.head(10))

#print(def_demo_3.loc['UAE'])
'''
'''
infla = pd.read_csv("inflation_annual_percent.csv", index_col=[0])
print(infla.loc['Zimbabwe','1990'])

a = infla.loc['Zimbabwe','1990']
#print(float(a))
print(float('-0.92'))
print(type(a))
print(a.replace('−', '+'))
print(a.replace('\U00002212', '-'))
print(float(a.replace('\U00002212', '-')))
b = float(a.replace('\U00002212', '-'))
print(type(b))
'''

