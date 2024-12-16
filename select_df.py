import pandas as pd

data = pd.read_csv("data_season.csv", sep=",")

# first5rows = data.head(5) # seleziono le prime 5 righe
# last5rows = data.tail(5) # seleziono le ultime 5 righe

filtro = data[data["Location"] == "Reano"]
replace_location = data.replace("Mangalore", "Reano")

#remove_col = data.drop("Year", axis=1)

print(replace_location)