#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri May 29 15:48:34 2020

@author: shauangel
"""
import time
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select

title = ['year', 'month', 'name', 'temperature', 'humidity']
web = webdriver.Chrome('/Users/shauangel/Desktop/chromedriver')
web.get("https://www.cwb.gov.tw/V8/C/C/Statistics/monthlydata.html")


class data:
    def __init__(self, year, month, name, temperature, humidity):
        self.year = year
        self.month = month
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
       
    def __iter__(self):
        return iter([self.year, self.month, self.name, self.temperature, self.humidity])
    
    def __repr__(self):
        return '{}年 {}月 {} {}度 {}%'.format(self.year, self.month, self.name, self.temperature, self.humidity)    

def Initfile(filename):
    with open(filename+".csv","w",encoding = 'utf-8',newline = '') as fp:
        writer = csv.DictWriter(fp, fieldnames = title, quotechar = "'")
        writer.writeheader()


def saveInfo(filename,data):
    obj = {}
    for n in range(len(title)):
        obj[title[n]] = data[n]
    with open(filename+".csv","a+",encoding = 'utf-8',newline = '') as fp:
        writer = csv.DictWriter(fp, fieldnames = title, quotechar = "'")
        writer.writerow(obj)

def getInfo(year, month):
    tr = table.find_elements_by_tag_name('tr')
    th = table.find_elements_by_tag_name('th')
    word = [i.text for i in th]
    for w in range(len(word)):
        if word[w] in stations2:
            td = tr[w].find_elements_by_tag_name('td')
            saveInfo('weather', [year, month, word[w], td[0].text, td[6].text])
            print(data(year, month, word[w], td[0].text, td[6].text))
  

stations2 = ['臺南', '高雄']
stations = ['臺中', '臺南', '恆春', '新屋', '高雄', '臺北', '新竹', '嘉義', '板橋', '宜蘭', '日月潭', '基隆', '花蓮', '臺東', '馬祖', '澎湖', '金門']
month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
year = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
year2020 = '2020'


for y in year :
    for m in month :
        selectY = Select(web.find_element_by_id('Year'))
        selectM = Select(web.find_element_by_id('Month'))
        selectY.select_by_visible_text(y)
        try:
            selectM.select_by_visible_text(m)
            
        except:
            selectM.select_by_value(m)
        time.sleep(1)
        table = web.find_element_by_id('MonthlyData_MOD')
        getInfo(y, m)
     
    
web.quit()  











