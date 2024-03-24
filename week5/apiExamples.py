import matplotlib.pyplot as plt
import pandas as pd
from randomuser import RandomUser

import requests
import json

r = RandomUser()


def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append(
            {
                "Name": user.get_full_name(),
                "Gender": user.get_gender(),
                "City": user.get_city(),
                "State": user.get_state(),
                "Email": user.get_email(),
                "DOB": user.get_dob(),
                "Picture": user.get_picture(),
            }
        )

    return pd.DataFrame(users)


# FruityVice API
# via requests library


data = requests.get("https://fruityvice.com/api/fruit/all")
print("this is sync")
results = json.loads(data.text)
pd.DataFrame(results)
df2 = pd.json_normalize(results)
banana = df2.loc[df2["name"] == "Banana"]
print(banana)
cals = banana.iloc[0]["nutritions.calories"]
print(cals)
