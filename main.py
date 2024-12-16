import pandas as pd

data = {
    "name": ["Alice", "Maria", "Mark", "David"],
    "age": [25, 30, 35, 40],
    "gender": ["F", "F", "M", "M"]
}

df = pd.DataFrame(data)
print(df)