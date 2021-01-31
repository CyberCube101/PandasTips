import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

# iLoc specifies rows and columns by integer position. iLoc works like range(0,4) ie ignores 4

print(ufo.iloc[:, [0, 3]])  # all rows and columns 0 and 3

print(ufo.columns)

# for i in range(len(ufo)):
#     print(ufo.iloc[i, 0])







