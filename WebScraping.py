import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
headers = {"User-Agent":"mozilla/5.0"}
page = requests.get(url, headers =headers)

content = BeautifulSoup(page.text,'html.parser')
table =content.find('table')
table =content.find('table', class_ = 'wikitable sortable') # finding the table with class "wikitable sortable"
columns = table.find_all('th') # selecling the column of the table finding all 'th' from "wikitable sortable
columns_text = [text.text.strip() for text in columns] # converting the raw exported data to text format and *strip()* to remove any unnecessey spaces

import pandas as pd 

df = pd.DataFrame(columns = columns_text)

rows = table.find_all('tr') # Code to find the row data
all_data = []
for data in rows[1:]:                # running loop to collect the data and append it in the empty list all_data[]
    row_data = data.find_all("td")
    row_data_text = [text.text.strip() for text in row_data]
    if len(row_data_text)==len(columns_text):
        all_data.append(row_data_text)

df = pd.DataFrame(all_data,columns = columns_text) # making the table by matching the row and column length
df.to_csv(r'C:\Users\user\Desktop\python Practise\New folder\companies.csv') #importing the data to my system in .CSV format.
