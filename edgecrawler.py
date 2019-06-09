# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:57:16 2019

@author: jeremy.chin.ee.wei
"""
import simplejson
import requests 
from bs4 import BeautifulSoup
pages=list(range(0,282))
url="https://www.theedgemarkets.com/flash-categories/hot-stock?page="
result=[]
for page in pages:
    page=requests.get(url+str(page))
    soup=BeautifulSoup(page.content, 'html.parser')
    news=soup.findAll("div",{"class":"views-field views-field-title"})
    hotnews=[pt.get_text() for pt in news]
    result.extend(hotnews)

f = open('edgenews.txt', 'w')
simplejson.dump(result, f)
f.close()