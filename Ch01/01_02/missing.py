

# %%
import pandas as pd

# %%
df = pd.read_csv('cart.csv')
df.dtypes

# %%
df

# %%
df = pd.read_csv('cart.csv', parse_dates=['date'])
df.dtypes

# %%
df

# %%
df['amount'] = df['amount'].astype('Int32')
df.dtypes

# %%
df

# %%
df.isnull()

# %%
df.isnull().any(axis=1)

# %%
df.isnull().any()

# %%
