import pandas as pd
df_2018 = pd.read_csv('data/daily_sales_data_0.csv',engine ='python')
df_2019 = pd.read_csv('data/daily_sales_data_1.csv',engine ='python')
df_2020 = pd.read_csv('data/daily_sales_data_2.csv',engine ='python')

df_all = pd.concat([df_2018, df_2019, df_2020])
df_pink_morsel = df_all[df_all['product'] == 'pink morsel']


price_num = (
	df_pink_morsel['price']
	.astype(str)
	.str.replace(r"[\$,]", "", regex=True)
	.astype(float)
)

df_pink_morsel_sales = (
	df_pink_morsel
	.assign(sales=df_pink_morsel['quantity'] * price_num)
	.loc[:, ['date', 'sales', 'region']]
)

df_pink_morsel_sales.to_csv('data/pink_morsel_sales_data.csv', index=False)