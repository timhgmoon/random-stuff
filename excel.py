import pandas as pd

excel_file = './our_predictions2.csv'

data = pd.read_csv(excel_file, usecols=['property_address'])
my_list = []
for i in data.values:
    my_list.append([s.replace('  ', ' ') for s in i])
new_list = []
for i in my_list:
    new_list.append(i[0])
df = pd.DataFrame()
df['property_address'] = new_list
df.to_csv('out.csv')
