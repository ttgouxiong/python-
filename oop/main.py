import pandas as pd
import openpyxl

df = pd.read_csv('D:\\python_learn\\deal_with_CSV\\1.csv')
print(df['ads'])
df['ads'] = '=HYPERLINK("' + df['ads'] + '")'
t = list(df['ads'])
print(df['ads'])



df.to_excel('new.xlsx', index=False)



