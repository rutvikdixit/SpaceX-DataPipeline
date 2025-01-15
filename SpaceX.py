import requests
import pandas as pd

print("Hello World!")

#Initialize variables
num_launches = 0
rocket_name = "Voyager"
success_rate = 0.5

print(success_rate, rocket_name)

response = requests.get('https://api.spacexdata.com/v4/launches')
launch_data = response.json()

df = pd.DataFrame(launch_data)

print(df.head())

print(launch_data)