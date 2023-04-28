# %%
import pandas as pd


# %%
df = pd.read_csv('cart.csv', parse_dates=['date'])
df

# %%
df.duplicated()

# %%
# df['date', 'name']
type(df[['date', 'name']])

# %%
type(df['date'])

# %%
type(df[['date']])

# %%
df.duplicated(['date', 'name'])