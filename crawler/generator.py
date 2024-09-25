# this file is generator that read id from whc-sites and crawl its description, then write into a csv
import pandas as pd

excel = 'whc-sites-2023.xls'
df = pd.read_excel(excel)
nid = df['id_no']
name = df['name_en']
short_description = df['short_description_en']
print(short_description[0])