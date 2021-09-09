import pandas as pd

def save(df, filename):
    writer = pd.ExcelWriter('data/'+filename)
    df.to_excel(writer, 'sheet1')
    writer.save()

jsonString = open('data/nonpay.json').read()

df_f_json = pd.read_json('data/nonpay.json')
print(df_f_json.count())

save(df_f_json, 'nonpay_e.xlsx')