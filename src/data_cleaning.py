import pandas as pd
import re
import functions as fun

attacks = pd.read_csv("data/attacks.csv", encoding= 'unicode_escape')

# First we rename some of the columns, as the names have spaces on them 

fun.rename_columns(attacks, "Species ", "Species")
fun.rename_columns(attacks, "Sex ", "Sex")

# Next, we drop some of the columns we are not going to use and the rows with many Nan or useless values

fun.drop_columns(attacks, ["Unnamed: 22", "Unnamed: 23", "original order", "href formula", "href", "Case Number.1","Case Number.2", "pdf", "Case Number", "Species", "Name", "Age", "Injury", "Location"])
fun.drop_rows(attacks, 9)
fun.move_info(attacks, "Year", "Date")

# We are going to clean the values in the columns in order to get them in more readable format

attacks["Year"] = [str(i).split(".")[0] for i in attacks["Year"]]

"""From here, we are doing regex on the different columns in order to have the most cleared data

The percentage between "Nan" values and total number of rows, justify the cleaning process we have been doing before. From this dataframe we are able to establish hypothesis without loosing much value information during the cleaning.

We start to clean the Date column, transforming it into Year and Month We are going to clean the Date and Year columns, trying to clear the info and extracting the most usefull one First we create another column called NewYear with the str values of the column Year."""

fun.regex_columns(attacks, "Year", "^\d{4}")
fun.regex_new_column(attacks, "Date", "Month", "([a-z|A-Z]{3})" )
fun.regex_columns(attacks, "Month", "(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)*$")
fun.drop_columns(attacks, "Date")

activities = {
                         "Swimming related": ".*(swim).*|.*(Swim).*",
                         "Board involved activity": ".*(Surf).*|.*(surf).*|.*(Board).*|.*(board).*|.*(Pad).*|.*(pad).*|.*(Kay).*|.*(Canoe).*",
                         "Fishing related": ".*(fish).*|(Fish).*|.*(Kill).*|.*(Pull).*|.*(Pick).*|.*(feed).*",
                         "Beach activities":".*(Wad).*|.*(Bath).*|.*(bath).*|.*(Stans).*|.*(Play).*|.*(play).*|.*(Walk).*|.*(walk).*",
                         "Diving activities": ".*(Div).*|.*(div).*|.*(underw).*|.*(Snork).*",
                         "Consequence of a shipwreck": ".*(dinghy).*|.*(collide).*|.*(lifeboat).*|.*(explodex).*|.*(skiff).*|.*(sink).*|.*(sank).*",
                         "Consequence of handeling sharks": ".*(Shark).*|.*(shark).*",
}     
fun.filter_activity(attacks, activities, "Activity")
fun.filter_time(attacks, "Time")
fun.regex_new_column(attacks, "Fatal (Y/N)", "Fatal", "^(N|Y)")
fun.drop_columns(attacks, "Fatal (Y/N)")
fun.regex_columns(attacks, "Sex", "^(F|M)")

attacks.to_csv("data/attacks_cleaned.csv", index=False)