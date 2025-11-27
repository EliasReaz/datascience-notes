import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

import matplotlib.pyplot as plt
import plotly.express as px

np.random.seed(42)
 
data = np.random.exponential(scale=20, size=1000)
px.histogram(data, nbins=50).show()

df = pd.DataFrame({'sales': data})
df['sales_log'] = np.log1p(df['sales'])
px.histogram(df, x='sales_log', nbins=50).show()

# --- 2) Quantile-based binning (low/med/high) ---
df['quantile_group'] = pd.qcut(df['sales'], q=3, labels=['Low','Medium','High'])
df['quantile_group_numeric'] = df['quantile_group'].map({'Low':0, 'Medium':1, 'High':2})
px.histogram(df, x='sales', color='quantile_group', nbins=50, title='Quantile-based Binning').show()

# --- 3) K-Means on raw data ---
kmeans_raw = KMeans(n_clusters=3, random_state=42, n_init=10)
df['kmeans_raw'] = kmeans_raw.fit_predict(df[['sales']])

# --- 4) K-Means on log-transformed data ---
log_sales = np.log1p(df['sales'])  # log(1+x)
kmeans_log = KMeans(n_clusters=3, random_state=42, n_init=10)
df['kmeans_log'] = kmeans_log.fit_predict(log_sales.to_numpy().reshape(-1,1))

# --- 5) Plot comparison ---
fig, axes = plt.subplots(1, 4, figsize=(15,4))

axes[0].hist(df['sales'], bins=30, color='gray')
axes[0].set_title('Sales Distribution (Right-skewed)')

axes[1].scatter(df.index, df['sales'], c=df['kmeans_raw'], cmap='viridis')
axes[1].set_title('K-Means on Raw Sales')

axes[2].scatter(df.index, df['sales'], c=df['kmeans_log'], cmap='viridis')
axes[2].set_title('K-Means on Log(Sales)')

axes[3].scatter(df.index, df['sales'], c=df['quantile_group_numeric'], cmap='viridis')
axes[3].set_title('qcut on sales')

plt.tight_layout()
plt.show()

###BOX PLOTS using Plotly
# =========================

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px

# --- 1) Simulate right-skewed sales data ---
np.random.seed(42)
sales = np.random.exponential(scale=1000, size=200)
df = pd.DataFrame({'sales': sales})

# --- 2) Quantile-based binning ---
df['qcut_group'] = pd.qcut(df['sales'], q=3, labels=['Low','Medium','High'])

# --- 3) K-Means raw ---
kmeans_raw = KMeans(n_clusters=3, random_state=42, n_init=10)
df['kmeans_raw'] = kmeans_raw.fit_predict(df[['sales']])

# --- 4) K-Means log-transformed ---
log_sales = np.log1p(df['sales'])
kmeans_log = KMeans(n_clusters=3, random_state=42, n_init=10)
df['kmeans_log'] = kmeans_log.fit_predict(log_sales.to_numpy().reshape(-1,1))

# --- 5) Melt dataframe for Plotly ---
df_melt = df.melt(value_vars=['sales'], id_vars=['qcut_group','kmeans_raw','kmeans_log'],
                  var_name='metric', value_name='sales_value')

# --- 6) Plotly box plots ---
fig = px.box(df, 
             y='sales', 
             x='qcut_group',
             color='qcut_group',
             points='all', 
             title='Quantile Binning (qcut)')

fig2 = px.box(df, 
              y='sales', 
              x='kmeans_raw', 
              color='kmeans_raw',
              points='all', 
              title='K-Means on Raw Sales')

fig3 = px.box(df, 
              y='sales', 
              x='kmeans_log', 
              color='kmeans_log',
              points='all', 
              title='K-Means on Log-Transformed Sales')

# Show plots
fig.show()
fig2.show()
fig3.show()

# ========================
# Let’s make a single interactive Plotly figure 
# with 3 side-by-side box plots for easy comparison:
# ========================
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# --- 1) Simulate right-skewed sales data ---
np.random.seed(42)
sales = np.random.exponential(scale=1000, size=200)
df = pd.DataFrame({'sales': sales})

# --- 2) Quantile-based binning ---
df['qcut_group'] = pd.qcut(df['sales'], q=3, labels=['Low','Medium','High'])

# --- 3) K-Means raw ---
kmeans_raw = KMeans(n_clusters=3, random_state=42, n_init=10)
df['kmeans_raw'] = kmeans_raw.fit_predict(df[['sales']])

# --- 4) K-Means log-transformed ---
log_sales = np.log1p(df['sales'])
kmeans_log = KMeans(n_clusters=3, random_state=42, n_init=10)
df['kmeans_log'] = kmeans_log.fit_predict(log_sales.to_numpy().reshape(-1,1))

# --- 5) Create subplots ---
fig = make_subplots(rows=1, cols=3, subplot_titles=('Quantile Binning (qcut)',
                                                    'K-Means Raw Sales',
                                                    'K-Means Log-Transformed'))

# Quantile Binning box plot
for grp in df['qcut_group'].unique():
    fig.add_trace(go.Box(y=df[df['qcut_group']==grp]['sales'],
                         name=str(grp),
                         boxpoints='all',
                         jitter=0.5,
                         marker_color='blue'),
                  row=1, col=1)

# K-Means Raw box plot
for grp in sorted(df['kmeans_raw'].unique()):
    fig.add_trace(go.Box(y=df[df['kmeans_raw']==grp]['sales'],
                         name=f'Cluster {grp}',
                         boxpoints='all',
                         jitter=0.5,
                         marker_color='green'),
                  row=1, col=2)

# K-Means Log box plot
for grp in sorted(df['kmeans_log'].unique()):
    fig.add_trace(go.Box(y=df[df['kmeans_log']==grp]['sales'],
                         name=f'Cluster {grp}',
                         boxpoints='all',
                         jitter=0.5,
                         marker_color='red'),
                  row=1, col=3)

# Layout
fig.update_layout(height=500, width=1200, showlegend=False, title_text="Comparison of Clustering Methods")
fig.show()

