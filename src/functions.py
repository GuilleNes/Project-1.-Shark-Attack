import re

# We create a function for joining all the different activities into only 7 categories.

def filter_activity (df, dict, column):
    for key, value in dict.items(): 
        df[column] = df[column].str.replace(value, key, regex = True)  
    return df.sample()


# We create a function to rename the columns
def rename_columns(df, oldcolumn, newcolumn):
    df.rename(columns={oldcolumn: newcolumn}, inplace = True, errors = "raise")
    return


# This function drops the unnused columns
def drop_columns(df, list_):
    df.drop(list_, axis = 1, inplace=True)
    return

# This function drops the rows with more than a given number of Nan
def drop_rows(df, thresh_):
    df.dropna(axis=0, inplace=True, thresh=thresh_)
    df.reset_index(drop = True)
    return

# This function is used for applying regex to the different columns of the df.
def regex_columns(df, column, patternn):
    df[column] = df[column].apply(lambda x: re.findall(patternn, str(x))).apply(lambda x: ' '.join(x))
    df[column] = df[column].explode()
    return df.sample()

# This function is used for applying regex and create a new column on the df.
def regex_new_column(df, column, new, patternn):
    df[new] = df[column].apply(lambda x: re.findall(patternn, str(x))).apply(lambda x: ' '.join(x))
    df[new] = df[new].explode() 
    return df.sample()

# With the function below we fill the empty values in one column with the existing values in other
def move_info(df, column1, column2):
    df[column1].fillna(df[column2], inplace=True)
    return 


def filter_time(df, column):
    for i in df[column]:
            i = str(i)
            if "06" in i or "07"  in i or "08" in i or "09" in i or "10" in i or "11" in i or "morning" in i or "Morning" in i or "A.M" in i or "AM" in i or "dawn" in i or "Dawn"in i:
                df[column] = df[column].replace(i, "Morning")
            elif "12" in i or "13"in i or "14"in i or "15"in i or "16"in i or "17"in i or "afternoon"in i or "lunch"in i or "noon"in i or "Noon"in i or "Midday"in i or "P.M." in i:      
                df[column] = df[column].replace(i, "Afternoon")
            elif "18"in i or "19"in i or "20"in i or "21"in i or "Sunset"in i or "dusk"in i or "Dusk"in i or "evening" in i:
                df[column] = df[column].replace(i, "Evening")
            elif "22"in i or "23"in i or "24"in i or "01"in i or "02"in i or "03"in i or "04"in i or "05"in i or "Night"in i or "night"in i:
                df[column] = df[column].replace(i, "Nightime")    
            else:
                df[column] = df[column].replace(i, "Random or not clear time references")
    return df[column].value_counts()