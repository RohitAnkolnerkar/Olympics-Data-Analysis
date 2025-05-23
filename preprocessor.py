import pandas as pd
o=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Desktop\\athlete_events.csv")
p=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Desktop\\noc_regions.csv")
def preprocess():
    global o,p
    o=o[o['Season']=='Summer']
    o = o.merge(p, on='NOC', how='left')
    o.drop_duplicates(inplace=True)
    o = pd.concat([o, pd.get_dummies(o['Medal'])], axis=1)
    o = o.replace(False, 0)
    o = o.replace(True, 1)

    return o


