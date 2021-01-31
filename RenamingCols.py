import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

print(ufo.columns)

# lets rename Colors reported and Shape Reported

ufo.rename(columns={'Colors Reported': 'Colors_Reported', 'Shape Reported': 'Shape_Reported'}, inplace=True)
print(ufo.columns)

# If renaming all columns

ufo_cols = ['city', 'colors reports', 'shape reported', 'state', 'time']

ufo.columns = ufo_cols
print(ufo.columns)

df = pd.read_csv('http://bit.ly/uforeports', names=ufo_cols, header=0)  # rename as reading in file
print(df.columns)

# using replace method

df1 = pd.read_csv('http://bit.ly/uforeports')
df1.columns = df1.columns.str.replace(' ', '-')
print(df1.columns)
