import pandas as pd
import os

from datetime import datetime
from datetime import timedelta

# Function to load CSV files into a dictionary of DataFrames
def load_data_to_dict(folder_path):
    main_withing_df = pd.DataFrame()
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            # Extract person's name from the filename
            person_name = filename.replace('.csv', '')
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            df['Person'] = person_name
            # Store DataFrame in dictionary with person's name as key
            main_withing_df = pd.concat([main_withing_df, df], ignore_index=True)
    return main_withing_df


#Required functions
def count_elements(list_string):
    # Split the string on commas and count the number of elements
    count = len(list_string.strip("[]").split(","))
    return count

def separate_elements(list_string):
    # Split the string on commas and count the number of elements
    list = list_string.strip("[]").split(",")
    return list



# Function to create a time range for each entry
def create_time_range(start, end, date, person, manual_value):
    # Convert start and end times to datetime objects with the correct date
    start_time = datetime.combine(date, start)
    end_time = datetime.combine(date, end)
    
    # Handle cases where the end time might be after midnight
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    # Generate timestamps every second between start and end times
    timestamps = pd.date_range(start=start_time, end=end_time, freq='S')
    
    # Create a DataFrame for this range
    df_range = pd.DataFrame({'Datetime': timestamps})
    df_range['Manual Value'] = manual_value
    df_range['Person'] = person
    
    return df_range