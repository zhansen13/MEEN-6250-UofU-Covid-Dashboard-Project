# -*- coding:utf-8 -*-
# @Author : Bo Zhao
# @Time   : 12/1/2022 6:21 PM

import requests
from bs4 import BeautifulSoup
import json

def scrape_country(country,url,day = 'today'):

    print('Scraping...')
    '''
    request the whole website content in url
    '''
    response = requests.post(url).text
    print('Scraping finished!')
    print('--------------------')
    identity = 'main_table_countries_' + day  # id of desired contents
    soup = BeautifulSoup(response, 'html.parser')    # parsing the HTML documents using html.parser
    today = soup.find('table', attrs={'id': identity})  # extract the contents that has covid data
    data_today = today.tbody.find_all('tr')  # extract all data from 'tr' subsection

    data = [] # detailed data of all country
    for index in range(1, len(data_today)):
        r = []
        for tr in data_today[index].find_all('td'):
            r.append(tr.text.replace('\n', '').strip())
        data.append(r)
    data = data[7:]

    head = today.thead.find_all('th') # find all the header of the table
    header = []
    for i in head:
        header.append(i.text.replace('\n', '').strip())
    '''
    use table header as key and detailed covid data as value to creat a dictionary for each country
    put every dictionary into a list
    '''
    data_dic_all = []
    for i in data:
        data_dic = {}
        for j in range(len(header)):
            data_dic[header[j]] = i[j]
        data_dic_all.append(data_dic)
    '''
    find out the data of the input country
    print out the raw data and normalized data 
    '''
    total_num = 0
    total_num_relative = 0
    country_name = ''
    country_data = {}
    for i in data_dic_all:
        if i['Country,Other'].upper().replace(' ','').strip() == country.upper().replace(' ','').strip():
            total_num = i['TotalCases']
            country_name = i['Country,Other']
            total_num_relative = i['Tot Cases/1M pop']
            country_data = i

    del country_data['#']
    print(country_name,':')
    print('Total Cases:',total_num)
    print('Total Cases / 1M Population:',total_num_relative)
    '''
    save the jason file
    '''
    if day == 'today':
        with open('today.json','w') as f:
            f.write(json.dumps(data_dic_all))
    if day == 'yesterday':
        with open('yesterday.json','w') as f:
            f.write(json.dumps(data_dic_all))
    if day == 'yesterday2':
        with open('two_days_ago.json','w') as f:
            f.write(json.dumps(data_dic_all))
    '''return a dictionary of input country'''
    return country_data

if __name__ == '__main__':
    url = 'https://www.worldometers.info/coronavirus/'
    country = 'Turkey'
    day = 'today'  # valid inputs of day: 'today'(default)/ 'yesterday'/ 'yesterday2'
    data = scrape_country(country, url, day)
    print(data)
