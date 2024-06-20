# ENSF 692 Spring 2024 - Group Project

# Group members: Bo Zheng Ma, Rick Zhang, Warisa Khaophong 


## Outline:
* Design and document a terminal-based Python application
* Select, import, and manipulate a set of data
* Merge multiple datasets using Pandas
* Use hierarchical indexing to sort and slice data
* Process data according to user input
* Operate on data in Pandas and NumPy
* Display data using Matplotlib


## Goal:
* Our goal with this project is to create a program that imports datasets containing information of global socio-economic and technological data. We want to present the user a way of seeing such trends within select countries and allow them to perform insightful analysis.


## Selected datasets:
* Number of Cellphones 
* Total Coal Consumption 
* ELectricity generated 
* Inflation annual percent 
* Daily income ($ earned/person on a daily basis)
* Life expentancy
* Net internet users
* Population
* Residential electricity use
* Total GDP USA (Inflation adjusted)

## How to run the program:
* Clone the repository onto your local machine
* Ensure that python along with pandas and matploblib are installed properly.
    * Change working directory to ensf-692-project-super-awesometeam
    * python 692Project.py

## Input:
* The program will process datasets from 'src' folder

## Output:
* Merged dataframe containing the 10 datasets will be inside /output/df_merged.csv
* Merged dataframe with additionally added columns will be inside /output/df_export.csv
* Pivot tables of the selected country and topic will be in /output/
* Plots of the selected country and topic will be in /output/

## Documentation/Report:
* The report is located in this repository along with the powerpoint presentation.