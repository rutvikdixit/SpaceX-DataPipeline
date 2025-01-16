import requests
import pandas as pd

#sample dataframe
data = {
    'rocket': [
        'F1',
        'F2',
        'Voyager'
    ],
    'launches': [5, 10, 11]
}

df = pd.DataFrame(data)
print(df)

#adding columns
df['success_rate'] = [0.1, 0.22, 0.35]

print(df)

#filtering dataframe by launch count
print(df[df['launches'] > 8])