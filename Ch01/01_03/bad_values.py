# %%
import pandas as pd

# %%
df = pd.read_csv('metrics.csv', parse_dates=['time'])
df.sample(10)

# %%
df.groupby('name').describe()

# %%
df['name'].value_counts()

# %%
pd.pivot(df, index='time', columns='name')

# %%
pd.pivot(df, index='time', columns='name').plot(subplots=True)

# %%
df.query('name == "cpu" & (value < 0 | value > 100)')

# %%
mem = df[df['name'] == 'mem']
mem.head()

# %% 
mem = df[df['name'] == 'mem'][['time','value']]
mem.head()


# %%
# Actually a Series:
mem2 = df[df['name'] == 'mem'][['value']]
mem2.head()



# %%
mem = df[df['name'] == 'mem']['value']
mem.head()


# %%
z_score = (mem - mem.mean())/mem.std()
z_score

# %%
bad_mem = mem[z_score.abs() > 2]
bad_mem

# %%
# bad_mem
df.loc[bad_mem.index]

# %%
