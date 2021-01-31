import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

#### row selection

# loc is used to select by label - ufo.loc[r,c]. It is inclusive on both sides when using :

# print(ufo.loc[0, :])  # row 0 and all columns
# print(ufo.loc[0:2, :])  # rows 0,1,2 with ALL columns
# print(ufo.loc[0:2])  # same as above

### column selection


# print(ufo.loc[0:2, ['City', 'State']])  # all rows, columns=City and State

###  Boolean Conditions - Say all rows where City=Oakland

print(ufo.loc[ufo.City == 'Oakland', 'State'])  # Filter for City = Oakland, return the State
