#!/usr/bin/env python
# coding: utf-8

# **Today we focus on a **WEBSCRAPPING PROJECT**
# **We will mainly turn our focus to jumia(online trading and marketing enterprise)focusing on the stores grocery segment**
# 

# **we will start ny importing all the necessary libraries**

# In[ ]:


import csv
import requests
from bs4 import BeautifulSoup
import time
# we will then load the url from the browser we are using
url = 'https://www.jumia.co.ke/groceries/'


# we will need to create a new dataset this will act as a 'store' for all the set of values extracted

# In[ ]:


header = ['Product', 'Price']
products = []


# we will later execute the code as it is 
# in the last line you may have queries as to how i arrived at that;
# At the value you meant to extract highlight it and right click and press "inspect" this will open for you
# a new page with a html code all you need is to copy and paste, whether its a 'div'or a 'h1'.Then input the class.
# make sure at the end of the class, there is an underscore ,reason being 'class'alone will bring about a different interpretation

# In[ ]:


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
product_list = soup.find_all('div', class_='itm col')


# we will need to loop the different values in the webpage and later we shall
# append all the data to the 'products'file we created earlier

# we will also obtain the values of name and price using the same technique explained above

# In[ ]:


for product in product_list:
    name = product.find('div', class_='name').text
    price = product.find('div', class_='prc').text.strip()
    products.append([name, price])


# The code below will create an excel file in your pc that will contain all the values from the 'jumia webpage'

# In[ ]:


with open('jumiawebpagescrapping.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(products)


# This will load the already saved excel file in your pc in the jupyter notebook

# In[ ]:


import pandas as pd
df =pd.read_csv(r'C:\Users\stilinski\jumiawebpagescrapping.csv')
print(df)


# Next we need to create a function that webs all the data and all the previous information
# Then we create a while loop that will execute the 'with open [command]'every duration of time that you set it to
# Remeber time is always in seconds

# In[ ]:


def check_price():
    url = 'https://www.jumia.co.ke/groceries/'

    header = ['Product', 'Price']
    products = []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    product_list = soup.find_all('div', class_='itm col')

    for product in product_list:
        name = product.find('div', class_='name').text
        price = product.find('div', class_='prc').text.strip()
        products.append([name, price])

    with open('writes.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(products)


# In[23]:


while(True):
    check_price()
    time.sleep(6)


# we will need to print the file again and it will keep updating itself after every duration of time you set earlier

# In[ ]:


import pandas as pd
df = pd.read_csv(r'C:\Users\stilinski\writes.csv')
print(df)

