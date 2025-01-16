# .head()     : Affiche le debut du DataFrame (5 premiere lignes)
# .tail()     : Affiche la fin DataFrame (5 dernieres lignes)
# .describe() : Statistique Rapides
# .dropna()   : Eliminer les lignes aux donnees resetitions
# .groupby()["column"] : Analyse par groupe
# .shape()    : (linge number, column number)
# .loc[row_index_num_name, column_index_num_name]
# .iloc[row_index_just_num, column_index_just_num]
# df["column"].value_counts() : Compter les repetitions : عد التكرارات

import pandas as pd
import numpy as np

data = {
    'ID': [1, 2, 3, 4, 5],
    'Want': ['Yes', 'No', 'Yes', 'Yes', 'No'],
    'Nom': ['Said', 'Khalid', 'Sara', 'Mohamed', 'Khadija'],
    'Age': [18, 19, 17, 20, 16],
    'Taille': [1.85, 1.75, 1.65, 1.6, 1.7]    
}
df = pd.DataFrame(data = data)
df1 = df

df.set_index('ID')
df.shape
df.loc[1:4, ['Nom']]
df.iloc[3:5, :2]
df.loc[:5, ['Age']].sort_values('Age')
df['Note'] = [10, np.nan, 4, 6, np.nan]
df.insert(df.columns.get_loc('H'), column = 'H', value = ['#', '##', '#', '###', '#####'])
df.drop("H", axis = 1, inplace = True)
df[df['Note'].isnull()]
df.dropna(inplace = True) # Delete nan data
df = pd.concat([df, df1], axis = 1, ignore_index = True) # df + df1
df.to_csv("./data.csv", index = False) # Save
df['Age'].value_counts().plot.bar()
df.groupby(['Want'])