#Please run ImportCSV.py first before running this file

from ImportCSV import process_str_csv_file
from ImportCSV import process_float_csv_file

import pandas as pd

# import all csv files
print("Loading data begin....")
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

# Merge 10 csv files
print("Merging data...")
df_list = [df_inflation, df_coal_consu, df_internet, df_mincpcap, df_GDP_total, df_life_exp, df_population, df_electricity_gen, df_resi_electricity_consu, df_cell_phone]
df_final = df_list[0]

print(len(df_list))

for i in range(1, len(df_list)):
    print(".")
    df_final = pd.merge(df_final, df_list[i], left_index=True, right_on=['country', 'year'])

print("Final data size:", df_final.shape)
#print(df_final2)
print("Finished data merge.")
print("Data preview:")
print(df_final.head(3))