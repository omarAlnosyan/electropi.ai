#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

def fetch_data_from_file():
    file_name = input('Please enter the file name: ')
    try:
        if '.json' in file_name:
            return pd.read_json(file_name)
        elif any(ext in file_name for ext in ['.xlsx', '.xls']):
            return pd.read_excel(file_name)
        elif '.csv' in file_name:
            return pd.read_csv(file_name)
        else:
            print("The file name appears to be incorrect. Please check and try again.")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
    return None

def show_basic_stats(data):
    if data is not None:
        print("\n--- Basic Statistics Overview ---")
        print(f"Mean values:\n{data.mean(numeric_only=True, skipna=True)}\n")
        print(f"Median values:\n{data.median(numeric_only=True)}\n")
        print(f"Standard Deviation values:\n{data.std(numeric_only=True)}\n")
    else:
        print("No data available to show statistics.")

def eliminate_missing_values(data):
    if data is not None:
        axis = input("Would you like to eliminate missing values from rows or columns? Please type 'row' or 'column': ").lower()
        if axis in ['row', 'column']:
            axis_val = 0 if axis == 'row' else 1
            data = data.dropna(axis=axis_val)
            print("\nMissing values have been successfully eliminated.")
            return data
        else:
            print("Invalid selection. Please choose either 'row' or 'column'.")
    else:
        print("No data available for processing.")
    return data

def apply_one_hot_encoding(data):
    if data is not None:
        categorical_columns = data.select_dtypes(include=['object']).columns
        data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)
        print("\nOne-Hot Encoding has been successfully applied to all categorical columns.")
    else:
        print("No data available for encoding.")
    return data

def initiate_program():
    data = fetch_data_from_file()
    if data is None:
        print("Exiting due to lack of data.")
        return

    while True:
        print("\nSelect an operation:")
        print("1: Display the dataset")
        print("2: Eliminate Missing Values")
        print("3: Display Basic Statistics")
        print("4: Apply One-Hot Encoding")
        print("'STOP': Exit the program")
        choice = input("Your choice: ").lower()

        if choice == "1":
            print("\n--- Dataset Preview ---")
            print(data)
        elif choice == "2":
            data = eliminate_missing_values(data)
        elif choice == "3":
            show_basic_stats(data)
        elif choice == "4":
            data = apply_one_hot_encoding(data)
        elif choice == "STOP":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Sorry, that's not a valid option. Please try again.")

if __name__ == "__main__":
    initiate_program()




# In[ ]:





# In[ ]:





# In[ ]:




