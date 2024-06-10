import pandas as pd
import numpy as np

# Import data from CSV file
# Change header to dtype int
# Combine header year and index country as multiindex
# Conver data to int. k to 1000, M to 1000000, B to 1000000000
# https://www.skytowner.com/explore/converting_k_and_m_to_numerical_form_in_pandas_dataframe


def process_str_csv_file (file_name, data_name):
    """age: Set a new age value for a Horse object as long as it is greater than zero. A message is printed if update is successful.
        
    Args:
            file_name (str): Name of the CSV file
            data_name (str): Category name of the data
    Returns:
            stage4 (pd dataframe): Multiindex (country (str), year (int))
    """

    fresh_data = pd.read_csv(file_name, index_col=[0], header=None)
    
    vertical_integer_col_name = fresh_data.iloc[0,1:].apply(int)
    horizontal_integer_col_name = np.reshape(vertical_integer_col_name,(1,vertical_integer_col_name.size))
    
    fresh_data_body = pd.DataFrame(fresh_data.iloc[1:,1:])
   
    stack_integer_col_and_data_body = np.vstack((horizontal_integer_col_name, fresh_data_body))

    headerless_country_by_year_data = pd.DataFrame(stack_integer_col_and_data_body, index=fresh_data.index)

    #grab row 0 as header
    new_header = headerless_country_by_year_data.iloc[0] #grab the first row for the header
    body = headerless_country_by_year_data[1:] #take the data less the header row
    body.columns = new_header.rename('year') #set the header row as the df header
    country_by_year_data = pd.DataFrame(body, index=body.index.rename('country'))


    country_year_data = pd.DataFrame(country_by_year_data.stack())
    stage1 = country_year_data.rename(columns={country_year_data.columns.values[0]:data_name})
    stage2 = pd.DataFrame(stage1, index=stage1.index.set_names(['country', 'year']))


    stage3 = stage2[data_name].replace({"k":"*1e3", "M":"*1e6", "B":"*1e9", "µ":"*1e-6", "TR":"*1e12"}, regex=True).map(pd.eval).astype(int)
    stage4 = pd.DataFrame(stage3)
    stage5 = stage4.reset_index()
    return stage4

def process_float_csv_file (file_name, data_name):
    """age: Set a new age value for a Horse object as long as it is greater than zero. A message is printed if update is successful.
        
    Args:
            file_name (str): Name of the CSV file
            data_name (str): Category name of the data
    Returns:
            stage4 (pd dataframe): Multiindex (country (str), year (int))
    """

    fresh_data = pd.read_csv(file_name, index_col=[0], header=None)
    
    vertical_integer_col_name = fresh_data.iloc[0,1:].apply(int)
    horizontal_integer_col_name = np.reshape(vertical_integer_col_name,(1,vertical_integer_col_name.size))
    
    fresh_data_body = pd.DataFrame(fresh_data.iloc[1:,1:])
   
    stack_integer_col_and_data_body = np.vstack((horizontal_integer_col_name, fresh_data_body))

    headerless_country_by_year_data = pd.DataFrame(stack_integer_col_and_data_body, index=fresh_data.index)

    #grab row 0 as header
    new_header = headerless_country_by_year_data.iloc[0] #grab the first row for the header
    body = headerless_country_by_year_data[1:] #take the data less the header row
    body.columns = new_header.rename('year') #set the header row as the df header
    country_by_year_data = pd.DataFrame(body, index=body.index.rename('country'))


    country_year_data = pd.DataFrame(country_by_year_data.stack())
    stage1 = country_year_data.rename(columns={country_year_data.columns.values[0]:data_name})
    stage2 = pd.DataFrame(stage1, index=stage1.index.set_names(['country', 'year']))


    stage3 = stage2[data_name].replace({"\U00002212":"-","k":"*1e3", "µ":"*1e-6", "M":"*1e6", "B":"*1e9"}, regex=True).map(pd.eval).astype(float)
    stage4 = pd.DataFrame(stage3)
    stage5 = stage4.reset_index()
    return stage4