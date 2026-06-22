import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("economic-survey-of-manufacturing-march-2026-quarter.csv")
df['Data_value'] = pd.to_numeric(df['Data_value'], errors='coerce')
df = df.dropna(subset=['Data_value'])

def convert_to_quarter(val):
    month = str(f"{val:.2f}").split('.')[1]
    q_map = {'03': 'Q1', '06': 'Q2', '09': 'Q3', '12': 'Q4'}
    return f"{int(val)}-{q_map.get(month, 'Q4')}"

df['Quarter'] = df['Period'].apply(convert_to_quarter)
df['Datetime'] = pd.to_datetime(df['Period'].astype(str).str.replace(r'\.(\d+)', lambda m: f"-{int(m.group(1)):02d}-01", regex=True))
# Filter for current market prices and reshape variables 
filtered_df = df[df['Series_title_3'] == 'Current prices']
pivot_df = filtered_df.pivot_table(
    index=['Datetime', 'Quarter', 'Series_title_1'], 
    columns='Series_title_2', 
    values='Data_value', 
    aggfunc='sum'
).reset_index()

# column names 
pivot_df.rename(columns={
    'Sales (operating income)': 'Sales',
    'Stocks of finished goods, trading goods and work in progress': 'Stocks'
}, inplace=True)

# Filter for current market prices and reshape variables
filtered_df = df[df['Series_title_3'] == 'Current prices']
pivot_df = filtered_df.pivot_table(
    index=['Datetime', 'Quarter', 'Series_title_1'], 
    columns='Series_title_2', 
    values='Data_value', 
    aggfunc='sum'
).reset_index()

# Simplify column names 
pivot_df.rename(columns={
    'Sales (operating income)': 'Sales',
    'Stocks of finished goods, trading goods and work in progress': 'Stocks'
}, inplace=True)

# new economic health ratio from raw metrics
pivot_df['Inventory_to_Sales_Ratio'] = pivot_df['Stocks'] / pivot_df['Sales']

# Filter for macro-trends 
target_df = pivot_df[pivot_df['Series_title_1'] == "All manufacturing"].sort_values('Datetime')

# Plot 
fig = go.Figure()
fig.add_trace(go.Bar(x=target_df['Quarter'], y=target_df['Sales'], name='Quarterly Sales ($M)'))
fig.add_trace(go.Scatter(x=target_df['Quarter'], y=target_df['Inventory_to_Sales_Ratio'], name='Risk Ratio', yaxis='y2'))

# layout 
fig.update_layout(
    title="Manufacturing Economic Profile",
    yaxis=dict(title="Sales Volume ($ Millions)"),
    yaxis2=dict(title="Supply Chain Risk Ratio", overlaying='y', side='right'),
    template='plotly_white'
)
fig.show()