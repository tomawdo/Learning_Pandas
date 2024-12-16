import pandas as pd

colonna = ["Maria", "Ana", "Mark"]
titolo_colonne = {"Nome": colonna,
                  "Altezza": [167, 197, 182],
                  "Peso": [54, 100, 80]}
data = pd.DataFrame(titolo_colonne)

i_mass_corp = [] # peso / (altezza ** 2)
for i in range(len(data)):
    imc = data["Peso"][i] / (data["Altezza"][i] ** 2)
    i_mass_corp.append(imc)

data["IMC"] = i_mass_corp

#salvataggio dati su file
data.to_csv("imc.csv", float_format="%.5f", index=False)



print(data)
